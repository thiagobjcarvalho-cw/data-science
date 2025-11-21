# 📊 FONTES DOS DATASETS

## QUESTÃO 1: King County House Sales

### Opção 1: Kaggle
**URL:** https://www.kaggle.com/datasets/harlfoxem/housesalesprediction  
**Comando:**
```bash
kaggle datasets download -d harlfoxem/housesalesprediction
unzip housesalesprediction.zip -d dados/
```

### Opção 2: GitHub (Raw)
**URL:** https://raw.githubusercontent.com/datasciencedojo/datasets/master/kc_house_data.csv  
**Comando:**
```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/kc_house_data.csv')
```

### Opção 3: Kaggle API alternativa
```python
!pip install kaggle
!kaggle datasets download -d harlfoxem/housesalesprediction
```

---

## QUESTÃO 2: Hotel Booking Demand

### Opção 1: Kaggle
**URL:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand  
**Comando:**
```bash
kaggle datasets download -d jessemostipak/hotel-booking-demand
```

### Opção 2: TidyTuesday (GitHub)
**URL:** https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv  
**Comando:**
```python
df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
```

### Opção 3: Kaggle Direct
```python
import kaggle
kaggle.api.dataset_download_files('jessemostipak/hotel-booking-demand', path='dados/', unzip=True)
```

---

## QUESTÃO 3: Online Retail

### Opção 1: UCI ML Repository (Original)
**URL:** http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx  
**Comando:**
```python
df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
```

### Opção 2: Kaggle
**URL:** https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset  
**Comando:**
```bash
kaggle datasets download -d lakshmi25npathi/online-retail-dataset
```

### Opção 3: Mirror (se UCI estiver fora)
**URL:** https://github.com/stedy/Machine-Learning-with-R-datasets/raw/master/OnlineRetail.csv  
**Comando:**
```python
df = pd.read_csv('https://github.com/stedy/Machine-Learning-with-R-datasets/raw/master/OnlineRetail.csv')
```

---

## QUESTÃO 4: German Credit Risk

### Opção 1: sklearn (mais fácil)
```python
from sklearn.datasets import fetch_openml
credit = fetch_openml('credit-g', version=1, as_frame=True, parser='auto')
df = credit.frame
```

### Opção 2: UCI ML Repository
**URL:** https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)  
**Arquivo:** german.data (formato fixo)  
**Comando:**
```python
# Nomes das colunas
columns = ['checking_status', 'duration', 'credit_history', 'purpose', 'credit_amount',
           'savings_status', 'employment', 'installment_rate', 'personal_status',
           'other_parties', 'residence_since', 'property_magnitude', 'age',
           'other_payment_plans', 'housing', 'existing_credits', 'job',
           'num_dependents', 'own_telephone', 'foreign_worker', 'class']

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data',
                 sep=' ', header=None, names=columns)
```

### Opção 3: Kaggle
**URL:** https://www.kaggle.com/datasets/uciml/german-credit  
**Comando:**
```bash
kaggle datasets download -d uciml/german-credit
```

---

## 🔧 CONFIGURAÇÃO KAGGLE API

Se necessário usar Kaggle API:

### 1. Obter API Token
- Ir para https://www.kaggle.com/settings
- Clicar em "Create New API Token"
- Baixar kaggle.json

### 2. Configurar no ambiente
```bash
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### 3. Instalar biblioteca
```bash
pip install kaggle
```

---

## 📥 DOWNLOAD AUTOMÁTICO (Script)

Criar script `download_all_datasets.py`:

```python
import pandas as pd
import os

# Criar diretório
os.makedirs('dados', exist_ok=True)

# Q1: King County
try:
    df1 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/kc_house_data.csv')
    df1.to_csv('dados/king_county_houses.csv', index=False)
    print("✅ Q1 dataset baixado")
except Exception as e:
    print(f"❌ Q1 erro: {e}")

# Q2: Hotel Booking
try:
    df2 = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
    df2.to_csv('dados/hotel_bookings.csv', index=False)
    print("✅ Q2 dataset baixado")
except Exception as e:
    print(f"❌ Q2 erro: {e}")

# Q3: Online Retail
try:
    df3 = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
    df3.to_csv('dados/online_retail.csv', index=False)
    print("✅ Q3 dataset baixado")
except Exception as e:
    print(f"❌ Q3 erro: {e}")

# Q4: German Credit
try:
    from sklearn.datasets import fetch_openml
    credit = fetch_openml('credit-g', version=1, as_frame=True, parser='auto')
    credit.frame.to_csv('dados/german_credit.csv', index=False)
    print("✅ Q4 dataset baixado")
except Exception as e:
    print(f"❌ Q4 erro: {e}")

print("\n✅ DOWNLOAD CONCLUÍDO!")
```

---

## 🚨 TROUBLESHOOTING

### Erro: "kaggle: command not found"
```bash
pip install kaggle --user
export PATH=$PATH:~/.local/bin
```

### Erro: "401 Unauthorized" (Kaggle)
- Verificar se kaggle.json está em ~/.kaggle/
- Verificar permissões: `chmod 600 ~/.kaggle/kaggle.json`

### Erro: "SSL Certificate" (UCI)
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

### Erro: "openpyxl not installed"
```bash
pip install openpyxl
```

---

## 📝 NOTAS

- **Prioridade:** sklearn > GitHub > UCI > Kaggle
- **sklearn** é mais confiável (datasets hospedados na infraestrutura deles)
- **GitHub raw** geralmente funciona sem autenticação
- **Kaggle** requer API key (mais burocrático)
- **UCI** às vezes fica offline (usar mirrors)

---

## ✅ VALIDAÇÃO

Após download, verificar:
```python
import os
print(f"Q1: {os.path.exists('dados/king_county_houses.csv')}")
print(f"Q2: {os.path.exists('dados/hotel_bookings.csv')}")
print(f"Q3: {os.path.exists('dados/online_retail.csv')}")
print(f"Q4: {os.path.exists('dados/german_credit.csv')}")
```

Se todos True: ✅ Pronto para começar!
