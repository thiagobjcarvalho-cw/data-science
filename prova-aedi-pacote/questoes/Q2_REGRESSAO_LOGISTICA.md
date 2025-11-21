# QUESTÃO 2: REGRESSÃO LOGÍSTICA (2,5 pontos)

## 📊 DATASET
**Nome:** Hotel Booking Demand  
**Target:** is_canceled (0 = não cancelou, 1 = cancelou)  
**Tipo:** Classificação Binária

---

## 🎯 OBJETIVO
Construir modelo de Regressão Logística para prever cancelamento de reservas hoteleiras.

---

## 📋 ETAPAS

### a) ANÁLISE DESCRITIVA (10% = 0,25 pts)

**Ações:**
- Carregar dataset
- Verificar balanceamento da variável target
  ```python
  print(df['is_canceled'].value_counts(normalize=True))
  # Se ratio > 70/30: considerar SMOTE ou class_weight
  ```

**Gráficos:**
1. Barplot: distribuição de is_canceled
2. Boxplots: lead_time, adr, total_of_special_requests vs is_canceled
3. Countplots: hotel, meal, market_segment vs is_canceled

**Análise bivariada:** Quais features aparentam ter relação com cancelamento?

---

### b) MODELO DE REGRESSÃO LOGÍSTICA (60% = 1,5 pts)

#### b.1 PREPROCESSING

```python
# 1. Tratar missing
df.fillna(df.median(), inplace=True)  # ou estratégia apropriada

# 2. Encoding
# One-Hot para nominais
df_encoded = pd.get_dummies(df, columns=['hotel', 'meal', 'market_segment'], drop_first=True)

# 3. Scaling (OBRIGATÓRIO para Logística)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42
)
```

#### b.2 TREINAR MODELO

```python
from sklearn.linear_model import LogisticRegression

# Se desbalanceamento > 70/30:
model = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
# Senão:
model = LogisticRegression(max_iter=1000, random_state=42)

model.fit(X_train, y_train)
```

**Hyperparameter tuning (opcional mas recomendado):**
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.01, 0.1, 1, 10]}
grid = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')
grid.fit(X_train, y_train)
best_model = grid.best_estimator_
```

#### b.3 AVALIAÇÃO COMPLETA

**Métricas obrigatórias:**
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:,1]

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")
print(f"AUC-ROC: {roc_auc_score(y_test, y_pred_proba):.4f}")
```

**Matriz de confusão:**
```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predito')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()
```

**Interpretação:**
"A matriz mostra [VP], [VN], [FP], [FN]. Falsos positivos ([número]) representam clientes que não cancelariam mas o modelo previu cancelamento. Isso pode levar a overbooking desnecessário."

**Curva ROC:**
```python
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, label=f'AUC = {roc_auc_score(y_test, y_pred_proba):.3f}')
plt.plot([0,1], [0,1], 'r--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curva ROC')
plt.legend()
plt.show()
```

**Análise de threshold:**
"O threshold padrão (0.5) resulta em recall de [X]. Se queremos capturar mais cancelamentos (aumentar recall), podemos reduzir threshold para 0.3, mas isso aumenta falsos positivos."

---

### c) ANÁLISE DE FEATURES (20% = 0,5 pts)

#### c.1 COEFICIENTES

```python
# Pegar coeficientes (após encoding)
feature_importance = pd.DataFrame({
    'Feature': feature_names,  # nomes após encoding
    'Coeficiente': model.coef_[0],
    'Odds Ratio': np.exp(model.coef_[0])
})

feature_importance = feature_importance.sort_values('Coeficiente', key=abs, ascending=False)
print(feature_importance.head(10))
```

**Interpretação de Odds Ratio:**
"Feature 'lead_time' tem coeficiente 0.8, resultando em Odds Ratio de exp(0.8) = 2.23. Isso significa que para cada unidade de aumento em lead_time, o odds de cancelamento multiplica por 2.23 (aumenta 123%)."

**Plot:**
```python
top_features = feature_importance.head(10)
top_features.plot(x='Feature', y='Coeficiente', kind='barh', figsize=(10,6))
plt.xlabel('Coeficiente')
plt.title('Top 10 Features - Regressão Logística')
plt.show()
```

#### c.2 PERMUTATION IMPORTANCE (validação)

```python
from sklearn.inspection import permutation_importance

perm_importance = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)
perm_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': perm_importance.importances_mean
}).sort_values('Importance', ascending=False)
```

**Comparar** com coeficientes para validar consistência.

#### c.3 INTERPRETAÇÃO CONTEXTUAL

**Para top 3 features, escrever parágrafo:**

"**Lead Time** (dias entre reserva e chegada) é a feature mais importante. Quanto maior o lead time, maior probabilidade de cancelamento. Isso ocorre porque reservas antecipadas estão sujeitas a mais mudanças de planos (viagens de negócio canceladas, férias remarcadas)."

"**Deposit Type** tem forte impacto negativo quando há depósito. Clientes que pagam depósito não-reembolsável têm incentivo financeiro para não cancelar."

"**Previous Cancellations** é preditor óbvio: comportamento passado é melhor indicador de comportamento futuro."

---

### d) JUSTIFICATIVA DO MÉTODO (10% = 0,25 pts)

**Responder em 2-3 parágrafos:**

**1. Por que Logística e NÃO Linear?**

"Regressão Linear é inapropriada para classificação binária porque:
- Output é contínuo (pode prever -0.3 ou 1.7, fora de [0,1])
- Não modela probabilidades adequadamente
- Pressupostos (normalidade de resíduos) não fazem sentido para variável binária

Regressão Logística usa função sigmoid para garantir output em [0,1], interpretável como probabilidade."

**2. Vantagens da Logística:**
- Interpretabilidade: coeficientes → odds ratios
- Eficiência: treina rápido mesmo com muitas features
- Baseline sólido: antes de testar modelos complexos (RF, XGBoost)
- Output probabilístico: permite ajustar threshold conforme custo de erros

**3. Limitações:**
- Assume linearidade no logit (log-odds)
- Não captura interações complexas automaticamente
- Desempenho inferior a ensemble methods em datasets grandes

---

## ✅ CHECKLIST Q2

- [ ] EDA com análise de balanceamento
- [ ] Preprocessing justificado (encoding, scaling)
- [ ] Modelo treinado com class_weight se necessário
- [ ] Todas métricas calculadas (Acc, Prec, Rec, F1, AUC)
- [ ] Matriz confusão + interpretação
- [ ] Curva ROC plotada
- [ ] Top features identificadas e interpretadas
- [ ] Odds ratios explicados
- [ ] Justificativa método vs Regressão Linear
- [ ] HTML exportado

---

## 🎯 DICAS

1. **Contexto hoteleiro** é chave - conecte features com comportamento de clientes
2. **Recall vs Precision:** Qual mais importante? Depende do custo de overbooking vs perder receita
3. **Threshold:** Não aceite 0.5 como padrão sem questionar
4. **Odds Ratio:** É difícil, explique com exemplos numéricos
