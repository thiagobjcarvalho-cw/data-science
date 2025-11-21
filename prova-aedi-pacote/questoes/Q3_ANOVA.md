# QUESTÃO 3: ANOVA (2,0 pontos)

## 📊 DATASET
**Nome:** Online Retail  
**Objetivo:** Comparar médias de Quantity e UnitPrice entre países  
**Método:** ANOVA (Analysis of Variance)

---

## 🎯 OBJETIVO
Analisar se há diferença significativa nas médias de quantidade vendida e preço unitário entre diferentes países.

---

## 📋 ETAPAS

### a) ANÁLISE DESCRITIVA (10% = 0,2 pts)

```python
# Carregar
df = pd.read_excel('Online_Retail.xlsx')  # ou URL UCI

# Top países
top_countries = df['Country'].value_counts().head(7).index.tolist()
df_filtered = df[df['Country'].isin(top_countries)].copy()

# Limpar outliers extremos (opcional)
# Q1, Q3 = df_filtered['Quantity'].quantile([0.25, 0.75])
# IQR = Q3 - Q1
# df_filtered = df_filtered[(df_filtered['Quantity'] > Q1-1.5*IQR) & 
#                            (df_filtered['Quantity'] < Q3+1.5*IQR)]
```

**Gráficos:**
```python
# Boxplots
df_filtered.boxplot(column='Quantity', by='Country', figsize=(12,6))
plt.suptitle('')  # remover título automático
plt.title('Distribuição de Quantity por País')
plt.show()

df_filtered.boxplot(column='UnitPrice', by='Country', figsize=(12,6))
plt.suptitle('')
plt.title('Distribuição de UnitPrice por País')
plt.show()

# Estatísticas descritivas
print(df_filtered.groupby('Country')[['Quantity', 'UnitPrice']].describe())
```

---

### b) ANOVA - COMPARAÇÃO ENTRE PAÍSES (40% = 0,8 pts)

#### b.1 ANOVA para Quantity

```python
from scipy.stats import f_oneway

# Separar grupos
groups_qty = [df_filtered[df_filtered['Country']==country]['Quantity'].dropna() 
              for country in top_countries]

# ANOVA
F_stat_qty, p_value_qty = f_oneway(*groups_qty)

print(f"ANOVA - Quantity:")
print(f"  F-statistic: {F_stat_qty:.4f}")
print(f"  p-value: {p_value_qty:.4f}")
```

**Interpretação:**
- **H0:** μ₁ = μ₂ = ... = μₖ (todas as médias são iguais)
- **H1:** Pelo menos uma média difere
- **Decisão:** Se p < 0.05, rejeitar H0

"Com p-value de [valor], [rejeitamos/não rejeitamos] H0 ao nível de significância de 5%. [Se rejeitar: Há evidência estatística de que as médias de quantidade vendida diferem entre países]."

#### b.2 ANOVA para UnitPrice

```python
groups_price = [df_filtered[df_filtered['Country']==country]['UnitPrice'].dropna() 
                for country in top_countries]

F_stat_price, p_value_price = f_oneway(*groups_price)

print(f"ANOVA - UnitPrice:")
print(f"  F-statistic: {F_stat_price:.4f}")
print(f"  p-value: {p_value_price:.4f}")
```

**Tabela resumo:**
| Variável | F-statistic | p-value | Conclusão |
|----------|-------------|---------|-----------|
| Quantity | 15.32 | <0.001 | Rejeitar H0 |
| UnitPrice | 8.71 | <0.001 | Rejeitar H0 |

---

### c) VERIFICAÇÃO DE PRESSUPOSTOS (40% = 0,8 pts) ⚠️ CRÍTICO

ANOVA assume 3 pressupostos:

#### c.1 NORMALIDADE DOS RESÍDUOS

```python
# Shapiro-Wilk por grupo (se n < 5000 por grupo)
for country in top_countries:
    data = df_filtered[df_filtered['Country']==country]['Quantity'].dropna()
    if len(data) < 5000:
        stat, p = stats.shapiro(data)
        print(f"{country}: W={stat:.4f}, p={p:.4f}")
    else:
        print(f"{country}: Amostra muito grande para Shapiro-Wilk")

# Q-Q plots por grupo (visualizar)
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
for i, country in enumerate(top_countries):
    data = df_filtered[df_filtered['Country']==country]['Quantity'].dropna()
    stats.probplot(data, dist="norm", plot=axes[i//4, i%4])
    axes[i//4, i%4].set_title(country)
plt.tight_layout()
plt.show()
```

**Interpretação:**
"Testes de Shapiro-Wilk revelam que [X de Y] grupos violam normalidade (p<0.05). Q-Q plots confirmam desvios nas caudas, especialmente para [países]."

---

#### c.2 HOMOCEDASTICIDADE (homogeneidade de variâncias)

```python
from scipy.stats import levene, bartlett

# Teste de Levene (mais robusto)
levene_stat, levene_p = levene(*groups_qty)
print(f"Levene Test: statistic={levene_stat:.4f}, p-value={levene_p:.4f}")

# Teste de Bartlett (sensível a não-normalidade)
bartlett_stat, bartlett_p = bartlett(*groups_qty)
print(f"Bartlett Test: statistic={bartlett_stat:.4f}, p-value={bartlett_p:.4f}")
```

**Critério:**
- H0: variâncias são iguais
- Se p < 0.05: REJEITAR H0 = heterocedasticidade

