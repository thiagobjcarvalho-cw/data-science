# Glossário Técnico - Prova AEDI

## A

**Accuracy (Acurácia)**
Proporção de predições corretas sobre o total de predições. Fórmula: (VP+VN)/(VP+VN+FP+FN). Métrica básica, mas pode ser enganosa em dados desbalanceados.

**Adverse Selection (Seleção Adversa)**
Fenômeno econômico onde indivíduos com maior risco têm mais incentivo para contratar produtos (ex: seguros, crédito). Relevante em análise de crédito.

**ANOVA (Analysis of Variance)**
Teste estatístico paramétrico que compara médias de 3 ou mais grupos simultaneamente. H0: todas as médias são iguais.

**AUC (Area Under the Curve)**
Área sob a curva ROC. Varia de 0 a 1. Valores >0.8 indicam bom poder discriminatório. Interpretação: probabilidade de um positivo aleatório ter score maior que um negativo aleatório.

---

## B

**Baseline Model**
Modelo simples usado como referência para comparação. Exemplo: Regressão Logística antes de testar modelos complexos como XGBoost.

**Bartlett Test**
Teste de homogeneidade de variâncias (homocedasticidade). Mais poderoso que Levene, mas sensível a desvios de normalidade.

**Breusch-Pagan Test**
Teste de heterocedasticidade em regressão linear. H0: variância dos erros é constante. Se p<0.05, rejeita-se H0 (heterocedasticidade presente).

**Box-Cox Transformation**
Família de transformações de potência para normalizar dados: y^(λ). Caso especial λ=0 é log(y).

---

## C

**Class Imbalance (Desbalanceamento de Classes)**
Quando uma classe é muito mais frequente que outra. Exemplo: 90% não-inadimplentes, 10% inadimplentes. Solução: SMOTE, class_weight='balanced'.

**Confusion Matrix (Matriz de Confusão)**
Tabela 2x2 mostrando VP, VN, FP, FN. Essencial para entender erros de classificação.

**Cross-Validation (Validação Cruzada)**
Técnica de avaliação que divide dados em K partes, treina em K-1 e testa em 1, repetindo K vezes. Reduz viés de uma única divisão train/test.

**Curtosis (Curtose)**
Medida de "peso das caudas" de uma distribuição. Distribuição normal tem curtose=3. >3: caudas pesadas (outliers). <3: caudas leves.

---

## D

**DBSCAN (Density-Based Spatial Clustering)**
Algoritmo de clustering baseado em densidade. Identifica clusters de forma arbitrária e outliers (label=-1). Parâmetros: eps (raio) e min_samples.

**Decision Tree (Árvore de Decisão)**
Modelo de ML que divide dados recursivamente baseado em regras if-then. Interpretável, mas tende a overfitting.

**Durbin-Watson Test**
Teste de autocorrelação em resíduos de regressão. Valor ~2: sem autocorrelação. <1.5: autocorrelação positiva. >2.5: negativa.

---

## E

**EDA (Exploratory Data Analysis)**
Análise exploratória de dados. Fase inicial onde se examina distribuições, correlações, outliers, missing values.

**Elbow Method**
Técnica para escolher K no K-Means. Plotar inércia vs K e identificar "cotovelo" onde curvatura muda abruptamente.

**Ensemble Methods**
Combinação de múltiplos modelos para melhorar predições. Exemplos: Random Forest (bagging), XGBoost (boosting).

---

## F

**F1-Score**
Média harmônica entre Precision e Recall: 2×(P×R)/(P+R). Útil quando classes desbalanceadas. Balança precisão e cobertura.

**False Negative (FN) - Falso Negativo**
Erro Tipo II. Predizer negativo quando é positivo. Em crédito: aprovar inadimplente (CUSTO ALTO).

**False Positive (FP) - Falso Positivo**
Erro Tipo I. Predizer positivo quando é negativo. Em crédito: negar bom pagador (custo de oportunidade).

**Feature Engineering**
Criação de novas variáveis a partir das existentes. Exemplo: idade_imovel = 2025 - ano_construcao.

---

## G

**Gradient Boosting**
Técnica de ensemble que treina modelos sequencialmente, cada um corrigindo erros do anterior. Exemplos: XGBoost, LightGBM.

**GridSearchCV**
Busca exaustiva de hiperparâmetros testando todas as combinações de uma grade pré-definida.

---

## H

**Heterocedasticidade**
Variância não-constante dos resíduos. Viola pressuposto da regressão linear. Solução: transformação log ou Weighted Least Squares.

