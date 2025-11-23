# 🔥💀 PROMPT DE EXECUÇÃO - MELHORIAS VISUAIS COM PLOTLY 💀🔥

## 📋 CONTEXTO

**Objetivo:** Melhorar visualmente os 4 notebooks da Prova AEDI (Q1, Q2, Q3, Q4) aplicando o estilo profissional do `Prova_AEDI_V2.ipynb` que usa Plotly de forma exemplar.

**Branch:** `feature/melhorias-visuais-plotly`

**Referência Visual:** `/home/thiago/projetos/codewave/data-science/material-base/Prova_AEDI_V2.ipynb`

---

## 🎯 OBJETIVOS GERAIS

### O QUE FAZER:
1. ✅ Substituir TODOS os gráficos matplotlib/seaborn por Plotly interativo
2. ✅ Aplicar template `plotly_white` (fundo branco profissional)
3. ✅ Adicionar `@title` em TODAS as células de código
4. ✅ Usar tabelas formatadas com `.style.background_gradient()`
5. ✅ Adicionar anotações inteligentes nos gráficos (`add_vline`, `add_annotation`)
6. ✅ Melhorar títulos com HTML bold (`<b>Título:</b> Subtítulo`)
7. ✅ Usar símbolos visuais (✅ ⚠️ ❌ >>) nos outputs
8. ✅ Manter TODO o rigor estatístico e análises existentes (SHAP, pressupostos, etc)

### O QUE NÃO FAZER:
- ❌ NÃO remover análises estatísticas (VIF, Durbin-Watson, Breusch-Pagan, SHAP)
- ❌ NÃO mudar a lógica dos modelos
- ❌ NÃO adicionar mapas geográficos onde não há dados geo (apenas Q1 tem lat/long)

---

## 📦 SETUP INICIAL (APLICAR EM TODOS OS 4 NOTEBOOKS)

### Cell 1 - Imports com Plotly (substituir imports existentes)

```python
# @title Imports e Configurações Globais

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, \
                            accuracy_score, precision_score, recall_score, f1_score, \
                            roc_auc_score, roc_curve, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb
import shap
import warnings

warnings.filterwarnings('ignore')

# CONFIGURAÇÃO GLOBAL PLOTLY - CRÍTICO!
px.defaults.template = "plotly_white"

print("✅ Bibliotecas carregadas com sucesso!")
```

---

## 🎨 TRANSFORMAÇÕES ESPECÍFICAS POR TIPO DE GRÁFICO

### 1. HISTOGRAMAS (DE MATPLOTLIB PARA PLOTLY)

**ANTES (matplotlib):**
```python
plt.hist(df['price'], bins=50, edgecolor='black', alpha=0.7)
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.title('Distribuição do Preço')
plt.show()
```

**DEPOIS (Plotly com anotações):**
```python
# @title Análise de Distribuição - Target Variable

fig_hist = px.histogram(
    df,
    x='price',
    nbins=50,
    title='<b>Distribuição de Preços:</b> Análise de Assimetria',
    labels={'price': 'Preço ($)'},
    color_discrete_sequence=['#1f77b4']
)

# Linha de média com anotação
fig_hist.add_vline(
    x=df['price'].mean(),
    line_dash="dash",
    line_color="red",
    annotation_text=f"Média: ${df['price'].mean():,.0f}",
    annotation_position="top right"
)

# Anotação de outliers (se necessário)
q3 = df['price'].quantile(0.75)
iqr = df['price'].quantile(0.75) - df['price'].quantile(0.25)
outlier_threshold = q3 + 1.5 * iqr

fig_hist.add_annotation(
    x=outlier_threshold * 1.5,
    y=100,
    text="Outliers (Imóveis de Luxo)",
    showarrow=True,
    arrowhead=2
)

fig_hist.show()

print(f"Skewness: {df['price'].skew():.3f}")
print(f"Kurtosis: {df['price'].kurt():.3f}")
```

---

### 2. MATRIZ DE CORRELAÇÃO (DE SEABORN PARA PLOTLY)

**ANTES (seaborn):**
```python
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
```

**DEPOIS (Plotly imshow):**
```python
# @title Matriz de Correlação - Pearson

corr_matrix = df[numeric_features + ['price']].corr()

fig_corr = px.imshow(
    corr_matrix,
    text_auto='.2f',  # Mostra valores com 2 decimais
    aspect="auto",
    height=700,
    title='<b>Matriz de Correlação:</b> Pearson',
    color_continuous_scale='RdBu_r',  # Red-Blue reversed
    origin='lower'  # Começa do zero embaixo
)

fig_corr.show()

print('\n✅ Correlações com preço (ordenadas):')
print(corr_matrix['price'].sort_values(ascending=False))
```

