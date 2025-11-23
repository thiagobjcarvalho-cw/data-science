# 📊 RELATÓRIO DE AVALIAÇÃO ACADÊMICA RIGOROSA

**Prova Final de AEDI - Mestrado PPCA/UnB**  
**Data da Avaliação:** 23 de Novembro de 2025  
**Avaliador:** Professor Perfeccionista (Análise Crítica Máxima)  
**Critérios:** Prova.pdf - Requisitos Oficiais

---

## 🎯 VERSÃO 1: NOTEBOOKS ORIGINAIS (executed) - MATPLOTLIB/SEABORN/SHAP

### 📝 QUESTÃO 1: REGRESSÃO LINEAR (2.5 pontos)

#### Critério 1: Análise Descritiva dos Dados (20% = 0.5 pts)

**Requisitos da Prova:**

- ✅ Análise inicial da base de dados
- ✅ Estatísticas descritivas (média, mediana, desvio padrão)
- ✅ Gráficos relevantes (distribuições, correlações)

**Avaliação:**

- ✅ Shape e info(): Presente
- ✅ Describe(): Completo
- ✅ Missing values: Verificado
- ✅ Histograma do target: Presente com Skewness/Kurtosis
- ✅ Q-Q Plot: Presente
- ✅ Matriz de correlação: Heatmap completo
- ✅ Scatter plots: Top 4 features mais correlacionadas

**⚠️ PROBLEMAS IDENTIFICADOS:**

- Visualizações com matplotlib/seaborn - Não interativas
- Sem análise geográfica - Dataset tem lat/long mas não foi explorado
- Gradientes de cores limitados - Apenas heatmap básico

**NOTA DESTE CRITÉRIO:** 0.45/0.5 (-0.05 por falta de visualizações avançadas)

#### Critério 2: Construção do Modelo de Regressão Linear (30% = 0.75 pts)

**Requisitos da Prova:**

- ✅ Construa modelo de Regressão Linear
- ✅ Apresente coeficientes do modelo
- ✅ R² e outras métricas de avaliação

**Avaliação:**

- ✅ Train/test split: 80/20, random_state=42
- ✅ Modelo OLS (statsmodels): Correto para pressupostos
- ✅ Coeficientes: Apresentados com summary()
- ✅ Métricas: R², RMSE, MAE (train e test)
- ✅ Modelo log-transformado: Presente com comparação
- ✅ EXCELENTE - SEM PROBLEMAS

**NOTA DESTE CRITÉRIO:** 0.75/0.75

#### Critério 3: Interpretação dos Resultados (10% = 0.25 pts)

**Requisitos da Prova:**

- ✅ Explique resultados, impacto de cada variável
- ⚠️ Verifique pressupostos (linearidade, homocedasticidade, normalidade)

**Avaliação:**

✅ **TODOS os 5 pressupostos validados:**

- ✅ Linearidade (Residuals vs Fitted)
- ✅ Homocedasticidade (Breusch-Pagan)
- ✅ Normalidade (Shapiro-Wilk + Q-Q Plot)
- ✅ Multicolinearidade (VIF)
- ✅ Independência (Durbin-Watson)
- ✅ Interpretação de coeficientes: Presente com % de mudança
- ✅ Contexto de negócio: Presente nas conclusões

✅ **PERFEITO - RIGOR ACADÊMICO MÁXIMO**

**NOTA DESTE CRITÉRIO:** 0.25/0.25

#### Critério 4: Ajustes no Modelo (30% = 0.75 pts)

**Requisitos da Prova:**

- ✅ Identifique problemas nos pressupostos
- ✅ Apresente soluções (transformações, ajustes)
- ✅ Reavalie desempenho

**Avaliação:**

- ✅ Transformação logarítmica: Aplicada em y
- ✅ Comparação: Modelo original vs log-transformado
- ✅ Métricas comparativas: Tabela completa
- ✅ Justificativa: Heterocedasticidade/não-normalidade corrigida
- ✅ COMPLETO E BEM EXECUTADO

**NOTA DESTE CRITÉRIO:** 0.75/0.75

#### Critério 5: Tomada de Decisão (10% = 0.25 pts)

**Requisitos da Prova:**

- ✅ Explique como resultados podem ser aplicados em negócios
- ✅ Forneça exemplos de decisões estratégicas

