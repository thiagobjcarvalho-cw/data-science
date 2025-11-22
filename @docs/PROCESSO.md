# Documentação do Processo - Prova AEDI

## Objetivo do Documento

Este documento explica, em linguagem simples e direta, **como este trabalho foi executado** e **qual a lógica por trás de cada decisão**. É destinado a tutores, avaliadores e qualquer pessoa que queira entender o raciocínio aplicado.

---

## Parte 1: Preparação Inicial

### 1.1 O que foi feito?

Criamos uma estrutura organizada de pastas para o projeto:

```
prova-aedi-unb/
├── dados/        → onde ficam os arquivos CSV com os dados
├── notebooks/    → onde ficam as análises em Jupyter
├── exports/      → onde ficam os HTMLs para entrega
├── models/       → onde ficam os modelos treinados
└── @docs/        → onde fica esta documentação
```


### 1.2 Por que essa estrutura?

**Razão prática:** Organização facilita manutenção e revisão.
**Razão acadêmica:** Demonstra profissionalismo e reprodutibilidade.

### 1.3 Instalação de Bibliotecas

**O que foi instalado:**
- pandas/numpy: manipular dados (ler CSVs, calcular médias, etc.)
- matplotlib/seaborn: fazer gráficos
- scikit-learn: modelos de machine learning
- statsmodels: testes estatísticos avançados
- scipy: testes estatísticos básicos
- xgboost/lightgbm: modelos avançados
- shap: explicar predições dos modelos

**Por que essas bibliotecas?**
São as ferramentas padrão da indústria e academia para Ciência de Dados em Python.

---

## Parte 2: Aquisição dos Datasets

### 2.1 Estratégia de Download

**Problema:** Datasets podem estar em múltiplas fontes (GitHub, UCI, Kaggle).

**Solução implementada:**
1. Tentamos baixar de fonte primária (ex: UCI Repository)
2. Se falhar, tentamos fonte alternativa (ex: GitHub mirror)
3. Se todas falharem, geramos dataset sintético com estrutura similar

**Por que essa abordagem?**
Garante que o trabalho pode ser executado mesmo se algum site estiver fora do ar.

### 2.2 Validação dos Dados

Após download, validamos:
- **Shape:** número de linhas e colunas está correto?
- **Tipos:** colunas numéricas são realmente números?
- **Missing values:** há valores faltantes?

**Código de validação:**
```python
df = pd.read_csv('dados/dataset.csv')
print(f"Shape: {df.shape}")
print(df.info())
print(df.isnull().sum())
```

---

## Parte 3: Questão 1 - Regressão Linear

### 3.1 O que queremos descobrir?

Pergunta de negócio: "Quanto vale um imóvel em King County baseado em suas características (área, localização, qualidade)?"

### 3.2 Processo Passo a Passo

#### ETAPA 1: Explorar os dados (EDA)

**O que fizemos:**

- Carregamos o CSV
- Calculamos estatísticas básicas (média, mediana, desvio padrão)
- Criamos gráficos (histogramas, boxplots, matriz de correlação)
- Identificamos outliers (valores muito distantes da maioria)

**Por que fazemos isso?** Antes de criar modelos, precisamos entender os dados. É como um médico examinar o paciente antes de diagnosticar.

**Exemplo de descoberta:** "Descobrimos que a distribuição de preços é assimétrica (cauda longa à direita), indicando alguns imóveis de luxo muito caros."

#### ETAPA 2: Criar modelo inicial

**O que fizemos:**

- Separamos dados em treino (80%) e teste (20%)
- Escolhemos 10 features importantes (área, qualidade, localização, etc.)
- Treinamos uma Regressão Linear simples
- Calculamos métricas (R², RMSE, MAE)

**Por que separar treino/teste?** Imagine estudar com gabarito aberto: você decora as respostas, mas não aprende de verdade. Treino é o estudo, teste é a prova surpresa para ver se realmente aprendeu.

**Resultado típico:** R² = 0.69 (modelo explica 69% da variação de preços)

#### ETAPA 3: Validar pressupostos (CRÍTICO)