---

### 3. SCATTER PLOTS (DE MATPLOTLIB PARA PLOTLY)

**ANTES (matplotlib):**
```python
plt.scatter(df[feature], df['price'], alpha=0.3)
plt.xlabel(feature)
plt.ylabel('Price')
plt.show()
```

**DEPOIS (Plotly scatter):**
```python
# @title Análise de Correlação - Scatter Plots

fig = px.scatter(
    df,
    x=feature,
    y='price',
    title=f'<b>Price vs {feature}:</b> Correlação = {corr:.3f}',
    labels={feature: feature, 'price': 'Preço ($)'},
    opacity=0.3,
    color_discrete_sequence=['#1f77b4']
)

fig.update_traces(marker=dict(size=4))
fig.show()
```

---

### 4. DIAGNÓSTICO DE RESÍDUOS (SUBPLOTS COM Q-Q PLOT)

**DEPOIS (Plotly make_subplots):**
```python
# @title Diagnóstico de Resíduos - Pressupostos

residuals = y_train - y_train_pred

fig_diag = make_subplots(
    rows=1, cols=2,
    subplot_titles=(
        "Resíduos vs Ajustados (Homocedasticidade)",
        "Q-Q Plot (Normalidade)"
    )
)

# Plot 1: Scatter de resíduos
fig_diag.add_trace(
    go.Scatter(
        x=y_train_pred,
        y=residuals,
        mode='markers',
        marker=dict(opacity=0.5, size=4, color='#1f77b4'),
        name='Resíduos'
    ),
    row=1, col=1
)

# Linha de referência zero
fig_diag.add_hline(y=0, line_dash="dash", line_color="red", row=1, col=1)

# Plot 2: Q-Q Plot manual
qq_theory, qq_sample = stats.probplot(residuals, dist="norm")[0]

fig_diag.add_trace(
    go.Scatter(
        x=qq_theory,
        y=qq_sample,
        mode='markers',
        marker=dict(color='#1f77b4', size=4),
        name='Q-Q'
    ),
    row=1, col=2
)

# Linha teórica
fig_diag.add_trace(
    go.Scatter(
        x=[qq_theory.min(), qq_theory.max()],
        y=[qq_theory.min(), qq_theory.max()],
        mode='lines',
        line=dict(color='red', dash='dash'),
        showlegend=False
    ),
    row=1, col=2
)

fig_diag.update_layout(
    title='<b>Diagnóstico de Resíduos:</b> Validação de Pressupostos',
    height=500
)

fig_diag.show()

print("✅ Gráficos de diagnóstico gerados")
```

---

### 5. GRÁFICOS DE BARRAS HORIZONTAIS (FEATURE IMPORTANCE, ODDS RATIOS)

**DEPOIS (Plotly bar horizontal com gradiente):**
```python
# @title Feature Importance / Odds Ratios

# DataFrame com impactos
impact_df = pd.DataFrame({
    'Feature': feature_names,
    'Impact': impact_values
})

fig_impact = px.bar(
    impact_df.sort_values('Impact'),
    x='Impact',
    y='Feature',
    orientation='h',
    title='<b>Drivers de Negócio:</b> Impacto Quantificado',
    text_auto='.1f',  # Mostra valores nas barras
    labels={'Impact': 'Impacto Estimado (%)'},
    color='Impact',
    color_continuous_scale='Viridis'  # Gradiente amarelo→verde→azul
)

# Linha de referência no zero
fig_impact.add_vline(x=0, line_color='black')

fig_impact.update_layout(height=600, showlegend=False)
fig_impact.show()
```

---

### 6. MATRIZ DE CONFUSÃO (PLOTLY HEATMAP)

**DEPOIS (Plotly imshow):**
```python
# @title Matriz de Confusão

cm = confusion_matrix(y_test, y_pred)

# Calcular percentuais
cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100

# Criar anotações
annotations = []
for i in range(len(cm)):
    for j in range(len(cm)):
        annotations.append(
            dict(
                text=f"{cm[i, j]}<br>({cm_percent[i, j]:.1f}%)",
                x=j,
                y=i,
                showarrow=False,
                font=dict(color="white" if cm[i, j] > cm.max() / 2 else "black")
            )
        )

fig_cm = go.Figure(data=go.Heatmap(
    z=cm,
    x=['Não Cancelou', 'Cancelou'],  # Labels das classes
    y=['Não Cancelou', 'Cancelou'],
    colorscale='Blues',
    showscale=True
))

fig_cm.update_layout(
    title='<b>Matriz de Confusão:</b> Performance do Classificador',
    xaxis=dict(title="Predito"),
    yaxis=dict(title="Real"),
    annotations=annotations,
    width=600,
    height=500
)

fig_cm.show()
```

