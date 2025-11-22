# Guia de Implementação - Prova AEDI Mestrado UnB

## Sumário Executivo

Este documento descreve a implementação completa das 4 questões da Prova Final de Análise Estatística de Dados e Informações (AEDI) do Mestrado em Computação Aplicada (PPCA) da UnB.

**Autor:** Mestrando PPCA/UnB
**Data:** Novembro 2025
**Linguagem:** Python 3.11
**Ambiente:** Jupyter Notebook

---

## 1. Visão Geral do Projeto

### 1.1 Estrutura de Diretórios

```
prova-aedi-unb/
├── dados/                    # Datasets utilizados
│   ├── king_county_houses.csv
│   ├── hotel_bookings.csv
│   ├── online_retail.csv
│   └── german_credit.csv
├── notebooks/                # Jupyter Notebooks com análises
│   ├── Q1_Regressao_Linear.ipynb
│   ├── Q2_Regressao_Logistica.ipynb
│   ├── Q3_ANOVA.ipynb
│   └── Q4_ML_Avancado.ipynb
├── exports/                  # Exportações HTML
│   ├── Q1_Regressao_Linear.html
│   ├── Q2_Regressao_Logistica.html
│   ├── Q3_ANOVA.html
│   └── Q4_ML_Avancado.html
├── models/                   # Modelos treinados
│   └── credit_model.pkl
└── @docs/                    # Documentação técnica
```


### 1.2 Questões e Pontuação

| Questão | Técnica | Dataset | Pontos | Foco Principal |
|---------|---------|---------|--------|----------------|
| Q1 | Regressão Linear | King County Houses | 2.5 | Pressupostos estatísticos |
| Q2 | Regressão Logística | Hotel Bookings | 2.5 | Classificação e features |
| Q3 | ANOVA | Online Retail | 2.0 | Comparação de médias |
| Q4 | ML Avançado + SHAP | German Credit | 3.0 | Interpretabilidade |
| **TOTAL** | | | **10.0** | |

---

## 2. Metodologia de Desenvolvimento

### 2.1 Preparação do Ambiente

**Bibliotecas Essenciais:**
- **Manipulação de dados:** pandas, numpy
- **Visualização:** matplotlib, seaborn
- **Machine Learning:** scikit-learn, xgboost, lightgbm
- **Estatística:** scipy, statsmodels
- **Interpretabilidade:** shap
- **Notebooks:** jupyter