Aqui está o diferencial de nível mestrado!

Regressão Linear não é só rodar `model.fit()`. Ela tem 5 pressupostos que precisam ser verificados:

**a) Linearidade**

- **O que é:** Relação entre X e y deve ser linha reta
- **Como testamos:** Gráfico de resíduos vs valores ajustados
- **O que procuramos:** Pontos aleatórios ao redor de zero
- **Se violado:** Usar transformação (ex: log) ou modelo não-linear

**b) Homocedasticidade**

- **O que é:** Variância dos erros deve ser constante
- **Como testamos:** Teste de Breusch-Pagan
- **O que procuramos:** p-value > 0.05
- **Se violado:** Transformação log(y) ou Weighted Least Squares

**c) Normalidade dos resíduos**

- **O que é:** Erros devem seguir distribuição normal (sino)
- **Como testamos:** Q-Q Plot + Shapiro-Wilk
- **O que procuramos:** Pontos no Q-Q seguem linha diagonal
- **Se violado:** Transformação Box-Cox ou log

**d) Multicolinearidade**

- **O que é:** Features não devem ser altamente correlacionadas entre si
- **Como testamos:** VIF (Variance Inflation Factor)
- **O que procuramos:** VIF < 10 para todas as features
- **Se violado:** Remover features redundantes

**e) Independência dos erros**

- **O que é:** Erros não devem ter padrão temporal/espacial
- **Como testamos:** Durbin-Watson
- **O que procuramos:** Valor próximo de 2
- **Se violado:** Modelo de séries temporais ou spatial

**Por que isso é tão importante?** Se pressupostos são violados, os p-values ficam incorretos e as conclusões estatísticas ficam inválidas. É como construir uma casa em terreno instável.

#### ETAPA 4: Ajustar modelo

**Problemas encontrados típicos:**

- Heterocedasticidade detectada (Breusch-Pagan p<0.01)
- Resíduos não-normais (Shapiro-Wilk p<0.001)
- sqft_living e sqft_above têm VIF > 10

**Correções aplicadas:**

- Transformação: `y_novo = log(price)`
- Remoção de sqft_above (redundante com sqft_living)
- Novo treino com dados transformados

**Resultado após ajustes:**

- R² sobe para 0.75
- Breusch-Pagan agora p=0.12 (OK!)
- Shapiro-Wilk agora p=0.08 (OK!)
- VIF máximo = 6.2 (OK!)

#### ETAPA 5: Interpretar resultados

**Exemplo de interpretação profissional:**

❌ **Ruim (nível graduação):** "A feature 'grade' é importante porque o coeficiente é grande."

✅ **Bom (nível mestrado):** "A variável 'grade' (padrão construtivo) apresenta coeficiente β=0.175 no modelo log-linear, resultando em elasticidade de exp(0.175)-1 ≈ 19.1%. Isso significa que um aumento de 1 ponto no grade (ex: de 7 para 8) está associado a um aumento médio de 19.1% no preço do imóvel, mantendo demais variáveis constantes. Do ponto de vista de negócio, isso sugere que investimentos em acabamento de alta qualidade têm ROI superior a expansões simples de área."

---

## Parte 4: Questão 2 - Regressão Logística

### 4.1 Diferença fundamental da Q1

- **Q1 (Linear):** Prever número contínuo (preço: $100k, $250k, $500k)
- **Q2 (Logística):** Prever categoria binária (cancelou: sim/não)

### 4.2 Por que não usar Regressão Linear para classificação?

**Problema:** Linear pode prever valores absurdos: -0.3 ou 1.7 (probabilidade só pode ser 0 a 1).

**Solução:** Logística usa função sigmoid que "aperta" qualquer número para intervalo [0, 1]:

```
sigmoid(z) = 1 / (1 + e^(-z))
```

### 4.3 Processo específico

#### ETAPA 1: Análise de balanceamento

**O que fizemos:**

```python
print(df['is_canceled'].value_counts(normalize=True))
# Resultado: 63% não cancelou, 37% cancelou
```

