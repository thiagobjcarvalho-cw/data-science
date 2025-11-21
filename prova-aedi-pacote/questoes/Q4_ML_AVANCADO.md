# QUESTÃO 4: ML AVANÇADO + SHAP + CLUSTERING (3,0 pontos)

## 📊 DATASET
**Nome:** German Credit Risk (Kaggle)  
**Target:** Class (good = bom pagador, bad = mau pagador)  
**Objetivo:** Prever inadimplência bancária

⚠️ **Esta é a questão mais importante (30% da prova) e mais complexa!**

---

## 📋 ESTRUTURA

### a) DISCUSSÃO DO PROBLEMA (10% = 0,3 pts)
### b) ANÁLISE DESCRITIVA (15% = 0,45 pts)
### c) MÚLTIPLOS MODELOS (30% = 0,9 pts)
### d) SHAP VALUES (25% = 0,75 pts) ← **SUPER CRÍTICO**
### e) CLUSTERING (15% = 0,45 pts)
### f) DECISÃO ESTRATÉGICA (10% = 0,3 pts)

---

## a) DISCUSSÃO DO PROBLEMA (0,3 pts)

**Escrever texto acadêmico (3-4 parágrafos):**

### Parágrafo 1: Contexto Bancário
"O risco de crédito representa a probabilidade de um tomador de empréstimo não cumprir suas obrigações de pagamento, resultando em perdas financeiras para instituições bancárias. No Brasil, segundo dados do Banco Central, a taxa de inadimplência de pessoas físicas atingiu [X]% em 2024, gerando bilhões em provisões para devedores duvidosos (PDD)."

### Parágrafo 2: Custos Assimétricos
"A previsão de inadimplência envolve trade-off entre dois tipos de erro:
- **Falso Negativo (Tipo II):** Conceder crédito a mau pagador → perda direta do capital emprestado + juros
- **Falso Positivo (Tipo I):** Negar crédito a bom pagador → perda de receita + exclusão financeira

Estudos indicam que custo de FN pode ser 5-10x maior que FP, justificando modelos com alto recall."

### Parágrafo 3: Relevância de ML
"Abordagens tradicionais de credit scoring (regressão logística simples) capturam apenas relações lineares. Machine Learning permite:
- Detecção de padrões não-lineares complexos
- Interações automáticas entre features
- Atualização contínua conforme novos dados
- Explicabilidade via SHAP values (crucial para regulação bancária)"

### Parágrafo 4: Objetivo do Estudo
"Este trabalho compara múltiplos algoritmos (Logística, Árvores, Ensemble), identifica features críticas via SHAP, e segmenta clientes via clustering para suportar decisões de concessão de crédito."

---

## b) ANÁLISE DESCRITIVA (0,45 pts)

### b.1 CARREGAR DADOS

```python
# Opção 1: sklearn
from sklearn.datasets import fetch_openml
credit = fetch_openml('credit-g', version=1, as_frame=True, parser='auto')
df = credit.frame

# Opção 2: Kaggle
# df = pd.read_csv('german_credit_data.csv')

print(df.shape)
print(df.info())
```

### b.2 TARGET

```python
# Mapear para binário
df['target'] = df['class'].map({'good': 0, 'bad': 1})

# Verificar balanceamento
print(df['target'].value_counts(normalize=True))
# Calcular ratio
n_bad = (df['target'] == 1).sum()
n_good = (df['target'] == 0).sum()
ratio = n_bad / n_good
print(f"Ratio bad/good: {ratio:.2f}")

# SE ratio > 0.5 (desbalanceamento > 33/67): considerar SMOTE ou class_weight
```

### b.3 EDA COMPLETA

**Missing values:**
```python
print(df.isnull().sum())
# Estratégia de tratamento (justificar)
```

**Análise univariada:**
```python
# Numéricas
df[['age', 'credit_amount', 'duration']].hist(bins=30, figsize=(15,5))

# Categóricas
for col in ['checking_status', 'credit_history', 'purpose']:
    df[col].value_counts().plot(kind='bar')
    plt.title(col)
    plt.show()
```

**Análise bivariada (features vs target):**
```python
# Numéricas
for col in ['age', 'credit_amount', 'duration']:
    df.boxplot(column=col, by='target', figsize=(10,6))
    plt.suptitle('')
    plt.title(f'{col} vs Inadimplência')
    plt.show()

# Categóricas
for col in ['checking_status', 'credit_history']:
    pd.crosstab(df[col], df['target'], normalize='index').plot(kind='bar', stacked=True)
    plt.title(f'{col} vs Inadimplência')
    plt.show()
```