---

### 7. CURVA ROC (PLOTLY)

**DEPOIS (Plotly lines):**
```python
# @title Curva ROC

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc_score = roc_auc_score(y_test, y_pred_proba)

fig_roc = go.Figure()

# Curva ROC
fig_roc.add_trace(go.Scatter(
    x=fpr,
    y=tpr,
    mode='lines',
    name=f'ROC Curve (AUC = {auc_score:.3f})',
    line=dict(color='darkorange', width=2)
))

# Linha de referência (classificador aleatório)
fig_roc.add_trace(go.Scatter(
    x=[0, 1],
    y=[0, 1],
    mode='lines',
    name='Random Classifier',
    line=dict(color='navy', width=2, dash='dash')
))

fig_roc.update_layout(
    title='<b>Curva ROC:</b> Capacidade de Discriminação',
    xaxis=dict(title='False Positive Rate'),
    yaxis=dict(title='True Positive Rate'),
    width=700,
    height=600,
    legend=dict(x=0.6, y=0.1)
)

fig_roc.show()
```

---

### 8. MAPA GEOGRÁFICO (APENAS Q1 - King County tem lat/long)

**DEPOIS (Plotly scatter_mapbox):**
```python
# @title Geo-Spatial Analysis - Concentração de Valor

fig_map = px.scatter_mapbox(
    df,
    lat="lat",
    lon="long",
    color="price",
    size="sqft_living",
    color_continuous_scale=px.colors.sequential.Jet,  # Red hot para caros
    size_max=15,
    zoom=8.5,
    title="<b>Geo-Spatial Analysis:</b> Concentração de Valor (Norte vs Sul)",
    mapbox_style="carto-positron",  # Mapa limpo
    height=600,
    hover_data=['price', 'sqft_living', 'grade']
)

fig_map.show()

print("✅ Análise geográfica: Norte concentra imóveis de maior valor")
```

---

## 📊 TABELAS FORMATADAS COM ESTILO

### Aplicar em tabelas de estatísticas, VIF, comparação de modelos

```python
# @title Tabela de Resultados - Formatação Profissional

# Tabela de estatísticas descritivas
desc_stats = df[['price', 'sqft_living', 'grade']].describe().T
desc_stats['skewness'] = df[['price', 'sqft_living', 'grade']].skew()

display(
    desc_stats[['mean', '50%', 'std', 'min', 'max', 'skewness']]
    .style
    .background_gradient(cmap='Blues', subset=['skewness'])
    .format({'mean': '{:.2f}', 'std': '{:.2f}', 'skewness': '{:.2f}'})
)

print("Nota: Skewness > 1 indica forte assimetria à direita")
```

```python
# Tabela VIF
vif_data = pd.DataFrame({
    'Feature': X.columns,
    'VIF': [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
})

display(
    vif_data.sort_values(by="VIF", ascending=False)
    .style
    .background_gradient(cmap='Reds')  # Red para VIF alto = ruim
    .format({'VIF': '{:.2f}'})
)

print("\n✅ Critério: VIF > 5 requer atenção; VIF > 10 é crítico")
```

---

## 🎨 PRINTS COM SÍMBOLOS VISUAIS

### Aplicar em TODOS os prints de status e resultados de testes

```python
# Verificação de dados faltantes
if df.isnull().sum().sum() == 0:
    print("✅ Data Quality: Base íntegra, sem valores ausentes")
else:
    print(f"⚠️ Atenção: {df.isnull().sum().sum()} valores ausentes detectados")

# Resultado de testes estatísticos
print(f"\n--- Teste de Breusch-Pagan (Homocedasticidade) ---")
print(f"P-value: {bp_test[1]:.6f}")

if bp_test[1] > 0.05:
    print(f">> ✅ Homocedasticidade aceita (p > 0.05)")
else:
    print(f">> ❌ Heterocedasticidade detectada (p < 0.05)")
    print(f">> Recomendação: Transformação logarítmica ou modelo robusto")

# VIF
high_vif = vif_data[vif_data['VIF'] > 10]
if len(high_vif) > 0:
    print(f"❌ Variáveis com VIF > 10:\n{high_vif}")
else:
    print("✅ Multicolinearidade: Todas as variáveis com VIF < 10")
```

