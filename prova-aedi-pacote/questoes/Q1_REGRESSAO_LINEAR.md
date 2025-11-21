# QUESTÃO 1: REGRESSÃO LINEAR (2,5 pontos)

## 📊 DATASET
**Nome:** King County House Sales  
**Descrição:** Preços de imóveis vendidos em King County, Washington (EUA)  
**Variável Target:** price (preço de venda)  
**Features principais:** sqft_living, bedrooms, bathrooms, grade, waterfront, view, lat, long, yr_built

---

## 🎯 OBJETIVO
Construir modelo de Regressão Linear para prever preços de imóveis, validando TODOS os pressupostos estatísticos e aplicando correções necessárias.

---

## 📋 ETAPAS OBRIGATÓRIAS

### 1. ANÁLISE DESCRITIVA (20% da nota)

**Ações:**
- Carregar dataset
- Apresentar: shape, info(), describe()
- Missing values: count absoluto e percentual por coluna
- Estatísticas avançadas:
  * Média, mediana, desvio padrão
  * Assimetria (skewness)
  * Curtose (kurtosis)

**Gráficos obrigatórios:**
1. Grid 3x3 de histogramas das features numéricas principais
2. Boxplots: price vs sqft_living, price vs grade, price vs bedrooms
3. Heatmap de correlação (valores anotados, cmap='coolwarm')
4. Scatterplot: price vs latitude/longitude (identificar padrões geográficos)

**Análise de outliers:**
- Método IQR: Q1 - 1.5*IQR e Q3 + 1.5*IQR
- Identificar features com outliers extremos
- Decidir: remover, transformar ou manter (JUSTIFICAR)

**Texto interpretativo:**
Escrever 2-3 parágrafos respondendo:
- Quais features têm maior correlação com price?
- Há padrões geográficos? (lat/long)
- Distribuição de price é normal ou assimétrica?
- Quais features têm outliers preocupantes?

---

### 2. CONSTRUÇÃO DO MODELO INICIAL (30% da nota)

**Preparação:**
```python
# Features
X = df[['sqft_living', 'grade', 'sqft_above', 'sqft_living15', 
        'bathrooms', 'view', 'sqft_basement', 'lat', 'waterfront', 'yr_built']]
y = df['price']

# Train/test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

**Modelagem:**
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

**Métricas obrigatórias:**
- R² (train e test) - para detectar overfitting
- R² ajustado (penaliza número de features)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

**Apresentação de coeficientes:**
Criar tabela:
| Feature | Coeficiente | Interpretação |
|---------|-------------|---------------|
| sqft_living | 280.50 | A cada 1 sqft adicional, preço aumenta $280.50 |
| ... | ... | ... |

**Identificar top 3 features mais importantes** (valor absoluto do coeficiente)

---

### 3. VERIFICAÇÃO DE PRESSUPOSTOS (CRÍTICO - 30% implícito)

⚠️ **Esta é a parte mais importante da Q1!** Não pule nenhum pressuposto.

#### 3.1 LINEARIDADE

**Teste visual:**
```python
residuals = y_test - model.predict(X_test)
fitted = model.predict(X_test)

plt.scatter(fitted, residuals, alpha=0.5)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Valores Ajustados')
plt.ylabel('Resíduos')
plt.title('Linearidade: Resíduos vs Valores Ajustados')
plt.show()
```

**Critério:**
- Se há padrão sistemático (curva, cone): VIOLADO
- Se pontos aleatórios ao redor de zero: OK

**Também plotar:** Resíduos vs cada preditor (top 5 features)

**Interpretação:**
"O gráfico de resíduos vs valores ajustados [mostra/não mostra] padrão sistemático. [Se violado: isso sugere relação não-linear que pode ser corrigida com transformação logarítmica ou polinomial]"

---

#### 3.2 HOMOCEDASTICIDADE (variância constante)

**Teste visual:**
```python
plt.scatter(fitted, np.abs(residuals), alpha=0.5)
plt.xlabel('Valores Ajustados')
plt.ylabel('|Resíduos|')
plt.title('Homocedasticidade')
plt.show()
```

**Teste estatístico - Breusch-Pagan:**
```python
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan

X_with_const = sm.add_constant(X_train)
model_sm = sm.OLS(y_train, X_with_const).fit()
bp_test = het_breuschpagan(model_sm.resid, X_with_const)

