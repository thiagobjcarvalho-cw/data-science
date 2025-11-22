# Metodologia Estatística e Fundamentação Teórica

## Sumário

1. [Fundamentos de Regressão Linear](#1-fundamentos-de-regressão-linear)
2. [Fundamentos de Regressão Logística](#2-fundamentos-de-regressão-logística)
3. [Fundamentos de ANOVA](#3-fundamentos-de-anova)
4. [Fundamentos de Machine Learning](#4-fundamentos-de-machine-learning)
5. [Inferência Estatística e Testes de Hipóteses](#5-inferência-estatística-e-testes-de-hipóteses)
6. [Validação Cruzada e Métricas](#6-validação-cruzada-e-métricas)
7. [Interpretabilidade (SHAP)](#7-interpretabilidade-shap)
8. [Clustering](#8-clustering)

---

## 1. Fundamentos de Regressão Linear

### 1.1 Modelo Teórico

A regressão linear modela a relação entre uma variável dependente Y e uma ou mais variáveis independentes X:

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε
```

Onde:
- **Y**: Variável dependente (resposta)
- **X₁, X₂, ..., Xₚ**: Variáveis independentes (preditoras)
- **β₀**: Intercepto (valor de Y quando todos X = 0)
- **β₁, β₂, ..., βₚ**: Coeficientes de regressão
- **ε**: Erro aleatório (resíduo)

### 1.2 Estimação por Mínimos Quadrados Ordinários (OLS)

Os coeficientes β são estimados minimizando a soma dos quadrados dos resíduos:

```
min Σ(yᵢ - ŷᵢ)²
```

Solução matricial:
```
β̂ = (X'X)⁻¹X'y
```

### 1.3 Pressupostos da Regressão Linear

#### 1.3.1 Linearidade
A relação entre X e Y deve ser linear.

**Teste:** Análise visual de scatter plots e resíduos vs valores preditos.

#### 1.3.2 Homocedasticidade
A variância dos erros deve ser constante.

**Teste:** Breusch-Pagan

```
H₀: Homocedasticidade presente (variância constante)
H₁: Heterocedasticidade presente (variância não constante)
```

Rejeitar H₀ se p-value < 0.05

**Correção:** Transformação logarítmica, Box-Cox, ou usar Weighted Least Squares

#### 1.3.3 Normalidade dos Resíduos
Os resíduos devem seguir distribuição normal.

**Teste:** Shapiro-Wilk

```
H₀: Resíduos seguem distribuição normal
H₁: Resíduos não seguem distribuição normal
```

**Visualização:** Q-Q plot (quantil-quantil)

**Correção:** Transformação de variáveis (log, sqrt, Box-Cox)

#### 1.3.4 Ausência de Multicolinearidade
Variáveis independentes não devem ser altamente correlacionadas.

**Teste:** Variance Inflation Factor (VIF)

```
VIF = 1 / (1 - R²ⱼ)
```

Onde R²ⱼ é o R² da regressão de Xⱼ contra todas as outras variáveis.

**Interpretação:**
- VIF < 5: Multicolinearidade aceitável
- VIF 5-10: Multicolinearidade moderada
- VIF > 10: Multicolinearidade severa (remover variável)

#### 1.3.5 Independência dos Resíduos
Os resíduos não devem ser autocorrelacionados.

**Teste:** Durbin-Watson

```
DW = Σ(eᵢ - eᵢ₋₁)² / Σeᵢ²
```

**Interpretação:**
- DW ≈ 2: Não há autocorrelação
- DW < 2: Autocorrelação positiva
- DW > 2: Autocorrelação negativa

### 1.4 Métricas de Avaliação

#### R² (Coeficiente de Determinação)
```
R² = 1 - (SSres / SStot)
```

Onde:
- SSres = Σ(yᵢ - ŷᵢ)² (soma dos quadrados dos resíduos)
- SStot = Σ(yᵢ - ȳ)² (soma total dos quadrados)

**Interpretação:** Proporção da variância de Y explicada pelo modelo (0 a 1).

#### R² Ajustado
```
R²_adj = 1 - [(1 - R²)(n - 1) / (n - p - 1)]
```

Penaliza modelos com muitas variáveis.

#### RMSE (Root Mean Squared Error)
```
RMSE = √[Σ(yᵢ - ŷᵢ)² / n]
```

#### MAE (Mean Absolute Error)
```
MAE = Σ|yᵢ - ŷᵢ| / n
```

---

## 2. Fundamentos de Regressão Logística

### 2.1 Modelo Teórico

A regressão logística modela a probabilidade de um evento binário:

```
P(Y=1|X) = 1 / (1 + e^-(β₀ + β₁X₁ + ... + βₚXₚ))
```

Função logit (log-odds):
```
logit(p) = log(p / (1-p)) = β₀ + β₁X₁ + ... + βₚXₚ
```

### 2.2 Interpretação: Odds Ratio

**Odds:** Razão entre probabilidade de sucesso e fracasso
```
Odds = P(Y=1) / P(Y=0)
```

**Odds Ratio:** Mudança nas odds quando X aumenta 1 unidade
```
OR = e^β₁
```

**Interpretação:**
- OR = 1: Variável não afeta odds
- OR > 1: Aumento de X aumenta odds de Y=1
- OR < 1: Aumento de X diminui odds de Y=1

**Exemplo:**
- OR = 2.5: Cada unidade de aumento em X multiplica as odds por 2.5
- Equivalente a 150% de aumento nas odds [(2.5-1) × 100%]

### 2.3 Estimação: Maximum Likelihood

Os coeficientes β são estimados maximizando a função de verossimilhança:

```
L(β) = Π P(Y=yᵢ|X)
```

### 2.4 Métricas de Avaliação

#### Matriz de Confusão
```
                 Predito
              Negativo  Positivo
Real Negativo    TN        FP
Real Positivo    FN        TP
```

#### Acurácia
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

#### Precisão
```
Precision = TP / (TP + FP)
```

Proporção de predições positivas que são corretas.

#### Recall (Sensibilidade)
```
Recall = TP / (TP + FN)
```

Proporção de casos positivos reais que foram detectados.

#### F1-Score
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

Média harmônica de precisão e recall.

#### AUC-ROC
Área sob a curva ROC (Receiver Operating Characteristic).

**Interpretação:**
- AUC = 0.5: Modelo aleatório
- AUC = 0.7-0.8: Aceitável
- AUC = 0.8-0.9: Bom
- AUC > 0.9: Excelente

---

## 3. Fundamentos de ANOVA

### 3.1 Modelo Teórico

ANOVA (Analysis of Variance) testa se as médias de múltiplos grupos são iguais:

```
H₀: μ₁ = μ₂ = ... = μₖ
H₁: Pelo menos uma média é diferente
```

### 3.2 Decomposição da Variância

**Variância Total = Variância Entre Grupos + Variância Dentro dos Grupos**

```
SStotal = SSbetween + SSwithin
```

#### SS Between (Soma dos Quadrados Entre Grupos)
```
SSbetween = Σnᵢ(ȳᵢ - ȳ)²
```

#### SS Within (Soma dos Quadrados Dentro dos Grupos)
```
SSwithin = Σ(yᵢⱼ - ȳᵢ)²
```

### 3.3 Estatística F

```
F = (SSbetween / (k-1)) / (SSwithin / (n-k))
```

Onde:
- k: número de grupos
- n: número total de observações

**Interpretação:** Se F é grande, a variância entre grupos é maior que a variância dentro dos grupos, sugerindo diferenças significativas entre médias.

### 3.4 Pressupostos da ANOVA

#### 3.4.1 Normalidade
Cada grupo deve seguir distribuição normal.

**Teste:** Shapiro-Wilk por grupo
```
H₀: Dados do grupo seguem distribuição normal
```

#### 3.4.2 Homogeneidade de Variâncias
As variâncias dos grupos devem ser iguais.

**Teste:** Levene
```
H₀: Variâncias dos grupos são iguais (homocedasticidade)
H₁: Variâncias dos grupos são diferentes
```

**Alternativa:** Se pressupostos violados, usar Kruskal-Wallis (não-paramétrico)

### 3.5 Post-hoc: Tukey HSD

Quando ANOVA é significativa, Tukey HSD identifica quais pares de grupos diferem:

```
HSD = q × √(MSwithin / n)
```

Onde:
- q: valor crítico da distribuição studentized range
- MSwithin: mean square within groups
- n: tamanho da amostra

**Correção:** Ajusta p-values para múltiplas comparações (controle FWER - Family-Wise Error Rate).

---

## 4. Fundamentos de Machine Learning

### 4.1 Decision Trees (Árvores de Decisão)

#### Algoritmo
1. Selecionar feature que melhor separa os dados (max information gain ou min Gini)
2. Particionar dados com base nessa feature
3. Repetir recursivamente até critério de parada

#### Gini Impurity
```
Gini = 1 - Σpᵢ²
```

Onde pᵢ é a proporção de classe i no nó.

**Interpretação:**
- Gini = 0: Nó puro (todas observações da mesma classe)
- Gini = 0.5: Máxima impureza (classes balanceadas)

#### Vantagens
- Interpretável
- Não requer normalização
- Captura não-linearidades

#### Desvantagens
- Propenso a overfitting
- Instável (pequenas mudanças nos dados alteram árvore)

### 4.2 Random Forest

#### Conceito
Ensemble de múltiplas árvores de decisão treinadas em subsets aleatórios dos dados (bagging).

**Predição final:**
- Classificação: Voto majoritário
- Regressão: Média das predições

#### Hiperparâmetros Principais
- `n_estimators`: Número de árvores
- `max_depth`: Profundidade máxima de cada árvore
- `min_samples_split`: Mínimo de amostras para split
- `max_features`: Número de features consideradas em cada split

#### Vantagens
- Reduz overfitting vs árvores individuais
- Boa performance out-of-the-box
- Fornece feature importance

### 4.3 Gradient Boosting (XGBoost, LightGBM)

#### Conceito
Ensemble sequencial: cada árvore corrige os erros da anterior.

```
F_m(x) = F_{m-1}(x) + η × h_m(x)
```

Onde:
- F_m: modelo após m iterações
- η: learning rate
- h_m: nova árvore treinada nos resíduos

#### XGBoost
Implementação otimizada com regularização:

```
Obj = Σ L(yᵢ, ŷᵢ) + Σ Ω(fₖ)
```

Onde:
- L: Função de perda
- Ω: Termo de regularização (penaliza complexidade)

#### LightGBM
Variante que cresce árvores leaf-wise (vs level-wise) para maior eficiência.

#### Vantagens
- Estado da arte em muitos datasets tabulares
- Handles missing values
- Feature importance nativa

---

## 5. Inferência Estatística e Testes de Hipóteses

### 5.1 Framework de Testes de Hipóteses

1. **Definir hipóteses:**
   - H₀: Hipótese nula (status quo)
   - H₁: Hipótese alternativa

2. **Escolher nível de significância:**
   - α = 0.05 (padrão)
   - α = 0.01 (mais rigoroso)

3. **Calcular estatística de teste**

4. **Calcular p-value**

5. **Decisão:**
   - Se p-value < α: Rejeitar H₀
   - Se p-value ≥ α: Não rejeitar H₀

### 5.2 Interpretação de P-value

**P-value:** Probabilidade de observar um resultado tão extremo quanto o obtido, assumindo que H₀ é verdadeira.

**NÃO é:** Probabilidade de H₀ ser verdadeira.

**Exemplo:**
- p = 0.03: Se H₀ fosse verdadeira, teríamos 3% de chance de observar esses dados
- Conclusão: Evidência contra H₀

### 5.3 Erros Tipo I e II

| | H₀ Verdadeira | H₀ Falsa |
|-------------|---------------|----------|
| Rejeitar H₀ | Erro Tipo I (α) | Correto (1-β) |
| Não Rejeitar | Correto (1-α) | Erro Tipo II (β) |

- **Erro Tipo I:** Falso positivo (rejeitar H₀ quando é verdadeira)
- **Erro Tipo II:** Falso negativo (não rejeitar H₀ quando é falsa)

---

## 6. Validação Cruzada e Métricas

### 6.1 Train-Test Split

Divisão simples dos dados:
- **Train set:** 70-80% (treinar modelo)
- **Test set:** 20-30% (avaliar performance)

**Importante:** Usar `stratify=y` em classificação para manter proporção de classes.

### 6.2 K-Fold Cross-Validation

1. Dividir dados em K folds
2. Para cada fold:
   - Treinar em K-1 folds
   - Validar em 1 fold
3. Média das K métricas

**Vantagem:** Uso mais eficiente dos dados, estimativa mais robusta.

### 6.3 GridSearchCV

Busca exaustiva de hiperparâmetros com cross-validation:

```python
grid = {'param1': [val1, val2], 'param2': [val3, val4]}
GridSearchCV(model, grid, cv=5)
```

Testa todas combinações e retorna a melhor.

---

## 7. Interpretabilidade (SHAP)

### 7.1 Fundamento Teórico: Valores de Shapley

SHAP (SHapley Additive exPlanations) é baseado na teoria dos jogos cooperativos.

**Valor de Shapley:** Contribuição marginal média de uma feature considerando todas as possíveis coalizões.

```
φᵢ = Σ [|S|!(|F|-|S|-1)! / |F|!] × [f(S ∪ {i}) - f(S)]
```

Onde:
- φᵢ: SHAP value para feature i
- S: Subset de features
- F: Conjunto completo de features
- f: Função de predição do modelo

### 7.2 Propriedades Desejáveis

1. **Local accuracy:** Soma dos SHAP values = predição - baseline
2. **Missingness:** Feature ausente tem SHAP value = 0
3. **Consistency:** Se modelo muda e feature fica mais importante, SHAP value aumenta

### 7.3 Tipos de Plots SHAP

#### Summary Plot (Dot)
- Eixo Y: Features (ordenadas por importância)
- Eixo X: SHAP value (impacto na predição)
- Cor: Valor da feature (azul = baixo, vermelho = alto)

**Interpretação:**
- Dispersão horizontal → Impacto variável
- Vermelho à direita → Valores altos aumentam predição
- Azul à esquerda → Valores baixos diminuem predição

#### Summary Plot (Bar)
- Importância média absoluta de cada feature

#### Dependence Plot
- Mostra relação entre valor da feature e seu SHAP value
- Revela padrões não-lineares

#### Force Plot
- Explicação individual (uma observação)
- Mostra contribuição de cada feature para a predição

---

## 8. Clustering

### 8.1 K-Means

#### Algoritmo
1. Inicializar K centroides aleatoriamente
2. Atribuir cada ponto ao centroide mais próximo
3. Recalcular centroides (média dos pontos)
4. Repetir 2-3 até convergência

#### Função Objetivo (Inércia)
```
Σ min(||xᵢ - μₖ||²)
```

Minimiza distância intra-cluster.

#### Elbow Method
Plotar inércia vs número de clusters K.

**"Cotovelo":** Ponto onde aumento de K não reduz muito inércia.

#### Hiperparâmetros
- `n_clusters`: Número de clusters (escolher via elbow)
- `n_init`: Número de inicializações (padrão: 10)
- `random_state`: Seed para reprodutibilidade

### 8.2 DBSCAN

#### Conceito
Density-Based Spatial Clustering of Applications with Noise

**Vantagens:**
- Não requer especificar número de clusters
- Detecta outliers automaticamente
- Clusters de formas arbitrárias

#### Parâmetros
- `eps`: Raio de vizinhança
- `min_samples`: Mínimo de pontos para formar cluster

#### Tipos de Pontos
1. **Core point:** Tem ≥ min_samples pontos em raio eps
2. **Border point:** Está em vizinhança de core point
3. **Noise point:** Não é core nem border (outlier)

---

## 9. Boas Práticas Metodológicas

### 9.1 Reprodutibilidade
- Fixar seeds: `random_state=42`
- Versionar código e dados
- Documentar ambiente (bibliotecas, versões)

### 9.2 Validação de Pressupostos
- **SEMPRE** validar pressupostos antes de interpretar resultados
- Documentar testes realizados
- Aplicar correções quando pressupostos violados

### 9.3 Interpretação
- Conectar estatística com contexto de negócio
- Incluir valores numéricos específicos
- Considerar significância estatística E prática

### 9.4 Transparência
- Documentar limitações
- Reportar todas as métricas relevantes
- Não cherry-pick resultados

---

## 10. Referências Bibliográficas

### Livros Fundamentais
1. James, G. et al. (2021). *An Introduction to Statistical Learning*. Springer.
2. Hastie, T. et al. (2009). *The Elements of Statistical Learning*. Springer.
3. Montgomery, D. C. (2012). *Design and Analysis of Experiments*. Wiley.
4. Agresti, A. (2018). *An Introduction to Categorical Data Analysis*. Wiley.

### Artigos Seminais
5. Shapley, L. S. (1953). *A value for n-person games*. Contributions to the Theory of Games.
6. Lundberg, S. M. & Lee, S. I. (2017). *A unified approach to interpreting model predictions*. NIPS.
7. Breiman, L. (2001). *Random Forests*. Machine Learning, 45(1), 5-32.
8. Chen, T. & Guestrin, C. (2016). *XGBoost: A Scalable Tree Boosting System*. KDD.

### Documentação Técnica
9. scikit-learn documentation: https://scikit-learn.org
10. statsmodels documentation: https://www.statsmodels.org
11. SHAP documentation: https://github.com/slundberg/shap

---

**Nota Final:** Esta fundamentação teórica serve como base para as implementações práticas nos notebooks. Qualquer decisão metodológica foi tomada com rigor acadêmico e seguindo as melhores práticas da literatura estatística e de machine learning.

**Versão:** 1.0
**Data:** Novembro 2025