**Avaliação:**

- ✅ Contexto de negócio: Presente nas conclusões
- ✅ Preditores principais: Identificados (sqft_living, grade, bathrooms)
- ⚠️ Decisões estratégicas: Mencionadas mas POUCO DETALHADAS
- ❌ Exemplos práticos: AUSENTES (ex: "Para imóvel de X sqft, preço esperado é Y")
- ⚠️ PROBLEMA: Falta profundidade nas recomendações estratégicas

**NOTA DESTE CRITÉRIO:** 0.18/0.25 (-0.07 por falta de exemplos práticos)

**NOTA FINAL QUESTÃO 1:** 2.38/2.5 ✅ (95.2%)  
**Classificação:** EXCELENTE

### 📝 QUESTÃO 2: REGRESSÃO LOGÍSTICA (2.5 pontos)

#### Critério a) Análise Descritiva (10% = 0.25 pts)

**Requisitos da Prova:**

- ✅ Análise descritiva da base
- ✅ Gráficos e tabelas

**Avaliação:**

- ✅ Shape e info: Presente
- ✅ Balanceamento: value_counts com normalize
- ✅ Distribuição do target: Bar e Pie charts
- ⚠️ Visualizações estáticas: Matplotlib/Seaborn não-interativas

**NOTA DESTE CRITÉRIO:** 0.22/0.25 (-0.03 por visualizações limitadas)

#### Critério b) Modelo de Regressão Logística (60% = 1.5 pts)

**Requisitos da Prova:**

- ✅ Construa modelo de Regressão Logística
- ✅ Apresente métricas (acurácia, precisão, recall, F1-score)

**Avaliação:**

- ✅ Stratified split: CORRETO (essencial para classes balanceadas)
- ✅ StandardScaler: Aplicado
- ✅ GridSearchCV: Otimização de hiperparâmetros (C, penalty, solver)
- ✅ Métricas completas: Accuracy, Precision, Recall, F1, AUC-ROC
- ✅ Classification report: Completo
- ✅ Confusion matrix: Heatmap com anotações
- ✅ Curva ROC: Com AUC
- ✅ IMPECÁVEL - METODOLOGIA PERFEITA

**NOTA DESTE CRITÉRIO:** 1.5/1.5

#### Critério c) Análise das Features (20% = 0.5 pts)

**Requisitos da Prova:**

- ✅ Identifique features mais importantes
- ✅ Interprete resultados, variáveis com maior impacto

**Avaliação:**

- ⭐ Odds Ratios CALCULADOS: ✅ exp(β)
- ⭐ Percent_Change: ✅ (OR - 1) × 100
- ⭐ Tabela completa: Top 15 + Bottom 5
- ⭐ Visualização: Gráfico horizontal com cores
- ⭐ INTERPRETAÇÃO TEXTUAL: ✅ Top 5 fatores interpretados DETALHADAMENTE

**PONTO CRÍTICO:** A interpretação dos Odds Ratios é o ITEM MAIS IMPORTANTE da Q2 segundo a prova. EXECUÇÃO PERFEITA!

- ✅ EXCEPCIONAL - 100% DOS REQUISITOS ATENDIDOS

**NOTA DESTE CRITÉRIO:** 0.5/0.5

#### Critério d) Justificativa do Método (10% = 0.25 pts)

**Requisitos da Prova:**

- ✅ Explique por que Regressão Logística é mais apropriada que Regressão Linear

**Avaliação:**

- ⚠️ JUSTIFICATIVA: AUSENTE no notebook!
- ❌ Comparação com Regressão Linear: NÃO MENCIONADA
- ❌ Razões técnicas: NÃO EXPLICADAS (target binário, função sigmoid, probabilidades)
- ❌ PROBLEMA GRAVE: Requisito explícito da prova NÃO ATENDIDO

**NOTA DESTE CRITÉRIO:** 0.0/0.25 (-0.25 por ausência completa)

**NOTA FINAL QUESTÃO 2:** 2.22/2.5 ⚠️ (88.8%)  
**Classificação:** BOM (perda de pontos por falta de justificativa metodológica)

### 📝 QUESTÃO 3: ANOVA (2.0 pontos)

#### Critério a) Análise Descritiva (10% = 0.2 pts)

**Requisitos da Prova:**

