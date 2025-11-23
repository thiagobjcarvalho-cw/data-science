# 🎓 GUIA DE EXECUÇÃO - Prova Final AEDI UnB

## 📋 Informações Gerais

- **Disciplina:** Análise Estatística de Dados e Informações
- **Programa:** PPCA - UnB (Mestrado)
- **Data da Prova:** 23/11/2025
- **Pontuação Total:** 10 pontos (4 questões)

---

## 🚀 EXECUÇÃO RÁPIDA (Quick Start)

```bash
# 1. Clone o repositório
git clone https://github.com/thiagobjcarvalho-cw/data-science.git
cd data-science

# 2. Crie ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute os notebooks
cd prova-aedi-unb/notebooks
jupyter notebook

# 5. Ou execute diretamente
python -m jupyter nbconvert --to notebook --execute Q1_Regressao_Linear.ipynb
python -m jupyter nbconvert --to notebook --execute Q2_Regressao_Logistica.ipynb
python -m jupyter nbconvert --to notebook --execute Q3_ANOVA.ipynb
python -m jupyter nbconvert --to notebook --execute Q4_ML_Avancado.ipynb

# 6. Gere HTML para entrega
python -m jupyter nbconvert --to html Q1_Regressao_Linear.ipynb
python -m jupyter nbconvert --to html Q2_Regressao_Logistica.ipynb
python -m jupyter nbconvert --to html Q3_ANOVA.ipynb
python -m jupyter nbconvert --to html Q4_ML_Avancado.ipynb
```

---

## 📁 ESTRUTURA DO PROJETO

```
data-science/
├── prova-aedi-unb/
│   ├── dados/                      # Datasets
│   │   ├── king_county_houses.csv  # Q1
│   │   ├── hotel_bookings.csv      # Q2
│   │   ├── online_retail.csv       # Q3
│   │   └── german_credit.csv       # Q4
│   ├── notebooks/                  # Notebooks da prova
│   │   ├── Q1_Regressao_Linear.ipynb
│   │   ├── Q2_Regressao_Logistica.ipynb
│   │   ├── Q3_ANOVA.ipynb
│   │   └── Q4_ML_Avancado.ipynb
│   └── exports/                    # HTMLs gerados (entrega)
├── material-base/                  # Material original
│   └── Prova.pdf                  # Enunciado oficial
└── requirements.txt                # Dependências Python
```

---

## ⚙️ PRÉ-REQUISITOS

### Software Necessário

- **Python 3.8+** (recomendado 3.11)
- **pip** (gerenciador de pacotes Python)
- **Jupyter Notebook ou JupyterLab**

### Instalação do Python

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### macOS
```bash
brew install python@3.11
```

#### Windows
Baixe de: https://www.python.org/downloads/

---

## 📦 INSTALAÇÃO DE DEPENDÊNCIAS

### Método 1: requirements.txt (Recomendado)

```bash
pip install -r requirements.txt
```

### Método 2: Instalação Manual

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels xgboost lightgbm shap jupyter nbconvert openpyxl
```

### Verificar Instalação

```python
python3 << EOF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import scipy
import statsmodels
import xgboost
import lightgbm
import shap
print("✅ Todas as dependências instaladas com sucesso!")
EOF
```

---

## 📊 EXECUÇÃO DOS NOTEBOOKS

### Opção 1: Jupyter Notebook (Interface Gráfica)

```bash
cd prova-aedi-unb/notebooks
jupyter notebook
```

**Passos:**
1. Browser abrirá automaticamente
2. Clique no notebook desejado (Q1, Q2, Q3 ou Q4)
3. Execute: `Cell > Run All` ou `Shift + Enter` célula por célula
4. Exporte: `File > Download as > HTML`

### Opção 2: Linha de Comando (Automatizado)

```bash
cd prova-aedi-unb/notebooks

# Executar e gerar HTML em um comando
jupyter nbconvert --to html --execute Q1_Regressao_Linear.ipynb --output ../exports/Q1_Regressao_Linear.html
jupyter nbconvert --to html --execute Q2_Regressao_Logistica.ipynb --output ../exports/Q2_Regressao_Logistica.html
jupyter nbconvert --to html --execute Q3_ANOVA.ipynb --output ../exports/Q3_ANOVA.html
jupyter nbconvert --to html --execute Q4_ML_Avancado.ipynb --output ../exports/Q4_ML_Avancado.html
```

### Opção 3: Script Automatizado

```bash
#!/bin/bash
# execute_all.sh

cd prova-aedi-unb/notebooks

for notebook in Q1_Regressao_Linear Q2_Regressao_Logistica Q3_ANOVA Q4_ML_Avancado; do
    echo "Executando ${notebook}.ipynb..."
    jupyter nbconvert --to html --execute ${notebook}.ipynb --output ../exports/${notebook}.html

    if [ $? -eq 0 ]; then
        echo "✅ ${notebook} concluído!"
    else
        echo "❌ Erro em ${notebook}"
    fi
