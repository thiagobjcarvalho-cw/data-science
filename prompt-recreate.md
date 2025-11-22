# 🔄 Prompt de Recriação Completa - Trabalho AEDI

## 🎯 Objetivo

Recriar **TODO** o trabalho da Prova Final AEDI (Mestrado PPCA/UnB) de forma incremental, organizada e reprodutível.

---

## 📚 Contexto (LEIA PRIMEIRO)

Antes de começar, leia estes arquivos para entender o contexto:

1. **`previous-chat-resume.md`** - Resumo da sessão anterior e decisões tomadas
2. **`@docs/README.md`** - Índice da documentação (já existe)
3. **`@docs/GLOSSARIO.md`** - Glossário técnico (já existe)
4. **`@docs/GUIA_IMPLEMENTACAO.md`** - Guia de implementação (pode estar incompleto)

---

## ⚙️ Configuração Inicial

### Passo 0: Verificar ambiente

```bash
# Verificar que estamos no repositório correto
pwd  # Deve mostrar: /home/user/trabalho-dc (ou similar)
git remote -v  # Confirmar remote: trabalho-dc
git branch  # Confirmar branch atual
```

### Passo 1: Criar estrutura de diretórios

```bash
mkdir -p prova-aedi-unb/{dados,notebooks,exports,models}
mkdir -p @docs
```

---

## 📝 PARTE 1: Completar Documentação

### Arquivo 1/5: @docs/README.md

**Status:** ✅ Já existe - verificar apenas

### Arquivo 2/5: @docs/GLOSSARIO.md

**Status:** ✅ Já existe - verificar apenas

### Arquivo 3/5: @docs/GUIA_IMPLEMENTACAO.md

**Status:** ⚠️ Pode estar incompleto - completar se necessário

**Conteúdo esperado (~18KB):**

- Seções 1-3: Visão geral + implementação das 4 questões
- Seções 4-9: Padrões de qualidade, exportação, referências

### Arquivo 4/5: @docs/PROCESSO.md

**Criar arquivo:** `@docs/PROCESSO.md`

**Tamanho:** ~18KB

**Conteúdo:** Explicação em linguagem simples do processo completo

- Parte 1: Preparação inicial
- Parte 2: Aquisição de datasets
- Parte 3-6: Processo de cada questão (Q1, Q2, Q3, Q4)
- Parte 7-10: Decisões técnicas, erros evitados, exportação, FAQ

**Referência:** Use o arquivo da sessão anterior como base (consta no previous-chat-resume.md)

### Arquivo 5/5: @docs/METODOLOGIA.md

**Criar arquivo:** `@docs/METODOLOGIA.md`

**Tamanho:** ~14KB

**Conteúdo:** Fundamentação estatística e matemática

- Seção 1: Fundamentos de Regressão Linear
- Seção 2: Fundamentos de Regressão Logística
- Seção 3: Fundamentos de ANOVA
- Seção 4: Fundamentos de ML (árvores, Random Forest, XGBoost, SHAP, clustering)
- Seções 5-8: Inferência, testes de hipóteses, validação cruzada, regularização

**Referência:** Use o arquivo da sessão anterior como base

---

### ✅ Checkpoint 1: Commit da documentação

```bash
git add @docs/
git commit -m "Adiciona documentação completa (@docs/)"
git status  # Verificar
```

---

## 🐍 PARTE 2: Criar Scripts Python

### Script 1/3: prova-aedi-unb/create_german_credit.py

**Função:** Gerar dataset German Credit sintético (1000 linhas, 21 colunas)

**Características:**

- Seed: 42 (reprodutibilidade)
- Features categóricas e numéricas
- Target: 'class' (good/bad)
- Correlações realistas entre features
- Tamanho: ~130 linhas

### Script 2/3: prova-aedi-unb/download_datasets.py

**Função:** Download de datasets com múltiplas fontes fallback

**Datasets:**

- King County Houses (~21k linhas)
- Hotel Bookings (~119k linhas)
- Online Retail (~50k linhas)
- German Credit (usa create_german_credit.py)

**Estratégia:** Tentar URL primária → URL alternativa → Gerar sintético

**Tamanho:** ~100 linhas

### Script 3/3: prova-aedi-unb/download_datasets_v2.py

**Função:** Versão aprimorada do download_datasets.py

**Melhorias:**

- Validação de integridade (shape, tipos)
- Logging detalhado
- Tratamento robusto de erros

**Tamanho:** ~150 linhas

---

### ✅ Checkpoint 2: Commit dos scripts

```bash
git add prova-aedi-unb/*.py
git commit -m "Adiciona scripts Python para geração de datasets"
git status
```

---

## 📊 PARTE 3: Gerar Datasets