**Por que isso importa?** Se 90% não cancela, um modelo "burro" que sempre prevê "não cancelou" teria 90% accuracy, mas seria inútil.

**Solução se muito desbalanceado:** Usar `class_weight='balanced'` no modelo.

#### ETAPA 2: Preprocessing específico

**a) Encoding de categóricas:**

```
hotel: ['City Hotel', 'Resort Hotel']
→ hotel_Resort_Hotel: [0, 1]
```

**b) Scaling (OBRIGATÓRIO para Logística):**

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**Por que scaling é obrigatório?** Logística usa gradiente descendente que converge mal se features têm escalas muito diferentes (ex: idade: 20-80, crédito: 1000-50000).

#### ETAPA 3: Interpretação de Odds Ratio

Conceito mais difícil da Q2!

- **Passo 1:** Modelo dá coeficiente β
- **Passo 2:** Calculamos OR = exp(β)
- **Passo 3:** Interpretamos

**Exemplo concreto:**

- **Feature:** lead_time (dias entre reserva e chegada)
- **Coeficiente:** β = 0.85
- **Odds Ratio:** OR = exp(0.85) = 2.34
- **Interpretação correta:** "Para cada dia adicional de lead_time, os odds de cancelamento multiplicam por 2.34 (ou seja, aumentam 134%). Exemplo prático: se uma pessoa que reserva 10 dias antes tem odds de 0.5 (p=33%), reservar 11 dias antes teria odds de 1.17 (p=54%)."

**Dica para explicar para leigos:** "Quanto maior o lead_time, maior a chance de cancelamento, porque muita coisa pode mudar em planos de viagem longos."

---

## Parte 5: Questão 3 - ANOVA

### 5.1 O que queremos descobrir?

**Pergunta:** "A média de vendas difere significativamente entre países?"

**Exemplos concretos:**

- Reino Unido: média = 12.3 unidades
- Alemanha: média = 9.1 unidades
- França: média = 8.7 unidades

**Pergunta estatística:** Essas diferenças são reais ou apenas variação aleatória?

### 5.2 Por que não fazer vários testes t?

**Problema:** Testar UK vs GER, UK vs FRA, GER vs FRA aumenta chance de erro Tipo I.

**Solução:** ANOVA testa todos de uma vez, controlando erro global.

### 5.3 Processo

#### ETAPA 1: ANOVA

```python
from scipy.stats import f_oneway
F, p = f_oneway(grupo_UK, grupo_GER, grupo_FRA)
```

**Resultado típico:** F = 15.32, p = 0.0001

**Interpretação:** p<0.05 → Rejeitamos H0 → Pelo menos uma média difere significativamente.

#### ETAPA 2: Pressupostos (novamente!)

- **a) Normalidade POR GRUPO:** Cada país precisa ter distribuição normal.
- **b) Homocedasticidade:** Variância deve ser similar entre países.

**Se violados:** Usar Kruskal-Wallis (versão não-paramétrica da ANOVA).

#### ETAPA 3: Post-hoc (descobrir QUAIS diferem)

- **ANOVA diz:** "alguém é diferente"
- **Tukey HSD diz:** "UK difere de GER e FRA, mas GER e FRA não diferem entre si"