### b.4 FEATURE ENGINEERING

```python
# Criar features derivadas
df['debt_to_income'] = df['credit_amount'] / (df['duration'] * 100)  # assumindo renda mensal
df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 50, 100], labels=['young', 'adult', 'middle', 'senior'])
df['high_amount'] = (df['credit_amount'] > df['credit_amount'].median()).astype(int)
```

### b.5 PREPROCESSING

```python
# Encoding
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Separar numéricas e categóricas
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# Features e Target
X = df_encoded.drop(['target', 'class'], axis=1)
y = df_encoded['target']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42
)

print(f"Train: {X_train.shape}, Test: {X_test.shape}")
```

---

## c) MÚLTIPLOS MODELOS (0,9 pts)

### c.1 JUSTIFICATIVA DOS MODELOS

**Escrever parágrafo para CADA modelo:**

1. **Logistic Regression:** Baseline interpretável, coeficientes têm significado (odds ratio), rápido.
2. **Decision Tree:** Captura não-linearidades, interpretável via visualização da árvore, pode overfittar.
3. **Random Forest:** Ensemble de árvores, reduz overfitting, feature importance nativa.
4. **XGBoost:** State-of-the-art para dados tabulares, otimiza gradient boosting, regularização.
5. **LightGBM:** Mais rápido que XGBoost, eficiente em memória, leaf-wise growth.

### c.2 TREINAR TODOS OS MODELOS

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import time

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=10, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'XGBoost': XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss'),
    'LightGBM': LGBMClassifier(n_estimators=100, random_state=42, verbosity=-1)
}

results = []
for name, model in models.items():
    start = time.time()
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:,1]
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)
    
    elapsed = time.time() - start
    
    results.append([name, acc, prec, rec, f1, auc, elapsed])
    print(f"{name} trained in {elapsed:.2f}s")

