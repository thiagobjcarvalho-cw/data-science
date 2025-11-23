# 🎯 VERSÃO 2: NOTEBOOKS PLOTLY (Melhorados) - VISUALIZAÇÕES INTERATIVAS

## 📝 QUESTÃO 1: REGRESSÃO LINEAR (2.5 pontos)

### Critério 1: Análise Descritiva dos Dados (20% = 0.5 pts)

**Comparação com Versão Original:**

#### MELHORIAS IMPLEMENTADAS:

**⭐ Histograma interativo (Plotly):**

- Hover mostra valores exatos
- Linha de média com anotação automática
- Anotação de outliers (threshold Q3 + 1.5×IQR) ← NOVO!

**⭐ Q-Q Plot interativo (Plotly):**

- `go.Scatter` com linha teórica
- Interatividade para zoom

**⭐ Matriz de correlação (px.imshow):**

- Valores automáticos com `text_auto='.2f'`
- Escala RdBu_r (Red-Blue reversed) - acadêmica
- Hover mostra correlação exata

**⭐ Scatter plots em subplots:**

- 2x2 grid com correlações nos títulos
- Interatividade completa

**⭐⭐⭐ GEO-SPATIAL ANALYSIS (NOVIDADE):**

- `px.scatter_mapbox` com lat/long
- Color por preço (Jet colorscale - hot colors para caros)
- Size por sqft_living
- Hover_data: price, sqft_living, grade, bedrooms, bathrooms
- Mapbox style: carto-positron (limpo e profissional)

**INOVAÇÃO:** Visualização geográfica da concentração de valor!

#### PROBLEMAS CORRIGIDOS:

- ✅ Visualizações agora são INTERATIVAS
- ✅ Análise geográfica PRESENTE
- ✅ Anotações contextuais (média, outliers)

**NOTA DESTE CRITÉRIO:** 0.5/0.5 (+0.05 recuperado - NOTA MÁXIMA)

---

### Critério 2: Construção do Modelo (30% = 0.75 pts)

IGUAL à versão original - Modelo OLS correto, métricas completas

**NOTA DESTE CRITÉRIO:** 0.75/0.75

---

### Critério 3: Interpretação dos Resultados (10% = 0.25 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Diagnóstico de resíduos (make_subplots):**

- Histograma + Q-Q Plot lado a lado
- Interativo com Plotly

**⭐ Teste de Breusch-Pagan:** Mantido (correto)

**⭐ VIF com gradient highlighting:**

- `display()` com `.style.background_gradient(cmap='Reds')`
- Visual impact maior para VIFs altos

**NOTA DESTE CRITÉRIO:** 0.25/0.25

---

### Critério 4: Ajustes no Modelo (30% = 0.75 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Comparação de modelos com gradient:**

- DataFrame com `.style.background_gradient(cmap='Blues')`
- Formatação diferenciada: R² com 4 decimais, RMSE com currency

**NOTA DESTE CRITÉRIO:** 0.75/0.75

---

### Critério 5: Tomada de Decisão (10% = 0.25 pts)

**⚠️ AINDA FALTA:**

- Decisões estratégicas AINDA pouco detalhadas
- Sem exemplos práticos de precificação

**NOTA DESTE CRITÉRIO:** 0.18/0.25 (mesmo problema da versão original)

**NOTA FINAL Q1 (PLOTLY):** 2.43/2.5 ✅ (97.2%)  
**MELHORIA:** +0.05 pontos (+2% vs versão original)

---

## 📝 QUESTÃO 2: REGRESSÃO LOGÍSTICA (2.5 pontos)

### Critério a) Análise Descritiva (10% = 0.25 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Gráfico de barras interativo (px.bar):**

- `color_discrete_sequence=['#2ecc71', '#e74c3c']` (verde/vermelho semântico)
- `text='count'` com percentuais automáticos
- Anotação de balanceamento com interpretação

**NOTA DESTE CRITÉRIO:** 0.25/0.25 (+0.03 recuperado)

---

### Critério b) Modelo de Regressão Logística (60% = 1.5 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Matriz de Confusão (go.Heatmap):**

- Anotações com valores + percentuais
- Colorscale 'Blues'
- Análise textual dos erros (FP vs FN)

**⭐⭐⭐ Curva ROC EXTREMAMENTE MELHORADA:**

- `fill='tozeroy'` com `fillcolor='rgba(255, 165, 0, 0.2)'` (área sob a curva preenchida!)
- Ponto do threshold 0.5 marcado como diamante vermelho
- Interpretação quantitativa: "X% de melhoria sobre aleatório"
- Escala de qualidade (Excelente ≥0.90, Bom ≥0.80, etc.)

**NOTA DESTE CRITÉRIO:** 1.5/1.5

---

### Critério c) Análise das Features (20% = 0.5 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Tabela de OR com gradient:**

- `.style.background_gradient(cmap='RdYlGn')`
- Formatação: `{:+.2f}%` para Percent_Change

**⭐⭐⭐ Visualização de OR MAGISTRAL (px.bar horizontal):**

- `color_continuous_scale='RdYlGn_r'` (Red para OR alto, Green para OR baixo)
- Linha vertical em OR=1 com anotação
- 2 ANOTAÇÕES CONTEXTUAIS:
  - "OR > 1: Aumenta chance de cancelamento" (caixa vermelha com seta)
  - "OR < 1: Reduz chance de cancelamento" (caixa verde com seta)
- `texttemplate='%{text:.2f}'` fora das barras
- Legenda interpretativa completa

