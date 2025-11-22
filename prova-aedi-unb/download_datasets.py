#!/usr/bin/env python3
"""
Download de datasets com múltiplas fontes fallback
Datasets: King County, Hotel Bookings, Online Retail, German Credit
Uso: python download_datasets.py
"""

import pandas as pd
import numpy as np
import os

# Criar diretório de dados
os.makedirs('dados', exist_ok=True)

np.random.seed(42)

print("="*60)
print("DOWNLOAD E GERAÇÃO DE DATASETS")
print("="*60)

# ========================================
# DATASET 1: King County Houses
# ========================================
print("\n[1/4] King County Houses...")

king_county_urls = [
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/kc_house_data.csv',
    'https://gist.githubusercontent.com/anonymous/raw/kc_house_data.csv',
]

df_king = None
for url in king_county_urls:
    try:
        print(f"  Tentando: {url[:50]}...")
        df_king = pd.read_csv(url)
        print(f"  ✓ Download bem-sucedido!")
        break
    except Exception as e:
        print(f"  ✗ Falha: {str(e)[:50]}")
        continue

if df_king is None:
    print("  → Gerando dataset sintético...")
    n = 21613
    df_king = pd.DataFrame({
        'price': np.random.lognormal(13, 0.7, n),
        'bedrooms': np.random.randint(1, 11, n),
        'bathrooms': np.random.uniform(0.5, 8, n),
        'sqft_living': np.random.randint(370, 13540, n),
        'sqft_lot': np.random.randint(520, 1651359, n),
        'floors': np.random.choice([1, 1.5, 2, 2.5, 3, 3.5], n),
        'waterfront': np.random.choice([0, 1], n, p=[0.99, 0.01]),
        'view': np.random.randint(0, 5, n),
        'condition': np.random.randint(1, 6, n),
        'grade': np.random.randint(3, 14, n),
        'sqft_above': np.random.randint(370, 9410, n),
        'sqft_basement': np.random.randint(0, 4820, n),
        'yr_built': np.random.randint(1900, 2016, n),
        'yr_renovated': np.random.choice([0] + list(range(1934, 2016)), n),
        'zipcode': np.random.randint(98001, 98200, n),
        'lat': np.random.uniform(47.1, 47.8, n),
        'long': np.random.uniform(-122.6, -121.3, n),
        'sqft_living15': np.random.randint(399, 6210, n),
        'sqft_lot15': np.random.randint(651, 871200, n),
    })

df_king.to_csv('dados/king_county_houses.csv', index=False)
print(f"  ✓ Salvo: dados/king_county_houses.csv ({df_king.shape})")

# ========================================
# DATASET 2: Hotel Bookings
# ========================================
print("\n[2/4] Hotel Bookings...")

hotel_urls = [
    'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotel_bookings.csv',
]

df_hotel = None
for url in hotel_urls:
    try:
        print(f"  Tentando: {url[:50]}...")
        df_hotel = pd.read_csv(url)
        print(f"  ✓ Download bem-sucedido!")
        break
    except Exception as e:
        print(f"  ✗ Falha: {str(e)[:50]}")
        continue