**Homocedasticidade**
Variância constante dos resíduos (homogênea). Pressuposto fundamental de ANOVA e regressão linear.

**Hyperparameter**
Parâmetro que não é aprendido pelo modelo, mas definido antes do treino. Exemplos: max_depth (árvores), C (regularização logística).

---

## I

**IQR (Interquartile Range)**
Q3 - Q1. Usado para detectar outliers: valores < Q1-1.5×IQR ou > Q3+1.5×IQR são suspeitos.

---

## K

**K-Means**
Algoritmo de clustering particional. Agrupa dados em K clusters minimizando variância intra-cluster. Assume clusters esféricos.

**Kruskal-Wallis Test**
Versão não-paramétrica da ANOVA. Testa se medianas de grupos diferem. Baseado em ranks, não assume normalidade.

**Kurtosis**
Ver "Curtosis".

---

## L

**Levene Test**
Teste robusto de homogeneidade de variâncias. Menos sensível a desvios de normalidade que Bartlett. H0: variâncias iguais.

**LightGBM**
Implementação de Gradient Boosting otimizada para velocidade e memória. Usa leaf-wise tree growth (vs level-wise do XGBoost).

**Logit**
Log-odds: log(p/(1-p)). Transformação usada na regressão logística para linearizar probabilidades.

---

## M

**MAE (Mean Absolute Error)**
Erro absoluto médio: média de |y_real - y_pred|. Em mesma unidade que y. Menos sensível a outliers que RMSE.

**Multicolinearidade**
Correlação alta entre preditores. Infla variância dos coeficientes. Detectada via VIF.

---

## N

**Normalidade**
Distribuição gaussiana (sino). Pressuposto de muitos testes paramétricos. Verificada via Shapiro-Wilk, Kolmogorov-Smirnov, Q-Q plot.

---

## O

**Odds**
Razão entre probabilidade de sucesso e falha: p/(1-p). Exemplo: p=0.75 → odds=3 (3 para 1).

**Odds Ratio (OR)**
Razão entre dois odds. Em regressão logística: OR=exp(β). Interpretação: "odds multiplicam por OR quando X aumenta 1 unidade".

**OLS (Ordinary Least Squares)**
Método dos Mínimos Quadrados Ordinários. Estima coeficientes minimizando soma dos quadrados dos resíduos.

**One-Hot Encoding**
Codificação de variáveis categóricas em múltiplas binárias. Exemplo: cor=[red, blue] → cor_red=[1,0], cor_blue=[0,1].

**Outlier**
Valor extremo que desvia significativamente do padrão. Pode indicar erro de medição ou fenômeno raro legítimo.

**Overfitting**
Modelo aprende ruído dos dados de treino em vez de padrões generalizáveis. Alto R² treino, baixo R² teste.

---

## P

**PCA (Principal Component Analysis)**
Redução de dimensionalidade via transformação linear que captura máxima variância. Componentes principais são ortogonais.

**Precision (Precisão)**
VP/(VP+FP). "Dentre os que previ positivos, quantos acertei?". Alta precisão = poucos falsos alarmes.

**P-value (Valor-p)**
Probabilidade de observar resultado tão ou mais extremo que o observado, assumindo H0 verdadeira. p<0.05: rejeita H0 (significativo a 5%).

---

## Q

**Q-Q Plot (Quantile-Quantile Plot)**
Gráfico para verificar normalidade. Compara quantis da amostra com quantis teóricos da normal. Se pontos seguem linha diagonal, é normal.

---

## R

**R² (Coeficiente de Determinação)**
Proporção de variância de y explicada pelo modelo. Varia 0-1. R²=0.85: modelo explica 85% da variância.

**R² Ajustado**
R² penalizado pelo número de preditores. Previne inflação artificial adicionando features irrelevantes. Fórmula: 1 - (1-R²)×(n-1)/(n-p-1).

**Random Forest**
Ensemble de Decision Trees treinadas em amostras bootstrap com features aleatórias. Reduz overfitting das árvores individuais.

**Random State**
Seed para gerador de números aleatórios. Garante reprodutibilidade. Exemplo: random_state=42.

**Recall (Sensibilidade, Revocação)**
VP/(VP+FN). "Dentre os positivos reais, quantos capturei?". Alto recall = poucos falsos negativos.

**RMSE (Root Mean Squared Error)**
Raiz quadrada do erro quadrático médio: √(Σ(y-ŷ)²/n). Penaliza erros grandes. Mesma unidade que y.