**Interpretação:**
"Teste de Levene (p=[valor]) [indica/não indica] heterocedasticidade. [Se violado: Bartlett confirma (p=[valor]), sugerindo que variâncias diferem significativamente entre países]."

---

#### c.3 INDEPENDÊNCIA

"Assumimos independência das observações pois cada transação é uma venda única, sem relação temporal ou hierárquica entre elas."

---

#### c.4 MODELO AJUSTADO (se pressupostos violados)

**Opção 1: Transformação Logarítmica**
```python
# Se não-normalidade E heterocedasticidade
df_filtered['log_Quantity'] = np.log1p(df_filtered['Quantity'])

# Refazer ANOVA
groups_log = [df_filtered[df_filtered['Country']==country]['log_Quantity'].dropna() 
              for country in top_countries]
F_log, p_log = f_oneway(*groups_log)
print(f"ANOVA com log: F={F_log:.4f}, p={p_log:.4f}")

# Reverificar pressupostos
levene_log, p_levene_log = levene(*groups_log)
print(f"Levene após log: p={p_levene_log:.4f}")
```

**Opção 2: Teste Não-Paramétrico (Kruskal-Wallis)**
```python
from scipy.stats import kruskal

# Se normalidade fortemente violada
H_stat, kw_p = kruskal(*groups_qty)
print(f"Kruskal-Wallis: H={H_stat:.4f}, p={kw_p:.4f}")
```

**Justificar escolha:**
"Dado que [pressupostos violados], optamos por [transformação log / Kruskal-Wallis] porque [razão]. Após correção, [pressupostos foram/não foram] atendidos."

**Comparar resultados:**
| Teste | F/H-statistic | p-value | Conclusão |
|-------|---------------|---------|-----------|
| ANOVA Original | 15.32 | <0.001 | Rejeitar H0 |
| ANOVA com log | 12.87 | <0.001 | Rejeitar H0 |
| Kruskal-Wallis | 145.6 | <0.001 | Rejeitar H0 |

---

### d) POST-HOC: Comparações Múltiplas (se ANOVA significativa)

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Tukey HSD
tukey = pairwise_tukeyhsd(df_filtered['Quantity'], df_filtered['Country'], alpha=0.05)
print(tukey)

# Visualizar
fig = tukey.plot_simultaneous(figsize=(10,6))
plt.show()
```

**Tabela de comparações:**
| Grupo 1 | Grupo 2 | Mean Diff | p-adj | Reject H0 |
|---------|---------|-----------|-------|-----------|
| UK | Germany | -5.2 | 0.001 | True |
| UK | France | -3.1 | 0.045 | True |
| Germany | France | 2.1 | 0.234 | False |

**Interpretação:**
"Teste de Tukey revela que Reino Unido difere significativamente de Alemanha (p=0.001) e França (p=0.045). Entretanto, Alemanha e França não diferem entre si (p=0.234)."

**Plot com letras de significância:**
```python
# Médias por país
means = df_filtered.groupby('Country')['Quantity'].mean().sort_values()

# Adicionar letras (A, B, C) para grupos que não diferem
# Grupos com mesma letra = não diferem estatisticamente
```

---

### e) INTERPRETAÇÃO E TOMADA DE DECISÃO (10% = 0,2 pts)

**Análise contextual:**

"**Quantidade Vendida:**
- Reino Unido apresenta maior média (μ=12.3 unidades)
- Alemanha e França têm médias intermediárias (~9 unidades)
- Possível explicação: UK é mercado doméstico (empresa britânica), maiores volumes

**Preço Unitário:**
- Alemanha tem maior preço médio (£4.8)
- Pode refletir: poder aquisitivo, mix de produtos premium, custos de envio

**Decisões Estratégicas:**

1. **Marketing:** 
   - Focar volume no UK (mercado já consolidado)
   - Focar margem na Alemanha (clientes pagam mais)

2. **Precificação:**
   - Considerar estratégia diferenciada por país
   - Alemanha pode tolerar preços 15% mais altos

3. **Estoque:**
   - Alocar maior volume de produtos de baixo valor no UK
   - Produtos premium para Alemanha

4. **Investigar causas:**
   - Por que França tem menor volume? Problema de distribuição?
   - Diferenças culturais em padrões de compra?"

---

## ✅ CHECKLIST Q3

- [ ] EDA com boxplots por país
- [ ] ANOVA executada para Quantity E UnitPrice
- [ ] Tabela ANOVA com F-statistic e p-value
- [ ] Hipóteses (H0/H1) declaradas
- [ ] **PRESSUPOSTOS verificados:**
  - [ ] Normalidade (Shapiro-Wilk + Q-Q plots)
  - [ ] Homocedasticidade (Levene + Bartlett)
  - [ ] Independência (assumida e justificada)
- [ ] Se pressupostos violados: correções aplicadas
- [ ] Modelo ajustado (log ou Kruskal-Wallis)
- [ ] Pressupostos reverificados
- [ ] Post-hoc (Tukey HSD) se ANOVA significativa
- [ ] Interpretação contextual (varejo/negócio)
- [ ] Decisões estratégicas sugeridas
- [ ] HTML exportado

---

## 🎯 DICAS

1. **Não ignore pressupostos violados** - isso tira pontos!
2. **Kruskal-Wallis** é seu amigo se normalidade for muito violada
3. **Tukey HSD** só faz sentido se ANOVA foi significativa
4. **Contexto de negócio** é chave - não basta dizer "há diferença", explique POR QUE importa
5. **Outliers** podem distorcer resultados - considere filtrá-los (justificando)