print(f"Breusch-Pagan Statistic: {bp_test[0]:.4f}")
print(f"p-value: {bp_test[1]:.4f}")
```

**Critério:**
- H0: variância é constante (homocedasticidade)
- Se p-value < 0.05: REJEITAR H0 = heterocedasticidade detectada

**Interpretação:**
"O teste de Breusch-Pagan resultou em p-value de [valor]. [Se <0.05: Rejeitamos H0, indicando heterocedasticidade. Isso viola o pressuposto e pode ser corrigido com transformação logarítmica de y ou uso de Weighted Least Squares]"

---

#### 3.3 NORMALIDADE DOS RESÍDUOS

**Teste visual - Q-Q Plot:**
```python
from scipy import stats
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot - Normalidade dos Resíduos')
plt.show()
```

**Critério visual:**
- Se pontos seguem linha diagonal: normal
- Se desvios nas caudas: violação

**Histograma com curva normal:**
```python
plt.hist(residuals, bins=50, density=True, alpha=0.7)
mu, sigma = residuals.mean(), residuals.std()
x = np.linspace(residuals.min(), residuals.max(), 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
plt.xlabel('Resíduos')
plt.title('Distribuição dos Resíduos')
plt.show()
```

**Teste estatístico - Shapiro-Wilk:**
```python
if len(residuals) < 5000:
    shapiro_stat, shapiro_p = stats.shapiro(residuals)
else:
    # Para amostras grandes, usar Kolmogorov-Smirnov
    ks_stat, ks_p = stats.kstest(residuals, 'norm')
    
print(f"Shapiro-Wilk p-value: {shapiro_p:.4f}")
```

**Critério:**
- H0: resíduos seguem distribuição normal
- Se p-value < 0.05: REJEITAR H0 = não-normalidade

**Interpretação:**
"O teste de Shapiro-Wilk (p=[valor]) [rejeita/não rejeita] a hipótese de normalidade. [Se rejeitado: Resíduos não-normais podem ser corrigidos com transformação Box-Cox ou log da variável target]"

---

#### 3.4 MULTICOLINEARIDADE

**Teste - VIF (Variance Inflation Factor):**
```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
vif_data = vif_data.sort_values('VIF', ascending=False)
print(vif_data)
```

**Critério:**
- VIF < 5: OK
- VIF 5-10: Atenção, possível problema
- VIF > 10: PROBLEMA SÉRIO

**Interpretação:**
"Features com VIF > 10: [listar]. Multicolinearidade alta indica que essas features são redundantes e podem ser removidas ou combinadas via PCA. Por exemplo, sqft_living e sqft_above são altamente correlacionadas (ambas medem área)."

---

#### 3.5 INDEPENDÊNCIA DOS ERROS

**Teste - Durbin-Watson:**
```python
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(residuals)
print(f"Durbin-Watson: {dw:.4f}")
```

**Critério:**
- Valor ideal: ~2.0
- < 1.5: autocorrelação positiva
- > 2.5: autocorrelação negativa

**Interpretação:**
"O estatístico de Durbin-Watson ([valor]) [está próximo/distante] de 2, [indicando/não indicando] autocorrelação nos resíduos. [Se houver: Isso pode ocorrer em dados de séries temporais; para dados cross-section como este, geralmente não é preocupante]"

---

### 4. AJUSTES NO MODELO (30% da nota)

⚠️ **Baseado nos problemas identificados acima**

#### 4.1 TRANSFORMAÇÕES

**Se resíduos não-normais E/OU heterocedasticidade:**
```python
# Transformação logarítmica
y_log = np.log1p(y)  # log1p = log(1+x) para evitar log(0)

# Retreinar
X_train_adj, X_test_adj, y_train_log, y_test_log = train_test_split(
    X, y_log, test_size=0.2, random_state=42
)
model_log = LinearRegression()
model_log.fit(X_train_adj, y_train_log)

# Predições (voltar para escala original)
y_pred_log = model_log.predict(X_test_adj)
y_pred_original = np.expm1(y_pred_log)  # exp(x) - 1
```

**Se multicolinearidade:**
```python
# Opção 1: Remover features com VIF > 10
X_reduced = X.drop(['sqft_above'], axis=1)  # exemplo

# Opção 2: PCA (se muitas features correlacionadas)
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)  # 95% da variância
X_pca = pca.fit_transform(X)
```

**JUSTIFICAR cada decisão:**
"Aplicamos transformação logarítmica em price porque [razão]. Isso corrigiu a heterocedasticidade (novo Breusch-Pagan p=[valor]) e melhorou a normalidade dos resíduos."

---

#### 4.2 FEATURE ENGINEERING

```python
# Criar features derivadas
df['age'] = 2015 - df['yr_built']  # idade do imóvel
df['price_per_sqft'] = df['price'] / df['sqft_living']
df['has_basement'] = (df['sqft_basement'] > 0).astype(int)