done

echo "🎉 Todos os notebooks executados!"
```

Tornar executável e rodar:
```bash
chmod +x execute_all.sh
./execute_all.sh
```

---

## 🔍 DETALHES POR QUESTÃO

### **Questão 1: Regressão Linear (2.5 pts)**

**Arquivo:** `Q1_Regressao_Linear.ipynb`
**Dataset:** `king_county_houses.csv`
**Tempo estimado:** 15-20 minutos de execução

**Principais Análises:**
- ✅ EDA completo (estatísticas descritivas, correlações)
- ✅ Modelo OLS (statsmodels)
- ✅ Validação de TODOS os pressupostos:
  - Linearidade
  - Homocedasticidade (Breusch-Pagan)
  - Normalidade (Shapiro-Wilk, Q-Q Plot)
  - Multicolinearidade (VIF)
  - Independência (Durbin-Watson)
- ✅ Transformação logarítmica (se necessário)
- ✅ Comparação de modelos

**Métricas Esperadas:**
- R² Test: ~0.50-0.65
- RMSE: ~$100k-150k

---

### **Questão 2: Regressão Logística (2.5 pts)**

**Arquivo:** `Q2_Regressao_Logistica.ipynb`
**Dataset:** `hotel_bookings.csv`
**Tempo estimado:** 10-15 minutos

**Principais Análises:**
- ✅ Análise de balanceamento (target: is_canceled)
- ✅ Preprocessing (encoding, scaling)
- ✅ Modelo Logístico (sklearn)
- ✅ Métricas: Accuracy, Precision, Recall, F1, AUC-ROC
- ✅ Matriz de confusão + interpretação
- ✅ Curva ROC
- ✅ Feature importance (coeficientes + odds ratio)
- ✅ Justificativa vs Regressão Linear

**Métricas Esperadas:**
- AUC-ROC: ~0.75-0.85
- F1-Score: ~0.70-0.80

---

### **Questão 3: ANOVA (2.0 pts)**

**Arquivo:** `Q3_ANOVA.ipynb`
**Dataset:** `online_retail.csv`
**Tempo estimado:** 10-12 minutos

**Principais Análises:**
- ✅ Comparação de médias entre países (Quantity e UnitPrice)
- ✅ One-way ANOVA (scipy.stats.f_oneway)
- ✅ Validação de pressupostos:
  - Normalidade por grupo (Shapiro-Wilk)
  - Homocedasticidade (Levene)
- ✅ Correções se necessário (log ou Kruskal-Wallis)
- ✅ Post-hoc: Tukey HSD (se ANOVA significativa)
- ✅ Interpretação de negócio

**Resultado Esperado:**
- p-value < 0.05 (diferenças significativas entre países)

---

### **Questão 4: ML Avançado + SHAP + Clustering (3.0 pts)**

**Arquivo:** `Q4_ML_Avancado.ipynb`
**Dataset:** `german_credit.csv`
**Tempo estimado:** 25-35 minutos ⏰ **MAIS LONGA**

**Principais Análises:**
- ✅ Discussão acadêmica do problema de crédito
- ✅ EDA completo + feature engineering
- ✅ **5 modelos treinados:**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - XGBoost
  - LightGBM
- ✅ Comparação de métricas (tabela + gráficos)
- ✅ **SHAP Values (25% da nota Q4!):**
  - Summary plot (dot + bar)
  - Dependence plots (top 3 features)
  - Force plots (2 casos: good/bad)
  - **Interpretação acadêmica completa**
- ✅ **Clustering:**
  - K-Means (Elbow + Silhouette)
  - DBSCAN (detecção de outliers)
  - Perfis de clusters
  - Comparação K-Means vs DBSCAN
- ✅ Decisão estratégica bancária

**Métricas Esperadas:**
- Melhor modelo AUC: ~0.75-0.85
- Clusters: 3-4 segmentos

---

## 📤 GERAÇÃO DE ENTREGAS (HTML)

### Método Manual (Jupyter Interface)

1. Abra o notebook
2. Execute `Cell > Run All`
3. Aguarde execução completa
4. `File > Download as > HTML (.html)`
5. Salve em `prova-aedi-unb/exports/`

### Método Automático (Recomendado)

```bash
cd prova-aedi-unb/notebooks

# Criar pasta de exports
mkdir -p ../exports