**ROC Curve (Receiver Operating Characteristic)**
Gráfico de TPR vs FPR para diferentes thresholds. Mostra trade-off sensibilidade/especificidade.

---

## S

**Shapiro-Wilk Test**
Teste de normalidade. H0: dados seguem distribuição normal. Recomendado para n<5000. Se p<0.05, rejeita normalidade.

**SHAP (SHapley Additive exPlanations)**
Método de interpretabilidade baseado em valores de Shapley (Teoria dos Jogos). Decomposição aditiva da predição em contribuições de cada feature.

**Silhouette Score**
Métrica de qualidade de clustering. Varia -1 a 1. >0.5: clusters bem separados. <0.2: estrutura fraca.

**Skewness (Assimetria)**
Medida de assimetria da distribuição. =0: simétrica. >0: cauda à direita (maioria valores baixos). <0: cauda à esquerda.

**SMOTE (Synthetic Minority Over-sampling Technique)**
Técnica para balancear classes gerando exemplos sintéticos da classe minoritária interpolando entre vizinhos.

**StandardScaler**
Padronização: z = (x-μ)/σ. Transforma features para média=0, std=1. Obrigatório para modelos baseados em distância (KNN, SVM, Logística).

**Stratified Split**
Divisão train/test preservando proporção de classes. Essencial em classificação desbalanceada.

---

## T

**Test Set (Conjunto de Teste)**
Dados reservados para avaliação final do modelo. Nunca usados no treino. Típico: 20-30% dos dados.

**Train Set (Conjunto de Treino)**
Dados usados para treinar o modelo. Típico: 70-80% dos dados.

**True Negative (TN) - Verdadeiro Negativo**
Predizer negativo e estar correto.

**True Positive (TP) - Verdadeiro Positivo**
Predizer positivo e estar correto.

**Tukey HSD (Honestly Significant Difference)**
Teste post-hoc para ANOVA. Compara todas as combinações de pares de grupos controlando erro Tipo I global.

---

## V

**VIF (Variance Inflation Factor)**
Medida de multicolinearidade: VIF = 1/(1-R²ⱼ). VIF>5: atenção. VIF>10: problema sério. Solução: remover features correlacionadas.

---

## X

**XGBoost (eXtreme Gradient Boosting)**
Implementação otimizada de Gradient Boosting. State-of-the-art em dados tabulares. Features: regularização, paralelização, handling de missing values.

---

## Símbolos e Notações

| Símbolo | Significado |
|---------|-------------|
| α (alfa) | Nível de significância (típico: 0.05 = 5%) |
| β (beta) | Coeficiente de regressão |
| μ (mu) | Média populacional |
| σ (sigma) | Desvio padrão populacional |
| ε (epsilon) | Erro/resíduo |
| Σ (sigma maiúsculo) | Somatório |
| ŷ (y-chapéu) | Valor predito |
| H0 | Hipótese nula |
| H1 | Hipótese alternativa |
| p | Probabilidade / p-value |
| n | Tamanho da amostra |
| k | Número de grupos/clusters |
| df | Graus de liberdade (degrees of freedom) |

---

## Nomenclaturas de Arquivos

**Padrão adotado:**
- `QX_Nome_Tecnica.ipynb` - Notebooks das questões
- `dados/dataset_name.csv` - Datasets em minúsculas com underscore
- `exports/QX_Nome_Tecnica.html` - Exportações HTML
- `models/nome_modelo.pkl` - Modelos salvos com pickle/joblib

**Exemplos:**
- Q1_Regressao_Linear.ipynb
- king_county_houses.csv
- Q4_ML_Avancado.html
- credit_model.pkl

---

## Abreviações Comuns

| Abreviação | Significado Completo |
|------------|----------------------|
| EDA | Exploratory Data Analysis |
| ML | Machine Learning |
| OLS | Ordinary Least Squares |
| VIF | Variance Inflation Factor |
| IQR | Interquartile Range |
| ROC | Receiver Operating Characteristic |
| AUC | Area Under the Curve |
| SHAP | SHapley Additive exPlanations |
| PCA | Principal Component Analysis |
| SMOTE | Synthetic Minority Over-sampling Technique |
| RF | Random Forest |
| DT | Decision Tree |
| LR | Logistic Regression / Linear Regression (contexto) |
| HSD | Honestly Significant Difference |
| VP | Verdadeiro Positivo (True Positive) |
| VN | Verdadeiro Negativo (True Negative) |
| FP | Falso Positivo (False Positive) |
| FN | Falso Negativo (False Negative) |

---

**Última Atualização:** Novembro 2025