# Interações (se teoria/EDA sugerir)
df['sqft_grade_interaction'] = df['sqft_living'] * df['grade']
```

**Justificar:**
"Criamos 'age' porque imóveis mais antigos tendem a valer menos (depreciação). 'price_per_sqft' normaliza preço pela área, útil para comparações."

---

#### 4.3 RETREINAR E COMPARAR

**Tabela comparativa obrigatória:**

| Métrica | Modelo Original | Modelo Ajustado | Melhoria |
|---------|-----------------|-----------------|----------|
| R² (test) | 0.75 | 0.83 | +10.7% |
| RMSE | 125,000 | 98,000 | -21.6% |
| MAE | 87,000 | 72,000 | -17.2% |
| Breusch-Pagan p | 0.001 | 0.12 | ✓ Corrigido |
| Shapiro-Wilk p | 0.003 | 0.08 | ✓ Corrigido |

**Reverificar pressupostos** (pelo menos plots visuais)

---

### 5. INTERPRETAÇÃO E TOMADA DE DECISÃO (10% da nota)

#### 5.1 Impacto das Features

**Com modelo ajustado:**
```python
# Intervalos de confiança (statsmodels)
X_with_const = sm.add_constant(X_train_adj)
model_final_sm = sm.OLS(y_train_adj, X_with_const).fit()
print(model_final_sm.summary())
```

**Interpretar top 3 coeficientes:**
"A feature 'grade' tem coeficiente de 0.35 (após transformação log), indicando que um aumento de 1 ponto no grade multiplica o preço por exp(0.35) ≈ 1.42, ou seja, 42% de aumento. Isso faz sentido pois grade reflete qualidade construtiva."

---

#### 5.2 Limitações do Modelo

**Texto crítico:**
"Apesar do R² de 0.83, o modelo possui limitações:
1. Dados são de 2014-2015, podem estar desatualizados
2. Não captura efeitos de eventos recentes (pandemia, mudanças econômicas)
3. Features importantes podem estar ausentes (crime, qualidade de escolas)
4. Assume linearidade mesmo após transformações"

---

#### 5.3 Aplicação Prática

**Recomendações para imobiliária:**
"Com base no modelo:
1. Priorizar imóveis com grade alto (maior ROI)
2. Waterfront tem impacto de +$X no preço médio
3. Reformas que aumentem sqft_living têm retorno de $280/sqft
4. Localização (lat/long) é crítica: imóveis em [coordenadas] valem até Y% mais"

---

## ✅ CHECKLIST FINAL Q1

Antes de marcar como completo:

- [ ] Dataset carregado com sucesso
- [ ] EDA completo com TODOS os gráficos obrigatórios
- [ ] Modelo inicial treinado com métricas apresentadas
- [ ] **TODOS os 5 pressupostos verificados** (testes + plots + interpretação)
- [ ] Problemas identificados foram corrigidos
- [ ] Modelo ajustado retreinado
- [ ] Tabela comparativa modelo antes/depois
- [ ] Pressupostos reverificados
- [ ] Interpretação de coeficientes com intervalos de confiança
- [ ] Limitações discutidas
- [ ] Recomendações práticas fornecidas
- [ ] Código comentado linha por linha
- [ ] Markdown explicativo entre células
- [ ] Notebook exportado para HTML

---

## 📊 PESO POR SEÇÃO

- EDA: 20% (0,5 pts)
- Modelo inicial: 30% (0,75 pts)
- Pressupostos: 30% (0,75 pts) ← CRÍTICO
- Ajustes: 30% (0,75 pts)
- Interpretação: 10% (0,25 pts)
- **TOTAL: 2,5 pontos**

---

## 🎯 DICAS PARA NOTA MÁXIMA

1. **Não pule pressupostos** - é o que diferencia mestrado de graduação
2. **Justifique TUDO** - cada transformação, cada remoção de outlier
3. **Conecte com teoria** - por que log funciona? Por que VIF>10 é problema?
4. **Gráficos profissionais** - títulos, labels, legendas, alta resolução
5. **Tabelas bem formatadas** - use DataFrame.style para deixar bonitinho
6. **Escreva em nível acadêmico** - formal, técnico, mas claro