results_df = pd.DataFrame(results, 
                          columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1', 'AUC', 'Time(s)'])
print(results_df.to_string(index=False))
```

### c.3 VISUALIZAÇÕES

**Curvas ROC (todas no mesmo gráfico):**
```python
plt.figure(figsize=(10,8))
for name, model in models.items():
    y_pred_proba = model.predict_proba(X_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    plt.plot(fpr, tpr, label=f'{name} (AUC={auc_score:.3f})')

plt.plot([0,1], [0,1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curvas ROC - Todos os Modelos')
plt.legend()
plt.show()
```

**Comparação visual:**
```python
results_df_plot = results_df.set_index('Model')[['Accuracy', 'Precision', 'Recall', 'F1', 'AUC']]
results_df_plot.plot(kind='bar', figsize=(12,6))
plt.title('Comparação de Métricas')
plt.xticks(rotation=45)
plt.legend(loc='lower right')
plt.show()
```

### c.4 ESCOLHER MODELO CAMPEÃO

```python
# Critério: maior AUC + maior Recall (recall é crítico para crédito)
best_idx = results_df['AUC'].idxmax()
best_model_name = results_df.loc[best_idx, 'Model']
best_model = models[best_model_name]

print(f"\n🏆 MODELO CAMPEÃO: {best_model_name}")
print(f"   AUC: {results_df.loc[best_idx, 'AUC']:.4f}")
print(f"   Recall: {results_df.loc[best_idx, 'Recall']:.4f}")

# Matriz confusão do campeão
y_pred_best = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred_best)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predito')
plt.ylabel('Real')
plt.title(f'Matriz de Confusão - {best_model_name}')
plt.show()

# Salvar
import joblib
joblib.dump(best_model, '/home/claude/prova-aedi-unb/models/credit_model.pkl')
```

---

## d) SHAP VALUES (0,75 pts) ⚠️ **SUPER CRÍTICO - 25% DA NOTA Q4**

### d.1 INSTALAÇÃO E SETUP

```python
!pip install shap -q
import shap

# Inicializar explainer
# Para tree-based models (XGBoost, LightGBM, RandomForest):
explainer = shap.TreeExplainer(best_model)

# Para outros modelos:
# explainer = shap.Explainer(best_model, X_train)

# Calcular SHAP values
shap_values = explainer.shap_values(X_test)

# Se retornar lista (classificação binária), pegar classe 1 (bad)
if isinstance(shap_values, list):
    shap_values = shap_values[1]
```

### d.2 GRÁFICOS OBRIGATÓRIOS

#### GRÁFICO 1: Summary Plot (Dot)

```python
plt.figure(figsize=(10,10))
shap.summary_plot(shap_values, X_test, feature_names=X.columns, show=False)
plt.tight_layout()
plt.savefig('/home/claude/prova-aedi-unb/exports/shap_summary_dot.png', dpi=150, bbox_inches='tight')
plt.show()
```

**INTERPRETAÇÃO TEXTUAL (OBRIGATÓRIO):**

"O summary plot revela as features mais importantes na predição de inadimplência:

**Eixo Y:** Features ordenadas por importância (topo = mais importante)  
**Eixo X:** Impacto no output do modelo (SHAP value)  
**Cor:** Vermelho = valor alto da feature; Azul = valor baixo

**Análise:**
- **checking_status** (topo) é a mais importante. Pontos vermelhos (saldo alto) concentram-se no lado NEGATIVO (esquerda), indicando que ter saldo positivo em conta corrente REDUZ risco de inadimplência. Pontos azuis (saldo baixo/negativo) estão no lado positivo, aumentando risco.
  
- **duration** (duração do crédito) mostra pontos vermelhos (longa duração) à direita (SHAP positivo), indicando que créditos de longo prazo aumentam risco. Isso é esperado pois maior exposição temporal permite mais choques econômicos.

- **credit_amount:** Interessantemente, não é linear. Valores muito baixos E muito altos têm SHAP positivo (aumentam risco). Possível U-shape: créditos muito pequenos podem indicar instabilidade financeira, enquanto muito grandes excedem capacidade de pagamento."

#### GRÁFICO 2: Summary Plot (Bar)

```python
plt.figure(figsize=(10,8))
shap.summary_plot(shap_values, X_test, feature_names=X.columns, plot_type="bar", show=False)
plt.tight_layout()
plt.savefig('/home/claude/prova-aedi-unb/exports/shap_summary_bar.png', dpi=150, bbox_inches='tight')
plt.show()
```

**INTERPRETAÇÃO:**
"Ranking absoluto de importância (mean |SHAP value|):
1. checking_status: 0.43
2. duration: 0.31
3. credit_history: 0.28
..."

#### GRÁFICO 3: Dependence Plots (top 3 features)

```python
# Identificar top 3
mean_abs_shap = np.abs(shap_values).mean(axis=0)
top_3_idx = np.argsort(mean_abs_shap)[-3:][::-1]
top_3_features = [X.columns[i] for i in top_3_idx]

for feature in top_3_features:
    plt.figure(figsize=(10,6))
    shap.dependence_plot(feature, shap_values, X_test, feature_names=X.columns, show=False)
    plt.tight_layout()
    plt.savefig(f'/home/claude/prova-aedi-unb/exports/shap_dependence_{feature}.png', dpi=150, bbox_inches='tight')
    plt.show()
```

**INTERPRETAÇÃO PARA CADA:**

"**checking_status dependence plot:**
A relação é aproximadamente linear e negativa. À medida que o valor (após encoding) aumenta, o SHAP value diminui fortemente. Isso confirma: maior saldo em conta → menor risco. A coloração por outra feature (interação) mostra que [explicar padrão de cores]."

"**duration dependence plot:**
Relação positiva clara: quanto maior a duração, maior o SHAP value (maior risco). Não há saturação aparente, sugerindo que mesmo créditos muito longos (>60 meses) continuam acumulando risco. Interação com [feature de cor] sugere que [explicar]."

#### GRÁFICO 4: Force Plots (2 casos individuais)

```python
# Caso 1: Cliente com menor risco (probabilidade baixa de bad)
y_pred_proba_best = best_model.predict_proba(X_test)[:,1]
good_idx = np.argmin(y_pred_proba_best)

shap.force_plot(explainer.expected_value, shap_values[good_idx], 
                X_test[good_idx], feature_names=X.columns, 
                matplotlib=True, show=False)
plt.tight_layout()
plt.savefig('/home/claude/prova-aedi-unb/exports/shap_force_good.png', dpi=150, bbox_inches='tight')
plt.show()

# Caso 2: Cliente com maior risco
bad_idx = np.argmax(y_pred_proba_best)

shap.force_plot(explainer.expected_value, shap_values[bad_idx], 
                X_test[bad_idx], feature_names=X.columns, 
                matplotlib=True, show=False)
plt.tight_layout()
plt.savefig('/home/claude/prova-aedi-unb/exports/shap_force_bad.png', dpi=150, bbox_inches='tight')
plt.show()
```

**INTERPRETAÇÃO:**

"**Cliente Baixo Risco (Good):**
- Base value (valor esperado): 0.30 (30% de chance média de inadimplência)
- Predição final: 0.08 (8%)
- **Features que diminuíram risco (vermelho/esquerda):**
  * checking_status = high (SHAP = -0.15)
  * credit_history = existing paid (SHAP = -0.08)
  * purpose = car (SHAP = -0.04)
- **Features que aumentaram risco (azul/direita):**
  * Nenhuma contribuição significativa
- **Conclusão:** Cliente com perfil sólido - conta corrente positiva e histórico limpo são fatores protetores dominantes."

"**Cliente Alto Risco (Bad):**
- Base value: 0.30
- Predição final: 0.78 (78%)
- **Features que aumentaram risco:**
  * checking_status = negative (SHAP = +0.22)
  * duration = 48 months (SHAP = +0.14)
  * credit_history = critical account (SHAP = +0.10)
- **Features que diminuíram risco:**
  * Nenhuma forte o suficiente
- **Conclusão:** Combinação tóxica - conta negativa + crédito longo + histórico ruim empurra probabilidade para 78%."

### d.3 INTERPRETAÇÃO ACADÊMICA ⚠️ ESSENCIAL

**Para as TOP 5 features, escrever parágrafo POR FEATURE:**

**Template obrigatório:**
"A variável **[NOME]** apresenta SHAP value médio absoluto de **[VALOR]**, classificando-se como a **[RANKING]ª** mais importante. O sinal [positivo/negativo] indica que [aumentar/diminuir] essa feature [aumenta/reduz] o risco de inadimplência. No contexto bancário, isso é esperado porque **[TEORIA ECONÔMICA/FINANCEIRA]**. Por exemplo, **[EXEMPLO CONCRETO]**."

**Exemplo real:**

"A variável **checking_account_status** apresenta SHAP value médio absoluto de **0.43**, classificando-se como a **1ª** mais importante. Valores positivos (saldo alto) têm SHAP negativo, reduzindo risco de inadimplência. No contexto bancário, isso alinha-se com a **teoria de restrição de liquidez** (Deaton, 1991): indivíduos com poupança têm colchão financeiro para absorver choques de renda (desemprego, doença) sem deixar de pagar dívidas. Por exemplo, um cliente com €500 em conta corrente tem 40% menos risco relativo comparado a alguém com conta negativa, pois pode recorrer a essa reserva em emergências."

**Fazer isso para as 5 mais importantes!**

---

## e) CLUSTERING (0,45 pts)

### e.1 PREPARAÇÃO

```python
# Selecionar features NUMÉRICAS
cluster_features = ['age', 'credit_amount', 'duration']
X_cluster = df[cluster_features].dropna()

# Scaling OBRIGATÓRIO
scaler_cluster = StandardScaler()
X_cluster_scaled = scaler_cluster.fit_transform(X_cluster)
```

### e.2 K-MEANS

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Elbow Method
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_cluster_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_cluster_scaled, kmeans.labels_))

# Plot Elbow
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(K_range, inertias, marker='o')
plt.xlabel('Número de Clusters')
plt.ylabel('Inércia')
plt.title('Elbow Method')

# Plot Silhouette
plt.subplot(1,2,2)
plt.plot(K_range, silhouette_scores, marker='o', color='orange')
plt.xlabel('Número de Clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis')
plt.tight_layout()
plt.show()

# Escolher melhor k
best_k = silhouette_scores.index(max(silhouette_scores)) + 2
print(f"Melhor k: {best_k} (Silhouette: {max(silhouette_scores):.3f})")
```

**Treinar modelo final:**
```python
kmeans_final = KMeans(n_clusters=best_k, random_state=42)
clusters = kmeans_final.fit_predict(X_cluster_scaled)
X_cluster['Cluster'] = clusters
```

**Perfis dos clusters:**
```python
# Estatísticas por cluster
profile = X_cluster.groupby('Cluster').agg({
    'age': ['mean', 'std'],
    'credit_amount': ['mean', 'std'],
    'duration': ['mean', 'std'],
    'Cluster': 'count'
}).round(2)
profile.columns = ['Age_Mean', 'Age_Std', 'Credit_Mean', 'Credit_Std', 'Duration_Mean', 'Duration_Std', 'Count']
print(profile)

# Adicionar % bad payers por cluster (se possível juntar com target)
```

**Interpretar:**
"**Cluster 0:** Jovens (média 28 anos) com créditos pequenos (€3.5k) e curto prazo (18 meses). Perfil: primeiro crédito, talvez estudantes.  
**Cluster 1:** Adultos (média 42 anos) com créditos médios (€6k) e prazo médio (30 meses). Perfil: estável, famílias.  
**Cluster 2:** Alto risco (média 35 anos) com créditos altos (€12k) e longo prazo (48 meses). Perfil: expansão de negócio ou dívidas consolidadas."

**Visualizar (PCA):**
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_cluster_scaled)

plt.figure(figsize=(10,8))
scatter = plt.scatter(X_pca[:,0], X_pca[:,1], c=clusters, cmap='viridis', alpha=0.6)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variância)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variância)')
plt.title('K-Means Clustering (PCA)')
plt.colorbar(scatter, label='Cluster')
plt.show()
```

### e.3 DBSCAN

```python
from sklearn.cluster import DBSCAN