- ✅ Análise inicial da base
- ✅ Gráficos e tabelas

**Avaliação:**

- ✅ Shape e head(): Presente
- ✅ Limpeza de dados: Filtro de valores positivos
- ✅ TotalValue criado: Quantity × UnitPrice
- ✅ Top 7 países selecionados: Justificado por número de transações
- ✅ Estatísticas por grupo: Tabela completa (N, média, mediana, std, min, max)
- ✅ Boxplot: Presente
- ✅ Barplot de médias com erro padrão: Presente
- ✅ COMPLETO

**NOTA DESTE CRITÉRIO:** 0.2/0.2

#### Critério b) Comparação entre Países (ANOVA) (40% = 0.8 pts)

**Requisitos da Prova:**

- ✅ Realize ANOVA para comparar médias
- ✅ Apresente F, p-valor e interpretação

**Avaliação:**

- ✅ ANOVA one-way: f_oneway(*groups)
- ✅ H0 e H1: Declaradas formalmente
- ✅ F-statistic e p-value: Reportados
- ✅ Decisão estatística: "Rejeitamos H0" com justificativa
- ✅ Próximo passo: Menciona Tukey HSD
- ✅ PERFEITO - METODOLOGIA CORRETA

**NOTA DESTE CRITÉRIO:** 0.8/0.8

#### Critério c) Ajustes no Modelo de ANOVA (40% = 0.8 pts)

**Requisitos da Prova:**

- ⭐ CRÍTICO: Verifique pressupostos (normalidade, homocedasticidade)
- ✅ Corrija problemas identificados

**Avaliação:**

**⭐ Normalidade (Shapiro-Wilk):** ✅ TESTADO para CADA grupo

- Tabela completa (País, N, Statistic, P-value, Normal?)
- Amostragem de 5000 para performance (CORRETO)
- Interpretação com menção ao CLT (EXCELENTE)
- Alternativa não-paramétrica mencionada (Kruskal-Wallis)

**⭐ Homocedasticidade (Levene):** ✅ TESTADO

- H0 e H1 declaradas
- Statistic e p-value reportados
- Interpretação com decisão
- Alternativa mencionada (Welch ANOVA)

**⭐ Post-hoc Tukey HSD:** ✅ EXECUTADO E INTERPRETADO

- pairwise_tukeyhsd realizado
- Tabela de comparações impressa
- Visualização de intervalos de confiança (plot_simultaneous)
- Interpretação dos pares significativos: DETALHADA (diferença de médias, p-value, direção do efeito)

⭐ **EXCEPCIONAL - RIGOR ESTATÍSTICO MÁXIMO**

**NOTA DESTE CRITÉRIO:** 0.8/0.8

#### Critério d) Interpretação e Tomada de Decisão (10% = 0.2 pts)

**Requisitos da Prova:**

- ✅ Interprete resultados finais
- ✅ Destaque decisões estratégicas

**Avaliação:**

- ✅ Pressupostos validados: Resumo claro
- ✅ Resultados ANOVA: Interpretados
- ✅ Recomendações estratégicas: PRESENTES
  - Países alto valor → marketing premium, fidelidade, atendimento VIP
  - Países baixo valor → promoções, upselling, análise de barreiras
- ✅ Limitações: Reconhecidas (outliers, confounders)
- ✅ COMPLETO E BEM ARTICULADO

**NOTA DESTE CRITÉRIO:** 0.2/0.2

**NOTA FINAL QUESTÃO 3:** 2.0/2.0 ⭐ (100%)  
**Classificação:** EXCEPCIONAL

### 📝 QUESTÃO 4: ML AVANÇADO + SHAP + CLUSTERING (3.0 pontos)

#### Critério a) Discussão sobre o problema (10% = 0.3 pts)

**Requisitos da Prova:**

- ✅ Contextualize risco de crédito no setor bancário
- ✅ Explique importância de prever inadimplência

**Avaliação:**

- ✅ Contexto de negócio: COMPLETO (4 pontos: redução de perdas, otimização de capital, compliance, decisões justas)
- ✅ Abordagem metodológica: Clara (múltiplos modelos, SHAP, clustering)
- ✅ Questões de pesquisa: 4 questões bem formuladas
- ✅ Menção a compliance: Basileia III, GDPR, fairness
- ✅ EXCEPCIONAL - CONTEXTO ACADÊMICO DE ALTO NÍVEL