# Executar e converter
jupyter nbconvert --to html --execute Q1_Regressao_Linear.ipynb --output ../exports/Q1_Regressao_Linear.html
jupyter nbconvert --to html --execute Q2_Regressao_Logistica.ipynb --output ../exports/Q2_Regressao_Logistica.html
jupyter nbconvert --to html --execute Q3_ANOVA.ipynb --output ../exports/Q3_ANOVA.html
jupyter nbconvert --to html --execute Q4_ML_Avancado.ipynb --output ../exports/Q4_ML_Avancado.html
```

### Verificar HTMLs Gerados

```bash
ls -lh prova-aedi-unb/exports/
```

**Tamanhos esperados:**
- Q1: ~1-2 MB
- Q2: ~1.5-2.5 MB
- Q3: ~1-1.5 MB
- Q4: ~3-5 MB (contém muitos gráficos SHAP)

---

## 🐛 TROUBLESHOOTING

### Erro: `ModuleNotFoundError`

**Problema:** Biblioteca não instalada
**Solução:**
```bash
pip install [nome_da_biblioteca]
# ou
pip install -r requirements.txt --upgrade
```

### Erro: `FileNotFoundError` (Dataset)

**Problema:** Caminho para dados incorreto
**Solução:**
```python
# Nos notebooks, os caminhos são relativos:
df = pd.read_csv('../dados/king_county_houses.csv')

# Certifique-se de estar em prova-aedi-unb/notebooks/
```

### Erro: `MemoryError` (Q4 - SHAP)

**Problema:** SHAP consome muita memória
**Solução:** Reduzir amostra no notebook
```python
# Em Q4, trocar:
shap_values = explainer(X_test)  # ORIGINAL
# Para:
shap_values = explainer(X_test[:100])  # REDUZIDO
```

### Erro: Jupyter não abre

**Solução:**
```bash
# Reinstalar Jupyter
pip install --upgrade jupyter notebook

# Ou usar JupyterLab
pip install jupyterlab
jupyter lab
```

### Erro: Gráficos não aparecem

**Solução:** Adicionar no início do notebook:
```python
%matplotlib inline
import matplotlib.pyplot as plt
```

### Warning: `FutureWarning` ou `DeprecationWarning`

**Não é erro!** Avisos sobre versões futuras. Pode ignorar ou suprimir:
```python
import warnings
warnings.filterwarnings('ignore')
```

---

## ⏱️ TEMPO TOTAL DE EXECUÇÃO

| Questão | Notebook | Execução | Total |
|---------|----------|----------|-------|
| Q1 | Regressão Linear | ~15-20 min | ~15-20 min |
| Q2 | Regressão Logística | ~10-15 min | ~10-15 min |
| Q3 | ANOVA | ~10-12 min | ~10-12 min |
| Q4 | ML Avançado + SHAP | ~25-35 min | ~25-35 min |
| **TOTAL** | - | **~60-82 min** | **~1h-1h22** |

**Obs:** Tempos em máquina com:
- CPU: 4+ cores
- RAM: 8+ GB
- SSD

---

## ✅ CHECKLIST FINAL

Antes de entregar, verifique:

- [ ] Todos os 4 notebooks executaram sem erros
- [ ] Todos os gráficos foram renderizados
- [ ] HTMLs foram gerados em `prova-aedi-unb/exports/`
- [ ] HTMLs abrem corretamente no browser
- [ ] Todos os pressupostos foram validados (Q1 e Q3)
- [ ] SHAP values foram calculados e interpretados (Q4)
- [ ] Clustering foi executado (Q4)
- [ ] Interpretações acadêmicas estão presentes
- [ ] Decisões de negócio foram incluídas

---

## 📚 RECURSOS ADICIONAIS

### Documentação

- **Prova Oficial:** `material-base/Prova.pdf`
- **Especificações Detalhadas:** `prova-aedi-pacote/questoes/`
- **Skill Data Science:** `skill/SKILL.md`

### Datasets Alternativos (se necessário)

- **Q1:** https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
- **Q2:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
- **Q3:** https://archive.ics.uci.edu/ml/datasets/Online+Retail
- **Q4:** https://www.kaggle.com/datasets/uciml/german-credit

### Bibliotecas - Documentação Oficial

- pandas: https://pandas.pydata.org/docs/
- scikit-learn: https://scikit-learn.org/
- statsmodels: https://www.statsmodels.org/
- SHAP: https://shap.readthedocs.io/

---

## 🎯 DICAS FINAIS

1. **Execute em ordem:** Q1 → Q2 → Q3 → Q4
2. **Q4 é a mais importante:** Vale 3.0 pontos (30% da prova)
3. **Pressupostos são críticos:** Q1 e Q3 exigem validação formal
4. **SHAP é obrigatório:** 25% da nota de Q4 (0.75 pts)
5. **Salve frequentemente:** `Ctrl+S` no Jupyter
6. **Teste antes de entregar:** Abra os HTMLs e revise

---

## 📞 SUPORTE

Em caso de dúvidas ou problemas:

1. Verifique a seção **TROUBLESHOOTING** acima
2. Consulte os arquivos de especificação em `prova-aedi-pacote/questoes/`
3. Verifique logs de erro no terminal

---

**Boa sorte na prova! 🎓**

**Versão:** 1.0
**Última atualização:** 23/11/2025