if df_hotel is None:
    print("  → Gerando dataset sintético...")
    n = 119390
    df_hotel = pd.DataFrame({
        'hotel': np.random.choice(['Resort Hotel', 'City Hotel'], n),
        'is_canceled': np.random.choice([0, 1], n, p=[0.63, 0.37]),
        'lead_time': np.random.randint(0, 738, n),
        'arrival_date_year': np.random.choice([2015, 2016, 2017], n),
        'arrival_date_month': np.random.choice(['January', 'February', 'March', 'April', 'May', 'June',
                                                 'July', 'August', 'September', 'October', 'November', 'December'], n),
        'arrival_date_week_number': np.random.randint(1, 54, n),
        'arrival_date_day_of_month': np.random.randint(1, 32, n),
        'stays_in_weekend_nights': np.random.randint(0, 20, n),
        'stays_in_week_nights': np.random.randint(0, 51, n),
        'adults': np.random.randint(0, 5, n),
        'children': np.random.choice([0, 1, 2, 3], n, p=[0.90, 0.05, 0.03, 0.02]),
        'babies': np.random.choice([0, 1, 2], n, p=[0.95, 0.04, 0.01]),
        'meal': np.random.choice(['BB', 'FB', 'HB', 'SC', 'Undefined'], n),
        'country': np.random.choice(['PRT', 'GBR', 'FRA', 'ESP', 'DEU', 'ITA', 'BRA', 'USA'], n),
        'market_segment': np.random.choice(['Direct', 'Corporate', 'Online TA', 'Offline TA/TO', 'Groups', 'Complementary', 'Aviation'], n),
        'distribution_channel': np.random.choice(['Direct', 'Corporate', 'TA/TO', 'GDS'], n),
        'is_repeated_guest': np.random.choice([0, 1], n, p=[0.97, 0.03]),
        'previous_cancellations': np.random.randint(0, 27, n),
        'previous_bookings_not_canceled': np.random.randint(0, 73, n),
        'reserved_room_type': np.random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L'], n),
        'assigned_room_type': np.random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L'], n),
        'booking_changes': np.random.randint(0, 22, n),
        'deposit_type': np.random.choice(['No Deposit', 'Refundable', 'Non Refund'], n, p=[0.88, 0.01, 0.11]),
        'agent': np.random.choice([np.nan, 1, 9, 240, 14, 7, 6, 1], n, p=[0.86, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01]),
        'company': np.random.choice([np.nan, 40, 223, 67, 45], n, p=[0.94, 0.02, 0.01, 0.02, 0.01]),
        'days_in_waiting_list': np.random.randint(0, 392, n),
        'customer_type': np.random.choice(['Transient', 'Contract', 'Transient-Party', 'Group'], n),
        'adr': np.random.uniform(0, 5400, n),
        'required_car_parking_spaces': np.random.choice([0, 1, 2, 3], n, p=[0.92, 0.06, 0.015, 0.005]),
        'total_of_special_requests': np.random.randint(0, 6, n),
        'reservation_status': np.random.choice(['Check-Out', 'Canceled', 'No-Show'], n),
        'reservation_status_date': pd.date_range('2015-01-01', periods=n, freq='H').astype(str),
    })

df_hotel.to_csv('dados/hotel_bookings.csv', index=False)
print(f"  ✓ Salvo: dados/hotel_bookings.csv ({df_hotel.shape})")

# ========================================
# DATASET 3: Online Retail
# ========================================
print("\n[3/4] Online Retail...")

print("  → Gerando dataset sintético...")
n = 50000
countries = ['United Kingdom', 'Germany', 'France', 'EIRE', 'Spain', 'Netherlands', 'Belgium',
             'Switzerland', 'Portugal', 'Australia', 'Norway', 'Italy', 'Channel Islands',
             'Finland', 'Cyprus', 'Sweden', 'Austria', 'Denmark', 'Poland', 'Japan']

df_retail = pd.DataFrame({
    'InvoiceNo': [f'{i}' for i in range(100000, 100000+n)],
    'StockCode': [f'{np.random.randint(10000, 99999)}' for _ in range(n)],
    'Description': [f'Product_{np.random.randint(1, 1000)}' for _ in range(n)],
    'Quantity': np.random.randint(1, 1201, n),
    'InvoiceDate': pd.date_range('2010-12-01', periods=n, freq='H').astype(str),
    'UnitPrice': np.random.uniform(0.01, 1000, n),
    'CustomerID': np.random.randint(12000, 20000, n),
    'Country': np.random.choice(countries, n, p=[0.91] + [0.09/(len(countries)-1)]*(len(countries)-1))
})

df_retail['TotalPrice'] = df_retail['Quantity'] * df_retail['UnitPrice']

df_retail.to_csv('dados/online_retail.csv', index=False)
print(f"  ✓ Salvo: dados/online_retail.csv ({df_retail.shape})")

# ========================================
# DATASET 4: German Credit
# ========================================
print("\n[4/4] German Credit...")
print("  → Executando create_german_credit.py...")

try:
    exec(open('create_german_credit.py').read())
except Exception as e:
    print(f"  ✗ Erro ao executar script: {e}")
    print("  → Executando geração inline...")
    import create_german_credit
    print("  ✓ German Credit gerado via import")

print("\n" + "="*60)
print("RESUMO")
print("="*60)

for filename in ['king_county_houses.csv', 'hotel_bookings.csv', 'online_retail.csv', 'german_credit.csv']:
    filepath = f'dados/{filename}'
    if os.path.exists(filepath):
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        df_temp = pd.read_csv(filepath)
        print(f"✓ {filename:30s} | {df_temp.shape[0]:7d} linhas | {size_mb:5.1f} MB")
    else:
        print(f"✗ {filename:30s} | NÃO ENCONTRADO")

print("="*60)
print("Concluído!")