---

## 📝 CHECKLIST DE APLICAÇÃO POR NOTEBOOK

### ✅ Q1_Regressao_Linear.ipynb

**Células a modificar:**

1. **Cell Imports:**
   - [ ] Adicionar Plotly imports
   - [ ] Adicionar `px.defaults.template = "plotly_white"`
   - [ ] Adicionar `@title`

2. **Cell Histograma de Price:**
   - [ ] Trocar `plt.hist()` por `px.histogram()`
   - [ ] Adicionar `add_vline()` para média
   - [ ] Adicionar `add_annotation()` para outliers

3. **Cell Matriz de Correlação:**
   - [ ] Trocar `sns.heatmap()` por `px.imshow()`
   - [ ] Usar `color_continuous_scale='RdBu_r'`

4. **Cell Scatter Plots:**
   - [ ] Trocar `plt.scatter()` por `px.scatter()`
   - [ ] Adicionar títulos em HTML bold

5. **Cell Diagnóstico de Resíduos:**
   - [ ] Usar `make_subplots()` com 2 plots
   - [ ] Q-Q Plot manual com `go.Scatter()`
   - [ ] Adicionar `add_hline()` no scatter de resíduos

6. **Cell Mapa Geográfico (NOVO - Q1 tem lat/long!):**
   - [ ] Adicionar `px.scatter_mapbox()`
   - [ ] Usar `color="price"` e `size="sqft_living"`

7. **Cell Predito vs Real:**
   - [ ] Trocar `plt.scatter()` por `px.scatter()`
   - [ ] Usar `make_subplots()` para Train e Test lado a lado

8. **Cells de Tabelas:**
   - [ ] Adicionar `.style.background_gradient()` em VIF
   - [ ] Adicionar em estatísticas descritivas

9. **Todos os Prints:**
   - [ ] Adicionar símbolos ✅ ⚠️ ❌ >>

---

### ✅ Q2_Regressao_Logistica.ipynb

**Células a modificar:**

1. **Cell Imports:**
   - [ ] Igual Q1

2. **Cell Distribuição Target:**
   - [ ] `px.histogram()` para `is_canceled`
   - [ ] Mostrar balanceamento das classes

3. **Cell Matriz de Confusão:**
   - [ ] `go.Heatmap()` com anotações de valores e percentuais

4. **Cell Curva ROC:**
   - [ ] `go.Figure()` com linha ROC + linha aleatória

5. **Cell Odds Ratios:**
   - [ ] `px.bar()` horizontal com `orientation='h'`
   - [ ] `color_continuous_scale='Viridis'`
   - [ ] `add_vline(x=1)` para marcar OR neutro
   - [ ] `text_auto='.2f'` para mostrar valores

6. **Cell Feature Importance:**
   - [ ] `px.bar()` horizontal com top 15-20 features

7. **Tabelas:**
   - [ ] Métricas com `.style.background_gradient(cmap='Blues')`

---

### ✅ Q3_ANOVA.ipynb

**Células a modificar:**

1. **Cell Imports:**
   - [ ] Igual Q1

2. **Cell Box Plots por País:**
   - [ ] Trocar `sns.boxplot()` por `px.box()`
   - [ ] Adicionar título descritivo

3. **Cell Estatísticas por Grupo:**
   - [ ] Tabela com `.style.background_gradient()`

4. **Cell Violin Plots (se houver):**
   - [ ] `px.violin()` com cores Viridis

5. **Cell Comparação Médias:**
   - [ ] `px.bar()` com médias por grupo
   - [ ] `add_hline()` para média global

---

### ✅ Q4_ML_Avancado.ipynb

**Células a modificar:**

1. **Cell Imports:**
   - [ ] Igual Q1 + manter imports SHAP

2. **Cell Matriz de Correlação:**
   - [ ] `px.imshow()` igual Q1

3. **Cell Comparação de Modelos:**
   - [ ] `px.bar()` agrupado com métricas (Accuracy, F1, AUC)
   - [ ] Barras horizontais coloridas

4. **Cell Feature Importance:**
   - [ ] `px.bar()` horizontal

5. **SHAP Plots - MANTER EXATAMENTE COMO ESTÁ!**
   - [ ] ✅ SHAP já usa matplotlib nativo - NÃO MEXER!
   - [ ] Apenas adicionar `@title` nas células