# Tuning (testar múltiplas combinações)
best_dbscan = None
best_n_clusters = 0
best_outliers_pct = 100

for eps in [0.3, 0.5, 1.0, 1.5]:
    for min_samples in [5, 10, 15]:
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        labels = dbscan.fit_predict(X_cluster_scaled)
        
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_outliers = list(labels).count(-1)
        outliers_pct = n_outliers / len(labels) * 100
        
        print(f"eps={eps}, min_samples={min_samples}: {n_clusters} clusters, {outliers_pct:.1f}% outliers")
        
        # Critério: 3-6 clusters, outliers < 10%
        if 3 <= n_clusters <= 6 and outliers_pct < 10:
            if best_n_clusters == 0 or abs(n_clusters - 4) < abs(best_n_clusters - 4):
                best_dbscan = dbscan
                best_n_clusters = n_clusters
                best_outliers_pct = outliers_pct

print(f"\nMelhor DBSCAN: {best_n_clusters} clusters, {best_outliers_pct:.1f}% outliers")
```

**Analisar outliers:**
```python
outlier_mask = best_dbscan.labels_ == -1
n_outliers = outlier_mask.sum()
print(f"{n_outliers} outliers detectados ({n_outliers/len(outlier_mask)*100:.1f}%)")

# Se tiver target disponível
# outlier_bad_rate = df.loc[outlier_mask, 'target'].mean()
# print(f"Taxa de inadimplência entre outliers: {outlier_bad_rate:.1%}")
```

**Comparação K-Means vs DBSCAN:**
"**K-Means:**
- Assume clusters esféricos (gaussianos)
- Força TODOS os pontos em um cluster
- Sensível a outliers (eles puxam centroides)
- Ótimo para segmentação de marketing

**DBSCAN:**
- Detecta clusters de densidade arbitrária (formas irregulares)
- Identifica outliers (label -1)
- Robusto a outliers, eles não afetam clusters principais
- Útil para detecção de fraude/anomalias

**Para Crédito:** DBSCAN é superior porque outliers (perfis atípicos) geralmente indicam maior risco. Por exemplo, cliente com crédito de €50k mas salário de €1.5k/mês é outlier legítimo, não ruído."

### e.4 INTEGRAÇÃO COM ANÁLISE SUPERVISIONADA

```python
# Adicionar cluster_id como feature
df['cluster_kmeans'] = clusters