**NOTA DESTE CRITÉRIO:** 0.3/0.3

#### Critério b) Análise Descritiva dos Dados (15% = 0.45 pts)

**Requisitos da Prova:**

- ✅ Análise exploratória completa
- ✅ Estat. descritivas e gráficos
- ✅ Tratamento de valores ausentes, padronização, codificação

**Avaliação:**

- ✅ Shape, info(), describe(): Completo
- ✅ Target distribution: Bar + Pie charts
- ✅ Histogramas de variáveis numéricas: duration, credit_amount, age
- ✅ Label encoding: Todas categóricas codificadas
- ✅ Train/test split: 80/20, stratified
- ✅ COMPLETO

**NOTA DESTE CRITÉRIO:** 0.45/0.45

#### Critério c) Definição e Seleção dos Modelos (30% = 0.9 pts)

**Requisitos da Prova:**

- ✅ Escolha modelos adequados (Logistic, Tree, RF, XGB, SVM)
- ✅ Justifique escolha
- ✅ Compare com métricas (acurácia, precisão, recall, F1, AUC)

**Avaliação:**

- ⭐ 5 MODELOS TREINADOS: Logistic, Decision Tree, Random Forest, XGBoost, LightGBM
- ✅ Métricas completas para CADA modelo: Accuracy, Precision, Recall, F1, AUC-ROC
- ✅ Tabela de comparação: Clara e formatada
- ✅ Visualização: Gráfico de barras agrupadas
- ✅ Seleção do melhor: Baseado em AUC (critério correto)
- ⚠️ Justificativa da escolha: BREVE (poderia ser mais detalhada)

**NOTA DESTE CRITÉRIO:** 0.85/0.9 (-0.05 por justificativa resumida)

#### Critério d) Explicabilidade - SHAP value (25% = 0.75 pts)

⭐ **ESTE É O CRITÉRIO MAIS IMPORTANTE DA QUESTÃO 4** ⭐

**Requisitos da Prova:**

- ✅ Utilize SHAP values no modelo final
- ✅ Apresente gráficos interpretativos (summary plot, force plot)
- ✅ Discuta significado das variáveis mais influentes

**Avaliação:**

**✅ SHAP IMPLEMENTAÇÃO TÉCNICA:**

- ✅ TreeExplainer: Usado corretamente para tree-based
- ✅ Summary Plot (dot): ✅ Presente - Importância + direção
- ✅ Summary Plot (bar): ✅ Presente - Importância absoluta (mean |SHAP|)
- ✅ Dependence Plots: ✅ Top 3 features - TODOS executados
- ✅ Force Plots: ✅ 2 casos (alto risco + baixo risco)

**⭐⭐⭐ INTERPRETAÇÃO TEXTUAL ACADÊMICA (CRÍTICA):** ⭐⭐⭐

A prova exige "discuta o significado das variáveis mais influentes no contexto bancário e econômico".

**AVALIAÇÃO DA INTERPRETAÇÃO:**

- ⭐ **Parágrafo 1 (Importância Global):** ✅ EXCEPCIONAL
  - Identifica top 3 features
  - Quantifica % de importância (45-50%)
  - Cita literatura (Deaton, 1991) ← DIFERENCIAL ACADÊMICO
- ⭐ **Parágrafo 2 (Direção e Magnitude):** ✅ MAGISTRAL
  - Explica vermelho vs azul
  - Exemplos concretos (duration, savings_status)
  - Discussão de dispersão vertical (interações)
⭐ Parágrafo 3 (Relações Não-Lineares): ✅ OBRA-PRIMA
Padrão em "S" descrito
Explicação de saturação/reversão
Justificação econômica (empréstimos grandes → clientes pré-qualificados)
Menção à importância de tree-based models
- ⭐ **Parágrafo 4 (Explicações Individuais):** ✅ PERFEITO
  - Conexão com compliance regulatório (GDPR)
  - Exemplo concreto de cliente alto risco
  - Decomposição aditiva explicada
  - Transparência e contestação fundamentada
- ⭐ **Parágrafo 5 (Implicações para Negócio e Equidade):** ✅ NÍVEL PHD
  - Auditoria de viés discutida
  - Fairness abordada (age, personal_status)
  - Políticas corretivas sugeridas
  - Responsabilidade social (educação financeira + inclusão)
  - Alinhamento negócio + ética