**Instalação:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels xgboost lightgbm shap jupyter openpyxl joblib
```

### 2.2 Aquisição de Dados
Os datasets foram obtidos de repositórios públicos:

King County Houses: Dataset clássico de preços imobiliários
Hotel Bookings: Dados reais de cancelamentos hoteleiros
Online Retail: Transações de varejo online (UCI Repository)
German Credit: Dataset de risco de crédito bancário
Estratégia de Download:

Múltiplas fontes alternativas para redundância
Validação de integridade (shape, tipos de dados)
Fallback para datasets sintéticos quando necessário
3. Implementação por Questão
3.1 Questão 1: Regressão Linear (2.5 pts)
Objetivo: Prever preços de imóveis validando todos os pressupostos estatísticos.

Etapas Implementadas:

EDA Completo (20%)

Estatísticas descritivas (média, mediana, desvio padrão, assimetria, curtose)
Análise de outliers (método IQR)
Correlações entre variáveis
Visualizações: histogramas, boxplots, heatmap, scatterplots
Modelagem Inicial (30%)

Seleção de features baseada em correlação e teoria
Train/test split (80/20) com random_state=42
Treinamento OLS (statsmodels)
Métricas: R², R² ajustado, RMSE, MAE
Validação de Pressupostos (30%) ⚠️ CRÍTICO

a) Linearidade:

Gráfico: Resíduos vs Valores Ajustados
Critério: Padrão aleatório ao redor de zero
b) Homocedasticidade:

Teste de Breusch-Pagan (statsmodels)
H0: variância constante
Decisão: rejeitar H0 se p-value < 0.05
c) Normalidade dos Resíduos:

Q-Q Plot (scipy.stats.probplot)
Teste de Shapiro-Wilk
Histograma com curva normal sobreposta
d) Multicolinearidade:

VIF (Variance Inflation Factor)
Critério: VIF > 10 indica problema sério
Solução: remover features ou aplicar PCA
e) Independência dos Erros:

Teste de Durbin-Watson
Valor ideal: ~2.0
- < 1.5: autocorrelação positiva
- > 2.5: autocorrelação negativa

Ajustes e Correções (30%)

Transformação logarítmica de y se heterocedasticidade detectada
Remoção de features com VIF alto
Feature engineering (idade do imóvel, interações)
Retreinamento e comparação de métricas
Interpretação (10%)

Análise de coeficientes com intervalos de confiança
Impacto prático das features
Limitações do modelo
Recomendações de negócio
Ferramentas Estatísticas Utilizadas:

from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from scipy import stats
3.2 Questão 2: Regressão Logística (2.5 pts)
Objetivo: Prever cancelamentos de reservas hoteleiras.

Etapas Implementadas:

EDA e Balanceamento (10%)

Análise de distribuição do target (is_canceled)
Cálculo de ratio (bad/good)
Se desbalanceamento > 30%: considerar class_weight='balanced'
Preprocessing

Tratamento de missing values
One-Hot Encoding para categóricas
StandardScaler para numéricas (obrigatório para Logística)
Stratified train/test split
Modelagem (60%)

Treinamento com scikit-learn LogisticRegression
Hyperparameter tuning (GridSearchCV com C=[0.01, 0.1, 1, 10])
Métricas: Accuracy, Precision, Recall, F1, AUC-ROC
Matriz de confusão com interpretação de FP e FN
Curva ROC
Análise de Features (20%)

Coeficientes → Odds Ratios (np.exp(coef))
Interpretação: "Para cada aumento de 1 unidade em X, odds multiplicam por exp(β)"
Permutation Importance para validação
Top 10 features mais importantes
Justificativa Metodológica (10%)

Por que Logística e não Linear?
Vantagens: interpretabilidade, output probabilístico
Limitações: assume linearidade no logit
Fórmula Odds Ratio:

OR = exp(β)
Interpretação: Para β=0.8, OR=2.23
Significa: odds aumentam 123% por unidade de X
3.3 Questão 3: ANOVA (2.0 pts)
Objetivo: Comparar médias de vendas entre países.

Etapas Implementadas:

Preparação de Dados (10%)

Seleção dos top 7 países por volume
Limpeza de outliers extremos (opcional, justificado)
Estatísticas descritivas por grupo
Execução da ANOVA (40%)

scipy.stats.f_oneway para Quantity e UnitPrice
H0: μ₁ = μ₂ = ... = μₖ
H1: Pelo menos uma média difere
Decisão baseada em p-value (α=0.05)
Validação de Pressupostos (40%) ⚠️ CRÍTICO

a) Normalidade por Grupo:

Shapiro-Wilk para cada país
Q-Q plots múltiplos
b) Homocedasticidade:

Teste de Levene (robusto)
Teste de Bartlett (sensível a não-normalidade)
c) Independência:

Assumida (cada venda é independente)
Se pressupostos violados:

Opção 1: Transformação log
Opção 2: Kruskal-Wallis (não-paramétrico)
Post-Hoc (Se ANOVA significativa)

Tukey HSD (Honestly Significant Difference)
Comparações par-a-par
Controle de erro Tipo I (family-wise error rate)
Interpretação de Negócio (10%)

Quais países diferem significativamente?
Implicações para estratégia de marketing
Decisões de precificação regionalizada
Código Tukey:

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(data['Quantity'], data['Country'], alpha=0.05)
3.4 Questão 4: ML Avançado + SHAP (3.0 pts)
Objetivo: Prever inadimplência bancária com interpretabilidade máxima.

Distribuição de Pontos:

Discussão contextual: 10% (0.3 pts)
EDA completo: 15% (0.45 pts)
Múltiplos modelos: 30% (0.9 pts)
SHAP Values: 25% (0.75 pts) ⚠️ SUPER CRÍTICO
Clustering: 15% (0.45 pts)
Decisão estratégica: 10% (0.3 pts)
Etapas Implementadas:

Discussão Contextual (0.3 pts)

Contexto bancário brasileiro
Custos assimétricos (FN > FP)
Relevância de ML vs métodos tradicionais
Regulação e transparência
EDA (0.45 pts)

Análise de balanceamento (bad/good)
Análise univariada e bivariada
Feature engineering (debt_to_income, age_group)
Encoding e scaling
Múltiplos Modelos (0.9 pts)

Modelos Treinados:

Logistic Regression (baseline)
Decision Tree
Random Forest
XGBoost
LightGBM
Comparação:

Tabela com todas as métricas
Curvas ROC sobrepostas
Seleção do campeão (maior AUC + Recall)
SHAP Values (0.75 pts) ⚠️ 25% DA NOTA Q4

Gráficos Obrigatórios:

a) Summary Plot (Dot):

Eixo Y: features ordenadas por importância
Eixo X: impacto no modelo (SHAP value)
Cor: valor da feature (vermelho=alto, azul=baixo)
Interpretação textual obrigatória
b) Summary Plot (Bar):

Ranking de importância (mean |SHAP|)
c) Dependence Plots (Top 3):

Mostra relação feature vs SHAP value
Colorido por feature de interação
Identifica não-linearidades
d) Force Plots (2 casos):

Cliente baixo risco (bom pagador)
Cliente alto risco (inadimplente)
Decomposição da predição
e) Interpretação Acadêmica (5 parágrafos):

Template para cada feature:

A variável [NOME] apresenta SHAP value médio absoluto de [X],
classificando-se como a [N]ª mais importante. O sinal [+/-]
indica que aumentar essa feature [aumenta/reduz] o risco.
No contexto bancário, isso alinha-se com a teoria de [TEORIA].
Por exemplo, [EXEMPLO CONCRETO COM NÚMEROS].
Teorias Econômicas Referenciadas:

Teoria de Restrição de Liquidez (Deaton, 1991)
Adverse Selection
Moral Hazard
Time Value of Money
Clustering (0.45 pts)

K-Means:

Elbow Method para escolher K
Silhouette Score
Perfis dos clusters (média, std por feature)
Visualização PCA
DBSCAN:

Tuning de eps e min_samples
Detecção de outliers
Análise de taxa de inadimplência em outliers
Comparação:

K-Means: força todos em clusters, bom para segmentação
DBSCAN: detecta outliers, bom para anomalias
Integração:

Testar cluster_id como feature no modelo
Comparar AUC antes/depois
Decisão Estratégica (0.3 pts)

Threshold customizado (0.35 em vez de 0.5)
Segmentação por cluster com políticas diferenciadas
Alertas preventivos baseados em SHAP
Limitações e considerações éticas
Próximos passos (dados longitudinais, A/B testing)
Código SHAP:

import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

shap.summary_plot(shap_values, X_test, feature_names=features)
shap.dependence_plot('feature_name', shap_values, X_test)
shap.force_plot(explainer.expected_value, shap_values[i], X_test[i])

---

## 4. Padrões de Qualidade Adotados

### 4.1 Código

- **Reprodutibilidade:** random_state=42 em TODAS as operações estocásticas
- **Modularidade:** Funções reutilizáveis quando lógica repetida
- **Nomenclatura:** variáveis descritivas (evitar x, y, tmp)
- **Comentários:** Apenas para lógica não-óbvia (< 10% do código)

### 4.2 Visualizações

- **Tamanho:** figsize=(10, 6) como padrão
- **Fontes:** 12pt mínimo para legibilidade
- **Resolução:** dpi=150 para exportações
- **Cores:** Paleta acadêmica (evitar cores berrantes)
- **Labels:** Sempre incluir título, eixos, legendas, unidades

### 4.3 Texto Interpretativo

- **Nível:** Rigor acadêmico de mestrado
- **Estrutura:** Afirmação → Evidência → Interpretação
- **Números:** Sempre incluir valores específicos (não "alto", mas "0.85")
- **Contexto:** Conectar estatística com domínio do problema

**Exemplo Ruim:**
> "O modelo é bom porque R² deu 0.85"

**Exemplo Bom:**
> "O modelo apresenta R² de 0.85, indicando que 85% da variância de price é explicada pelas features. Entretanto, a análise de resíduos revela heterocedasticidade (Breusch-Pagan p<0.01), sugerindo que transformação logarítmica da variável target pode ser necessária para atender aos pressupostos da regressão linear clássica."

---

## 5. Exportação e Entrega

### 5.1 Conversão para HTML

```bash
jupyter nbconvert --to html notebooks/Q1_Regressao_Linear.ipynb --output-dir exports/
jupyter nbconvert --to html notebooks/Q2_Regressao_Logistica.ipynb --output-dir exports/
jupyter nbconvert --to html notebooks/Q3_ANOVA.ipynb --output-dir exports/
jupyter nbconvert --to html notebooks/Q4_ML_Avancado.ipynb --output-dir exports/
```

### 5.2 Validação Pré-Entrega

**Checklist:**

- ✅ Todos os 4 notebooks executam sem erros
- ✅ Todos os gráficos renderizaram corretamente
- ✅ Pressupostos foram validados (Q1, Q3)
- ✅ SHAP tem interpretação textual completa (Q4)
- ✅ HTMLs exportados estão legíveis
- ✅ Código está comentado minimamente
- ✅ Interpretações conectam estatística com contexto

---

## 6. Respostas para Tutores

### 6.1 "Por que transformação logarítmica?"

**Resposta:** A transformação log(y) é aplicada quando:

- A variável target tem distribuição assimétrica (skewness > 1)
- Heterocedasticidade detectada (Breusch-Pagan p<0.05)
- Relação exponencial entre X e y (comum em preços)

**Efeito:**

- Lineariza crescimentos exponenciais
- Estabiliza variância dos resíduos
- Interpretação muda: coeficientes viram elasticidades

**Reversão:** Predições precisam ser revertidas: `y_pred_original = np.expm1(y_pred_log)`

### 6.2 "Por que VIF > 10 é problema?"

**Resposta:** VIF (Variance Inflation Factor) mede multicolinearidade:

```
VIF = 1 / (1 - R²ⱼ)
```

Onde R²ⱼ é o R² de Xⱼ regredido nas demais features.

**VIF=10 significa:**

- R²=0.9 → feature j é 90% explicada pelas outras
- Coeficientes ficam instáveis (pequenas mudanças nos dados → grandes mudanças nos β)
- Interpretação fica prejudicada (difícil isolar efeito individual)

**Solução:**

- Remover features redundantes
- Combinar features correlacionadas
- Aplicar PCA

### 6.3 "Por que SHAP e não feature importance padrão?"

**Resposta:** Feature importance do Random Forest/XGBoost tem limitações:

**Problemas:**

- Bias para features categóricas com muitas categorias
- Não indica direção do efeito (+/-)
- Não mostra interações
- Valores globais (não explica predições individuais)

**SHAP vantagens:**

- Baseado em Teoria dos Jogos (valores de Shapley)
- Satisfaz propriedades desejáveis (eficiência, simetria, dummy)
- Decomposição aditiva: base_value + Σ(SHAP) = predição
- Permite explicações locais (força plots)
- Aprovado por reguladores bancários (transparência)

### 6.4 "Kruskal-Wallis vs ANOVA?"

**Resposta:**

**ANOVA (paramétrico):**

- Assume normalidade + homocedasticidade
- Testa médias
- Mais poderoso SE pressupostos atendidos
- F-statistic

**Kruskal-Wallis (não-paramétrico):**

- Não assume distribuição
- Testa medianas (tecnicamente, distribuições)
- Mais robusto a outliers
- Baseado em ranks
- H-statistic (qui-quadrado)

**Decisão:** Se Shapiro-Wilk p<0.05 em múltiplos grupos → Kruskal-Wallis

---

## 7. Referências Técnicas

### 7.1 Testes Estatísticos

| Teste | Hipótese H0 | Quando Usar | Função Python |
|-------|-------------|-------------|--------------|
| Shapiro-Wilk | Dados são normais | Normalidade (n<5000) | `scipy.stats.shapiro` |
| Kolmogorov-Smirnov | Dados são normais | Normalidade (n>5000) | `scipy.stats.kstest` |
| Breusch-Pagan | Homocedasticidade | Regressão linear | `statsmodels.stats.diagnostic.het_breuschpagan` |
| Levene | Variâncias iguais | ANOVA | `scipy.stats.levene` |
| Bartlett | Variâncias iguais | ANOVA (se normal) | `scipy.stats.bartlett` |
| Durbin-Watson | Não há autocorrelação | Regressão | `statsmodels.stats.stattools.durbin_watson` |

### 7.2 Métricas de Classificação

| Métrica | Fórmula | Interpretação |
|---------|---------|---------------|
| Accuracy | (TP+TN)/(TP+TN+FP+FN) | % acertos totais |
| Precision | TP/(TP+FP) | % acertos dentre os preditos como positivos |
| Recall | TP/(TP+FN) | % positivos reais que foram capturados |
| F1-Score | 2×(Prec×Rec)/(Prec+Rec) | Média harmônica Prec/Rec |
| AUC-ROC | Área sob curva ROC | Capacidade discriminatória global |

---

## 8. Tempo de Execução Estimado

| Questão | EDA | Modelagem | Validação | Ajustes | Interpretação | Total |
|---------|-----|-----------|-----------|---------|---------------|-------|
| Q1 | 15min | 10min | 20min | 15min | 10min | 70min |
| Q2 | 10min | 15min | 10min | 5min | 10min | 50min |
| Q3 | 10min | 10min | 20min | 10min | 10min | 60min |
| Q4 | 20min | 30min | 40min | 20min | 20min | 130min |
| **TOTAL** | | | | | | **~5h** |

**Nota:** Tempo para execução manual. Inclui pensamento, depuração e refinamento.

---

## 9. Conclusão

Este guia documenta uma implementação completa e rigorosa das 4 questões da Prova AEDI, seguindo as melhores práticas acadêmicas e profissionais de Ciência de Dados.

**Diferenciais:**

- Validação exaustiva de pressupostos estatísticos
- Interpretação contextual em todas as análises
- SHAP values com fundamentação teórica
- Reprodutibilidade garantida (seeds fixas)
- Documentação clara e objetiva

**Resultado Esperado:** 9.5-10.0 pontos (com execução cuidadosa)

---

**Última Atualização:** Novembro 2025


---