**⭐ ESTE É UM EXEMPLO DE EXCELÊNCIA EM VISUALIZAÇÃO ACADÊMICA**

**NOTA DESTE CRITÉRIO:** 0.5/0.5

---

### Critério d) Justificativa do Método (10% = 0.25 pts)

**❌ PROBLEMA AINDA PERSISTE:**

- Justificativa do método AINDA AUSENTE

**NOTA DESTE CRITÉRIO:** 0.0/0.25 (problema não corrigido)

**NOTA FINAL Q2 (PLOTLY):** 2.25/2.5 ✅ (90%)  
**MELHORIA:** +0.03 pontos (+1.2% vs versão original) ⚠️ AINDA FALTA: Justificativa metodológica

---

## 📝 QUESTÃO 3: ANOVA (2.0 pontos)

### Critério a) Análise Descritiva (10% = 0.2 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Tabela formatada com gradient:**

- `.style.background_gradient(cmap='Blues')` para Média/Mediana
- `.style.background_gradient(cmap='Greens')` para Desvio Padrão

**⭐ Box Plot interativo (px.box):**

- `color='Country'` com Set2 palette
- Hover mostra estatísticas automáticas
- `xaxis=dict(tickangle=-45)` para legibilidade

**⭐⭐⭐ Barplot APRIMORADO:**

- `color='Mean'` com Viridis colorscale
- Linha de média global (`add_hline`) com anotação
- `error_y='StdErr'` com barras de erro
- `text_auto='.2f'` com valores nas barras

**NOTA DESTE CRITÉRIO:** 0.2/0.2

---

### Critérios b, c, d) - ANOVA, Pressupostos, Decisão

IGUAL à versão original - Todos os testes formais presentes

**NOTA DESTE CRITÉRIO:** 0.8 + 0.8 + 0.2 = 1.8/1.8

**NOTA FINAL Q3 (PLOTLY):** 2.0/2.0 ⭐ (100%)  
**MELHORIA:** 0 pontos (já era perfeito, melhorias apenas estéticas)

---

## 📝 QUESTÃO 4: ML AVANÇADO + SHAP + CLUSTERING (3.0 pontos)

### Critério a) Discussão (10% = 0.3 pts)

IGUAL à versão original - Contexto acadêmico de alto nível

**NOTA DESTE CRITÉRIO:** 0.3/0.3

---

### Critério b) Análise Descritiva (15% = 0.45 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Target distribution (make_subplots):**

- Bar + Pie lado a lado
- Cores semânticas (green/red)
- `textinfo='label+percent'` no pie

**⭐ Histogramas com linha de média:**

- `add_vline` com anotação automática
- 3 subplots (duration, credit_amount, age)

**NOTA DESTE CRITÉRIO:** 0.45/0.45

---

### Critério c) Múltiplos Modelos (30% = 0.9 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐ Tabela de resultados:**

- `.style.background_gradient(cmap='Blues')`
- Formatação com precision=4

**⭐ Visualização (go.Bar grouped):**

- 5 métricas em barras agrupadas
- `text_auto` mostra valores
- Altura 600px, largura 1200px

**NOTA DESTE CRITÉRIO:** 0.9/0.9 (+0.05 recuperado - justificativa mais clara visualmente)

---

### Critério d) SHAP (25% = 0.75 pts)

**⚠️ VERSÃO PLOTLY MANTÉM MATPLOTLIB PARA SHAP:**

- Summary plots, dependence plots, force plots AINDA usam matplotlib
- **RAZÃO:** Biblioteca SHAP nativa usa matplotlib, não tem suporte Plotly nativo
- **INTERPRETAÇÃO TEXTUAL:** ✅ MANTIDA (5 parágrafos acadêmicos)

**NOTA DESTE CRITÉRIO:** 0.75/0.75 (mantida - não há como melhorar com Plotly)

---

### Critério e) Clustering (15% = 0.45 pts)

#### MELHORIAS IMPLEMENTADAS:

**⭐⭐⭐ Elbow + Silhouette (make_subplots):**

- 2 gráficos lado a lado em Plotly
- `mode='lines+markers'` com interatividade
- Cores distintas (azul/laranja)

**⭐ Perfil de risco:**

- `.style.background_gradient(cmap='RdYlGn_r')`
- Red para bad, Green para good

**NOTA DESTE CRITÉRIO:** 0.45/0.45

---

### Critério f) Decisão Estratégica (10% = 0.3 pts)

IGUAL à versão original - ROI estimado, 4 justificativas, etc.

**NOTA DESTE CRITÉRIO:** 0.3/0.3

**NOTA FINAL Q4 (PLOTLY):** 3.0/3.0 ⭐⭐⭐ (100%)  
**MELHORIA:** 0 pontos (já era perfeito)

---

## 📊 CONSOLIDAÇÃO - VERSÃO PLOTLY (Melhorada)

| Questão | Nota | Total | % | Status |
|---------|------|-------|---|--------|
| Q1 - Regressão Linear | 2.43 | 2.5 | 97.2% | ⭐ Excepcional (+2%) |
| Q2 - Regressão Logística | 2.25 | 2.5 | 90.0% | ✅ Excelente (+1.2%) |
| Q3 - ANOVA | 2.0 | 2.0 | 100% | ⭐ Excepcional (=) |
| Q4 - ML + SHAP + Clustering | 3.0 | 3.0 | 100% | ⭐⭐⭐ Obra-Prima (=) |
| **TOTAL** | **9.68** | **10.0** | **96.8%** | **EXCEPCIONAL** |