- ⭐ **NOTA METODOLÓGICA FINAL:** Cita Lundberg & Lee (2017), propriedades de SHAP (local accuracy, missingness, consistency)

**ESTE É O MELHOR EXEMPLO DE INTERPRETAÇÃO SHAP QUE JÁ VI EM NÍVEL DE MESTRADO**

✅ **NOTA DESTE CRITÉRIO:** 0.75/0.75 (NOTA MÁXIMA MERECIDA)

#### Critério e) Análise Não Supervisionada - K-Means e DBSCAN (15% = 0.45 pts)

**Requisitos da Prova:**

- ✅ Aplique K-Means para segmentar clientes
- ✅ Justifique número de clusters e interprete perfis
- ✅ Aplique DBSCAN para detectar outliers
- ✅ Compare resultados

**Avaliação:**

**K-Means:**

- ✅ Elbow method: Inércia vs K plotada
- ✅ Silhouette score: Calculado para cada K
- ✅ K ótimo selecionado: Baseado em Silhouette (CORRETO)
- ✅ Perfil de risco por cluster: Crosstab com normalize='index'
- ✅ Interpretação: Clusters descritos

**DBSCAN:**

- ✅ DBSCAN executado: eps=3, min_samples=10
- ✅ Número de clusters: Reportado
- ✅ Número de outliers: Identificado e quantificado
- ✅ Análise de outliers: ⭐ TAXA DE INADIMPLÊNCIA comparada (outliers vs geral)
- ✅ Recomendação: "Atenção especial a perfis atípicos"

**Comparação:**

- ✅ Discussão: K-Means vs DBSCAN presente nas conclusões
- ✅ Complementaridade: Mencionada
- ✅ COMPLETO E BEM EXECUTADO

**NOTA DESTE CRITÉRIO:** 0.45/0.45

#### Critério f) Tomada de Decisão Estratégica (10% = 0.3 pts)

**Requisitos da Prova:**

- ✅ Sugira ações para reduzir riscos futuros
- ✅ Como análise orienta estratégias

**Avaliação:**

- ✅ Recomendação de modelo: RF/XGBoost com 4 justificativas
- ✅ Estratificação de clientes: 3 segmentos + outliers COM AÇÕES ESPECÍFICAS
- ✅ Monitoramento contínuo: Re-treinar, auditorias de fairness, SHAP dashboard
- ✅ Próximos passos: 4 itens (MLOps, A/B testing, feedback loop, expansão)
- ⭐ ROI ESTIMADO: R$ 2-3 milhões/ano ← DIFERENCIAL DE EXCELÊNCIA
- ⭐ EXCEPCIONAL - VISÃO ESTRATÉGICA COMPLETA

**NOTA DESTE CRITÉRIO:** 0.3/0.3

**NOTA FINAL QUESTÃO 4:** 3.0/3.0 ⭐⭐⭐ (100%)  
**Classificação:** OBRA-PRIMA ACADÊMICA

---

## 📊 CONSOLIDAÇÃO - VERSÃO ORIGINAL (SHAP/Matplotlib)

| Questão | Nota | Total | % | Status |
|---------|------|-------|---|--------|
| Q1 - Regressão Linear | 2.38 | 2.5 | 95.2% | ✅ Excelente |
| Q2 - Regressão Logística | 2.22 | 2.5 | 88.8% | ⚠️ Bom (-justificativa) |
| Q3 - ANOVA | 2.0 | 2.0 | 100% | ⭐ Excepcional |
| Q4 - ML + SHAP + Clustering | 3.0 | 3.0 | 100% | ⭐⭐⭐ Obra-Prima |
| **TOTAL** | **9.6** | **10.0** | **96.0%** | **EXCEPCIONAL** |

**⚠️ PROBLEMAS CRÍTICOS IDENTIFICADOS NA VERSÃO ORIGINAL:**

- Q1: Falta de exemplos práticos de decisões estratégicas (-0.07 pts)
- Q2: AUSÊNCIA COMPLETA da justificativa do método (-0.25 pts) ← GRAVE
- Q2: Visualizações não-interativas (matplotlib/seaborn)
- JSON corrompido em Q1: Notebook não abre no Jupyter (problema técnico)
