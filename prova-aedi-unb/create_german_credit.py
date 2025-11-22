#!/usr/bin/env python3
"""
Gera dataset sintético German Credit com estrutura realista
Dataset: 1000 linhas, 21 colunas
Uso: python create_german_credit.py
"""

import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

print("Gerando German Credit Dataset sintético...")

df = pd.DataFrame()

# Variáveis categóricas
df['checking_status'] = np.random.choice(
    ['<0', '0<=X<200', '>=200', 'no checking'],
    n, p=[0.27, 0.27, 0.06, 0.40]
)

df['credit_history'] = np.random.choice(
    ['no credits/all paid', 'all paid', 'existing paid', 'delayed previously', 'critical/other existing credit'],
    n, p=[0.04, 0.05, 0.53, 0.09, 0.29]
)

df['purpose'] = np.random.choice(
    ['new car', 'used car', 'furniture/equipment', 'radio/tv', 'domestic appliances',
     'repairs', 'education', 'vacation', 'retraining', 'business', 'other'],
    n, p=[0.23, 0.10, 0.18, 0.28, 0.01, 0.02, 0.05, 0.01, 0.01, 0.10, 0.01]
)

df['savings_status'] = np.random.choice(
    ['<100', '100<=X<500', '500<=X<1000', '>=1000', 'no known savings'],
    n, p=[0.60, 0.10, 0.06, 0.05, 0.19]
)

df['employment'] = np.random.choice(
    ['unemployed', '<1', '1<=X<4', '4<=X<7', '>=7'],
    n, p=[0.06, 0.17, 0.34, 0.17, 0.26]
)

df['personal_status'] = np.random.choice(
    ['male div/sep', 'female div/sep/mar', 'male single', 'male mar/wid', 'female single'],
    n, p=[0.05, 0.31, 0.55, 0.09, 0.00]
)

df['other_parties'] = np.random.choice(
    ['none', 'co applicant', 'guarantor'],
    n, p=[0.91, 0.04, 0.05]
)

df['property_magnitude'] = np.random.choice(
    ['real estate', 'life insurance', 'car', 'no known property'],
    n, p=[0.28, 0.23, 0.33, 0.16]
)

df['other_payment_plans'] = np.random.choice(
    ['bank', 'stores', 'none'],
    n, p=[0.19, 0.05, 0.76]
)

df['housing'] = np.random.choice(
    ['rent', 'own', 'for free'],
    n, p=[0.18, 0.71, 0.11]
)

df['job'] = np.random.choice(
    ['unemp/unskilled non res', 'unskilled resident', 'skilled', 'high qualif/self emp/mgmt'],
    n, p=[0.02, 0.20, 0.63, 0.15]
)

df['telephone'] = np.random.choice(
    ['none', 'yes'],
    n, p=[0.60, 0.40]
)

df['foreign_worker'] = np.random.choice(
    ['yes', 'no'],
    n, p=[0.96, 0.04]
)

# Variáveis numéricas
df['duration'] = np.random.randint(4, 73, n)
df['credit_amount'] = np.random.randint(250, 18500, n)
df['installment_commitment'] = np.random.randint(1, 5, n)
df['residence_since'] = np.random.randint(1, 5, n)
df['age'] = np.random.randint(19, 76, n)
df['existing_credits'] = np.random.randint(1, 5, n)
df['num_dependents'] = np.random.choice([1, 2], n, p=[0.85, 0.15])

# Criar variável target com correlações realistas
risk_score = (
    (df['checking_status'] == '<0').astype(int) * 0.3 +
    (df['credit_history'] == 'critical/other existing credit').astype(int) * 0.25 +
    (df['duration'] > 24).astype(int) * 0.15 +
    (df['savings_status'] == '<100').astype(int) * 0.10 +
    (df['age'] < 25).astype(int) * 0.05 +
    (df['credit_amount'] > 5000).astype(int) * 0.10 +
    np.random.uniform(-0.2, 0.2, n)
)

threshold = np.percentile(risk_score, 70)
df['class'] = np.where(risk_score > threshold, 'bad', 'good')

# Salvar
output_path = 'dados/german_credit.csv'
df.to_csv(output_path, index=False)

print(f"✓ Dataset salvo em: {output_path}")
print(f"✓ Shape: {df.shape}")
print(f"✓ Distribuição target: {df['class'].value_counts().to_dict()}")
print(f"✓ Colunas: {list(df.columns)}")