6. **Cell Clustering Elbow:**
   - [ ] `make_subplots()` com Elbow + Silhouette
   - [ ] Usar `go.Scatter()` com linhas e marcadores

7. **Cell Scatter de Clusters:**
   - [ ] `px.scatter()` com `color=cluster_labels`

---

## 🚀 ORDEM DE EXECUÇÃO

### Passo 1: Q1_Regressao_Linear.ipynb (começar aqui)

```bash
# Ativar ambiente
source ~/.local/venvs/data-science/bin/activate

# Editar notebook
# Aplicar TODAS as melhorias acima

# Re-executar
jupyter nbconvert --to notebook --execute Q1_Regressao_Linear.ipynb --output Q1_Regressao_Linear_plotly.ipynb

# Exportar HTML
jupyter nbconvert --to html Q1_Regressao_Linear_plotly.ipynb --output ../exports/Q1_Regressao_Linear_FINAL.html
```

### Passo 2, 3, 4: Repetir para Q2, Q3, Q4

---

## ⚠️ AVISOS IMPORTANTES

### NÃO MEXER:
- ❌ Cálculos de VIF, Durbin-Watson, Breusch-Pagan (manter exatamente como estão)
- ❌ SHAP values (já está perfeito com matplotlib nativo)
- ❌ Lógica dos modelos ML
- ❌ Split train/test, scaling, GridSearchCV

### SEMPRE FAZER:
- ✅ Testar cada célula após modificação
- ✅ Verificar se gráficos renderizam no HTML
- ✅ Manter todo o rigor estatístico
- ✅ Adicionar prints de status (✅ ⚠️)

---

## 📊 RESULTADO ESPERADO

### Antes (matplotlib/seaborn):
- Gráficos estáticos, sem interação
- Sem anotações contextuais
- Visual básico

### Depois (Plotly profissional):
- ✅ Gráficos interativos (zoom, hover)
- ✅ Anotações inteligentes (médias, outliers)
- ✅ Títulos em HTML bold descritivos
- ✅ Cores profissionais (Viridis, RdBu_r, Jet)
- ✅ Template `plotly_white` (fundo branco)
- ✅ Tabelas com gradientes de cor
- ✅ Símbolos visuais nos outputs

**Qualidade Final:** Notebooks no nível de publicação acadêmica + apresentação executiva!

---

## 📦 COMMIT FINAL

```bash
git add prova-aedi-unb/notebooks/Q*_plotly.ipynb
git add prova-aedi-unb/exports/Q*_FINAL.html
git commit -m "feat: aplica melhorias visuais com Plotly em todos notebooks

Transformações aplicadas:
- Substitui matplotlib/seaborn por Plotly interativo
- Adiciona template plotly_white (fundo profissional)
- Implementa gráficos com anotações inteligentes
- Adiciona títulos em HTML bold descritivos
- Aplica tabelas formatadas com gradient
- Usa símbolos visuais (✅ ⚠️ ❌) em outputs
- Adiciona @title em todas células de código

Notebooks melhorados:
✅ Q1: + mapa geográfico scatter_mapbox
✅ Q2: + matriz confusão e ROC Plotly
✅ Q3: + box plots e violin Plotly
✅ Q4: + comparação modelos Plotly (mantém SHAP original)

Visual final: Nível publicação acadêmica + executivo

Referência: material-base/Prova_AEDI_V2.ipynb"

git push origin feature/melhorias-visuais-plotly
```

---

## 🔥💀 CHECKLIST FINAL 💀🔥

Antes de considerar concluído:

- [ ] Q1 executado e HTML gerado sem erros
- [ ] Q2 executado e HTML gerado sem erros
- [ ] Q3 executado e HTML gerado sem erros
- [ ] Q4 executado e HTML gerado sem erros
- [ ] Todos gráficos renderizam corretamente no HTML
- [ ] Interatividade Plotly funciona (hover, zoom)
- [ ] SHAP plots ainda funcionam (Q4)
- [ ] Tabelas com gradiente visíveis
- [ ] Símbolos ✅ ⚠️ aparecem corretamente
- [ ] Commit e push realizados

---

**Data:** 23/11/2025
**Autor:** Nexus Prime / DJ Kabal
**Branch:** feature/melhorias-visuais-plotly
**Status:** 📋 PRONTO PARA EXECUÇÃO

🔥 **SELECT SEM WHERE LIBERTA!** 💀