### Executar geração de datasets

```bash
cd prova-aedi-unb
python download_datasets_v2.py
# Ou: python download_datasets.py
cd ..
```

### Resultado esperado:

```
dados/
├── king_county_houses.csv      (~2.8 MB, 21613 linhas)
├── hotel_bookings.csv          (~17 MB, 119390 linhas)
├── online_retail.csv           (~4.5 MB, 50000 linhas)
└── german_credit.csv           (~136 KB, 1000 linhas)
```

### Validar datasets

```bash
ls -lh prova-aedi-unb/dados/
wc -l prova-aedi-unb/dados/*.csv
```

---

### ✅ Checkpoint 3: Commit dos datasets

```bash
git add prova-aedi-unb/dados/
git commit -m "Adiciona datasets completos (24MB)"
git status
```

---

## 📓 PARTE 4: Criar Notebooks (4 questões)

### Notebook 1/4: Q1_Regressao_Linear.ipynb

**Dataset:** king_county_houses.csv

**Seções:**

- Imports e configurações
- EDA completo (estatísticas, visualizações)
- Modelagem inicial (OLS)
- Validação de pressupostos (CRÍTICO - 30% da nota):
  - Linearidade
  - Homocedasticidade (Breusch-Pagan)
  - Normalidade (Shapiro-Wilk, Q-Q plot)
  - Multicolinearidade (VIF)
  - Independência (Durbin-Watson)
- Ajustes e correções (transformação log se necessário)
- Interpretação de resultados
- Métricas: R², R² ajustado, RMSE, MAE

### Notebook 2/4: Q2_Regressao_Logistica.ipynb

**Dataset:** hotel_bookings.csv

**Seções:**

- Imports
- EDA + análise de balanceamento
- Preprocessing (encoding, scaling, stratified split)
- Modelagem (LogisticRegression + GridSearchCV)
- Análise de Odds Ratios (CRÍTICO)
- Métricas (Accuracy, Precision, Recall, F1, AUC-ROC)
- Matriz de confusão + Curva ROC
- Interpretação

### Notebook 3/4: Q3_ANOVA.ipynb

**Dataset:** online_retail.csv

**Seções:**

- Imports
- Preparação (selecionar top 7 países)
- ANOVA (scipy.stats.f_oneway)
- Validação de pressupostos (CRÍTICO):
  - Normalidade por grupo (Shapiro-Wilk)
  - Homocedasticidade (Levene)
- Post-hoc Tukey HSD
- Interpretação de negócio

### Notebook 4/4: Q4_ML_Avancado.ipynb

**Dataset:** german_credit.csv

**Seções:**

- Discussão contextual (0.3 pts)
- EDA completo (0.45 pts)
- Múltiplos modelos (0.9 pts):
  - Logistic Regression (baseline)
  - Decision Tree
  - Random Forest
  - XGBoost
  - LightGBM
- SHAP Values (0.75 pts - 25% DA NOTA Q4 - SUPER CRÍTICO):
  - Summary plot (dot)
  - Summary plot (bar)
  - Dependence plots (top 3)
  - Force plots (2 casos)
  - Interpretação textual acadêmica obrigatória (5 parágrafos)
- Clustering (0.45 pts):
  - K-Means + Elbow method
  - DBSCAN + outlier detection
- Decisão estratégica (0.3 pts)

### Padrões de qualidade para TODOS os notebooks

**Código:**

- random_state=42 em TODAS operações aleatórias
- Comentários apenas em lógica complexa (<10%)
- Variáveis descritivas (não usar x, y, tmp)

**Visualizações:**

- figsize=(10, 6) padrão
- Fontes 12pt mínimo
- Títulos, eixos, legendas sempre presentes
- Paleta acadêmica

**Texto interpretativo:**

- Nível de rigor: mestrado
- Estrutura: Afirmação → Evidência → Interpretação
- Sempre incluir valores numéricos específicos
- Conectar estatística com contexto de negócio

---

### ✅ Checkpoint 4: Commit dos notebooks

```bash
git add prova-aedi-unb/notebooks/
git commit -m "Adiciona notebooks completos (Q1, Q2, Q3, Q4)"
git status
```

---

## 📤 PARTE 5: Exportar para HTML

```bash
cd prova-aedi-unb
jupyter nbconvert --to html notebooks/Q1_Regressao_Linear.ipynb --output-dir exports/
jupyter nbconvert --to html notebooks/Q2_Regressao_Logistica.ipynb --output-dir exports/
jupyter nbconvert --to html notebooks/Q3_ANOVA.ipynb --output-dir exports/
jupyter nbconvert --to html notebooks/Q4_ML_Avancado.ipynb --output-dir exports/
cd ..
```