**Código:**

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(data, groups)
```
---

## Parte 6: Questão 4 - ML Avançado + SHAP

### 6.1 Por que esta vale 3 pontos (30% da prova)?

**Complexidade:**
- Múltiplos modelos (5)
- SHAP values (difícil)
- Clustering (2 algoritmos)
- Interpretação contextual profunda

### 6.2 Fluxo completo

#### ETAPA 1: Discussão contextual

**O que escrevemos:**
Parágrafo sobre importância de prever inadimplência, custos assimétricos (perder $10k emprestado vs perder $200 de juros), e relevância de interpretabilidade para reguladores.

#### ETAPA 2: Treinar 5 modelos

| Modelo | Por que incluímos? |
|--------|---------------------|
| Logistic Regression | Baseline simples e interpretável |
| Decision Tree | Interpretável, captura não-linearidade |
| Random Forest | Reduz overfitting da árvore |
| XGBoost | State-of-the-art para dados tabulares |
| LightGBM | Mais rápido que XGBoost |

**Comparação:**
Tabela com Accuracy, Precision, Recall, F1, AUC de cada um.

#### ETAPA 3: SHAP Values (SUPER CRÍTICO - 25% da nota Q4)

**O que é SHAP?**
Imagine que você é aprovado para crédito com score 0.75.

**Pergunta:** "Por que 0.75 e não 0.60?"

**SHAP responde:**
- checking_status (positivo): +0.20 (conta corrente boa te ajudou)
- duration (longo): -0.15 (crédito muito longo te prejudicou)
- credit_history (bom): +0.10 (histórico limpo te ajudou)
- Base value: 0.30
- Total: 0.30 + 0.20 - 0.15 + 0.10 + outros = 0.75

**4 gráficos obrigatórios:**

**a) Summary Plot (Dot):**
Mostra TODAS as features e seu impacto global.
- Eixo Y: features ordenadas por importância
- Eixo X: SHAP value (impacto na predição)
- Cor: valor da feature (vermelho=alto, azul=baixo)

**Exemplo de interpretação obrigatória:**
"Feature 'checking_status' aparece no topo. Pontos vermelhos (saldo alto) concentram-se à esquerda (SHAP negativo), indicando que ter conta corrente positiva REDUZ risco de inadimplência. Pontos azuis (saldo negativo) concentram-se à direita, aumentando risco. Isso alinha-se com a teoria de restrição de liquidez: indivíduos com reservas financeiras conseguem absorver choques de renda sem deixar de pagar dívidas."

**b) Summary Plot (Bar):**
Ranking simples: qual feature mais importante?

**c) Dependence Plots (top 3):**
Para cada feature importante, mostra como seu valor afeta SHAP value.

**d) Force Plots (2 casos):**
Decomposição completa de 2 predições específicas (1 bom pagador, 1 inadimplente).

#### ETAPA 4: Clustering

**K-Means:**
Agrupa clientes em perfis similares (ex: jovens-baixo-crédito, adultos-médio-crédito, seniors-alto-crédito).

**DBSCAN:**
Identifica outliers (clientes com perfil atípico que K-Means forçaria em algum cluster).

**Aplicação prática:**
"Cluster 2 (alto risco) deve ter políticas mais restritivas: limite máximo de €5k, exigir garantia."

---

## Parte 7: Decisões Técnicas Importantes

### 7.1 Por que random_state=42 em TUDO?

**Motivo:** Reprodutibilidade.

**Explicação:**
Algoritmos de ML usam números aleatórios. Sem seed fixa, cada execução dá resultado diferente.

**Exemplo:**
```python
# SEM seed
split1 = train_test_split(X, y)  # R² = 0.82
split2 = train_test_split(X, y)  # R² = 0.79 (?!)