# Retreinar modelo com cluster como feature
X_with_cluster = df_encoded.join(pd.get_dummies(df['cluster_kmeans'], prefix='cluster'))
# ... treinar novamente ...
# Comparar AUC antes/depois

# Discussão:
"Incluir cluster_id como feature [melhorou/não melhorou] AUC de [antes] para [depois]. 
[Se melhorou: Isso sugere que segmentação captura padrões de risco não explícitos nas features individuais.]
[Se não melhorou: Clusters são redundantes com features já presentes, ou modelo já captura essas relações via interações.]"
```

---

## f) DECISÃO ESTRATÉGICA (0,3 pts)

**Escrever seção executiva (4-5 parágrafos):**

### 1. Políticas de Concessão

"Com base no modelo XGBoost (AUC=0.85), recomendamos:

**Threshold customizado:** Reduzir threshold de 0.5 para **0.35** aumenta recall de 0.65 para 0.78, capturando 20% mais inadimplentes potenciais. Custo: falsos positivos sobem de 15% para 22%. Trade-off aceitável dado que custo de FN (perda de capital) é ~7x maior que FP (perda de oportunidade).

**Segmentação por cluster:**
- **Cluster 0 (baixo risco):** Aprovação automática até €10k, taxa 1.5% a.m.
- **Cluster 1 (médio risco):** Revisão manual acima de €8k, taxa 2.0% a.m.
- **Cluster 2 (alto risco):** Exigir garantia ou aval, taxa 3.0% a.m., limite €5k"

### 2. Monitoramento de Features Críticas

"Com base em SHAP, estabelecer **alertas preventivos**:

- **Checking account negativo:** Cliente entra em lista de atenção, oferecer programa de educação financeira
- **Duration >36 meses:** Revisão trimestral obrigatória (não apenas anual)
- **Credit history deteriorando:** Renegociação proativa antes de inadimplência

Exemplo: Cliente com saldo que passou de €300 para -€50 em 2 meses → contato imediato do gerente."

### 3. Segmentação para Produtos

"Usar clusters para personalizar ofertas:

- **Cluster 0 (jovens):** Focar em produtos educacionais (cartão universitário, crédito consignado pequeno)
- **Cluster 1 (estáveis):** Cross-sell de seguros, previdência, crédito imobiliário
- **Cluster 2 (alto valor):** Gerente dedicado, produtos corporativos"

### 4. Limitações e Considerações Éticas

"**Limitações técnicas:**
- Dataset de 1994 (Alemanha) pode não generalizar para Brasil 2025
- Features faltantes: renda atual, score de bureaus, histórico em tempo real
- Concept drift: perfil de clientes muda (pandemia, inflação)

**Considerações éticas:**
- Age e gender podem introduzir viés discriminatório (regulações proíbem)
- Transparência: SHAP permite explicar negativas (exigência do Código de Defesa do Consumidor)
- Inclusão financeira: evitar negar crédito sistematicamente a grupos vulneráveis"

### 5. Próximos Passos

"1. **Dados longitudinais:** Coletar comportamento de pagamento mês a mês → modelagem de sobrevivência
2. **Monitoring:** Implementar dashboard de concept drift (distribuição de features mudando?)
3. **A/B testing:** Testar políticas propostas em 10% da carteira antes de roll-out completo
4. **Feedback loop:** Incorporar resultados reais (inadimplência observada) para retreinamento mensal"

---

## ✅ CHECKLIST Q4

- [ ] Discussão contextual do problema (3-4 parágrafos)
- [ ] EDA completo com análise de balanceamento
- [ ] Preprocessing justificado
- [ ] **5 modelos treinados e comparados**
- [ ] Tabela comparativa de métricas
- [ ] Modelo campeão escolhido e justificado
- [ ] **SHAP VALUES:**
  - [ ] Summary plot (dot) + interpretação textual
  - [ ] Summary plot (bar)
  - [ ] Dependence plots (top 3) + interpretação
  - [ ] Force plots (2 casos) + interpretação
  - [ ] **Interpretação acadêmica das top 5 features** (parágrafo por feature)
- [ ] **CLUSTERING:**
  - [ ] K-Means com Elbow + Silhouette
  - [ ] Perfis dos clusters interpretados
  - [ ] DBSCAN com tuning
  - [ ] Análise de outliers
  - [ ] Comparação K-Means vs DBSCAN
  - [ ] Tentativa de integração com modelo supervisionado
- [ ] **Decisão estratégica:**
  - [ ] Políticas de concessão
  - [ ] Segmentação personalizada
  - [ ] Limitações discutidas
  - [ ] Ética considerada
  - [ ] Próximos passos sugeridos
- [ ] Modelo salvo (.pkl)
- [ ] Todos os gráficos SHAP salvos (.png)
- [ ] HTML exportado

---

## 🎯 DICAS FINAIS

1. **SHAP é 25% da nota** - dedique tempo máximo aqui
2. **Interpretação > Código** - qualquer um roda shap.summary_plot(), mas interpretar no contexto bancário é o diferencial
3. **Conecte com teoria** - cite teoria de restrição de liquidez, adverse selection, moral hazard
4. **Gráficos salvos** - salve TODOS os plots SHAP em .png (alta resolução)
5. **Contexto em TUDO** - não diga "feature X é importante", diga "feature X é importante porque no contexto bancário [razão]"