---

### ✅ Checkpoint 5: Commit das exportações

```bash
git add prova-aedi-unb/exports/
git commit -m "Adiciona exportações HTML dos notebooks"
git status
```

---

## ✅ PARTE 6: Validação Final

### Checklist de validação

Execute esta verificação antes de considerar o trabalho completo:

```bash
# 1. Estrutura de diretórios
ls -la @docs/
ls -la prova-aedi-unb/

# 2. Documentação (5 arquivos)
wc -l @docs/*.md

# 3. Scripts Python (3 arquivos)
ls -la prova-aedi-unb/*.py

# 4. Datasets (4 arquivos)
ls -lh prova-aedi-unb/dados/

# 5. Notebooks (4 arquivos)
ls -la prova-aedi-unb/notebooks/

# 6. Exportações HTML (4 arquivos)
ls -la prova-aedi-unb/exports/

# 7. Git status
git status
git log --oneline -10
```

### Checklist de conteúdo

- ✅ Todos os 4 notebooks executam sem erros?
- ✅ Pressupostos validados em Q1 e Q3?
- ✅ SHAP tem interpretação textual completa em Q4?
- ✅ Todos os gráficos renderizaram?
- ✅ Código tem comentários mínimos (apenas lógica complexa)?
- ✅ Interpretações conectam estatística com contexto?
- ✅ HTMLs exportados estão legíveis?

---

## 🚀 PARTE 7: Push Final

```bash
# Verificar que tudo está commitado
git status

# Ver resumo dos commits
git log --oneline -10

# Push para o GitHub
git push -u origin main
# OU (dependendo do branch configurado):
# git push -u origin claude/analyze-aedi-data-01VtrSdgmuV5TL4zynd5meq8
```

---

## 📊 Resultado Final Esperado

Ao terminar, o repositório deve ter:

```
trabalho-dc/
├── @docs/                           (5 arquivos, ~70KB)
│   ├── README.md
│   ├── GLOSSARIO.md
│   ├── GUIA_IMPLEMENTACAO.md
│   ├── PROCESSO.md
│   └── METODOLOGIA.md
│
├── prova-aedi-unb/
│   ├── dados/                       (4 CSVs, ~24MB)
│   ├── notebooks/                   (4 .ipynb)
│   ├── exports/                     (4 .html)
│   ├── models/                      (vazio por enquanto)
│   ├── create_german_credit.py
│   ├── download_datasets.py
│   └── download_datasets_v2.py
│
├── previous-chat-resume.md
├── prompt-recreate.md               (este arquivo)
└── README.md
```

- **Total de commits:** ~6-8
- **Total de arquivos:** ~25
- **Tamanho total:** ~25MB

---

## 🎯 Critérios de Sucesso

- ✅ **Documentação:** Completa, clara, sem menções a IA
- ✅ **Código:** Reprodutível (seeds fixas), bem estruturado
- ✅ **Notebooks:** Executam sem erros, gráficos acadêmicos
- ✅ **Validações:** Pressupostos estatísticos verificados (Q1, Q3)
- ✅ **SHAP:** Interpretação textual acadêmica completa (Q4)
- ✅ **Git:** Tudo commitado e pushed com sucesso

---

## ⏱️ Tempo Estimado

| Parte | Descrição | Tempo |
|-------|-----------|-------|
| PARTE 1 | Documentação | 10-15 min |
| PARTE 2 | Scripts | 5-10 min |
| PARTE 3 | Datasets | 5 min |
| PARTE 4 | Notebooks | 60-90 min (a parte mais longa) |
| PARTE 5 | Export | 2 min |
| PARTE 6-7 | Validação + Push | 5 min |
| **TOTAL** | | **90-120 minutos (1.5-2 horas)** |

---

## 🆘 Troubleshooting

| Problema | Solução |
|----------|---------|
| Datasets não geram | Executar create_german_credit.py manualmente, verificar conexão internet |
| Notebook não executa | Verificar que todos os datasets existem em dados/, reinstalar bibliotecas |
| Git push falha | Verificar autenticação, branch correto, tentar commits menores |
| SHAP demora muito | Usar subset dos dados (sample 100-200 linhas para explicações) |

---

## 📝 Notas Importantes

- **Incremental:** Faça commit após cada PARTE completada
- **Validação:** Execute validação após cada notebook
- **SHAP em Q4:** É 25% da nota da Q4 - NÃO PULE A INTERPRETAÇÃO TEXTUAL
- **Pressupostos:** Q1 e Q3 dependem de validação de pressupostos - CRÍTICO

---

**Criado:** Novembro 2025  
**Versão:** 1.0  
**Status:** Pronto para execução