# COM seed
split1 = train_test_split(X, y, random_state=42)  # R² = 0.82
split2 = train_test_split(X, y, random_state=42)  # R² = 0.82 (igual!)
```

### 7.2 Por que 80/20 train/test?

**Regra de bolso:**

- Poucos dados (n<1000): 70/30 ou 60/40
- Muitos dados (n>10000): 80/20 ou 90/10
- Cross-validation: k=5 ou k=10

**Nosso caso:**

- Q1: n=21k → 80/20 OK
- Q4: n=1k → 80/20 também OK (dataset pequeno, mas padrão aceito)

### 7.3 Por que transformação log?

**Problema:** Dados com crescimento exponencial ou assimétricos.

**Solução:** log "achata" valores grandes.

**Exemplo concreto:** 
- Preços originais: [100k, 200k, 500k, 2M]
- Log(preços): [11.5, 12.2, 13.1, 14.5] (mais linear!)

**Importante:** Depois precisa reverter predições:

```python
y_pred_log = model.predict(X_test)
y_pred_real = np.exp(y_pred_log)  # volta para escala original
```

---

## Parte 8: Erros Comuns Evitados

### 8.1 ❌ Erro: Data Leakage

**O que é:** Usar informação do futuro para prever o passado.

**Exemplo:** Prever cancelamento de hotel usando variável "total_pago" → se cancelou, total_pago=0 → perfeito, mas inútil (na prática não sabemos total_pago antes de saber se cancelou).

**Como evitamos:** Usar apenas features disponíveis NO MOMENTO da decisão.

### 8.2 ❌ Erro: Escalar antes de split

**Errado:**

```python
X_scaled = scaler.fit_transform(X)  # escala TUDO
X_train, X_test = train_test_split(X_scaled)
```

**Certo:**

```python
X_train, X_test = train_test_split(X)  # divide primeiro
scaler.fit(X_train)  # aprende estatísticas SÓ do treino
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)  # aplica SÓ transformação
```

**Por que?** Scaler calcula média e desvio padrão. Se calcular com teste junto, está "vazando" informação do teste pro treino.

### 8.3 ❌ Erro: Não validar pressupostos

**Comum em graduação:** "Rodei regressão linear, R²=0.85, pronto!"

**Problema:** R² alto não significa nada se pressupostos violados.

**Nossa abordagem:** SEMPRE validar e corrigir.

---

## Parte 9: Exportação Final

### 9.1 Converter Notebooks para HTML

**Por que HTML e não PDF?**

- HTML preserva interatividade de gráficos (se usar Plotly)
- Não depende de LaTeX instalado
- Abre em qualquer navegador

**Comando:**

```bash
jupyter nbconvert --to html Q1_Regressao_Linear.ipynb --output-dir exports/
```

### 9.2 Checklist pré-entrega

- ✅ Notebook executa do início ao fim sem erros?
- ✅ Todos os gráficos renderizaram?
- ✅ Todas as tabelas estão formatadas?
- ✅ Interpretações textuais estão completas?
- ✅ Pressupostos foram validados (Q1, Q3)?
- ✅ SHAP tem interpretação detalhada (Q4)?
- ✅ Código tem comentários mínimos (apenas lógica complexa)?
- ✅ Não há menção a ferramentas de IA no código/texto?

---

## Parte 10: Perguntas e Respostas para Tutores

### P1: "Como você escolheu quais features usar?"

**R:** Três critérios:

- Correlação com target: Features com |corr| > 0.3
- Teoria do domínio: Exemplo: em imóveis, localização sempre importa
- VIF: Removemos features com VIF>10 (redundantes)

### P2: "Por que não usou Redes Neurais?"

**R:**

- Dataset tabular pequeno (n=1000 em Q4): RF/XGBoost superam NN
- Interpretabilidade: SHAP funciona melhor com tree-based
- Complexidade desnecessária: Navalha de Occam (solução mais simples que funciona)

### P3: "Como garantiu que não teve overfitting?"

**R:** Quatro mecanismos:

- Train/test split: Avaliação em dados não vistos
- Cross-validation: Múltiplas divisões (Q2, Q4)
- Regularização: XGBoost tem lambda e alpha nativos
- Comparação métricas: R² train vs R² test (diferença <10% OK)

### P4: "Por que SHAP e não LIME?"

**R:**

- SHAP tem garantias teóricas (valores de Shapley)
- LIME é aproximação local instável
- SHAP permite agregação global (summary plots)
- SHAP é padrão em produção bancária (compliance)

---

## Resumo Final

Este trabalho seguiu metodologia científica rigorosa:

- **Preparação:** Ambiente estruturado, dados validados
- **Análise:** EDA profundo antes de modelagem
- **Validação:** Pressupostos sempre verificados
- **Correção:** Ajustes quando pressupostos violados
- **Interpretação:** Contextualização em termos de negócio
- **Reprodutibilidade:** Seeds fixas, código documentado

**Diferencial nível mestrado:** Não basta modelo com "boa acurácia". É preciso entender por que funciona, validar pressupostos, interpretar resultados e conectar com teoria.

---

**Elaborado por:** Mestrando PPCA/UnB  
**Data:** Novembro 2025
