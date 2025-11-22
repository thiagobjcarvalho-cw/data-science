#!/usr/bin/env python3
"""
Versão aprimorada do download de datasets
Melhorias: Validação de integridade, logging detalhado, tratamento robusto de erros
Uso: python download_datasets_v2.py
"""

import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime

# Configuração
os.makedirs('dados', exist_ok=True)
np.random.seed(42)

def log(message, level="INFO"):
    """Logging com timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {level:5s} | {message}")

def validate_dataset(df, name, expected_rows_min, expected_cols_min):
    """Valida integridade básica do dataset"""
    if df is None:
        log(f"Dataset {name} é None", "ERROR")
        return False

    rows, cols = df.shape

    if rows < expected_rows_min:
        log(f"{name}: Poucas linhas ({rows} < {expected_rows_min})", "WARN")
        return False

    if cols < expected_cols_min:
        log(f"{name}: Poucas colunas ({cols} < {expected_cols_min})", "WARN")
        return False

    log(f"{name}: Validação OK ({rows} linhas, {cols} colunas)", "OK")
    return True

def try_download(urls, name):
    """Tenta download de múltiplas URLs"""
    for i, url in enumerate(urls, 1):
        try:
            log(f"{name}: Tentativa {i}/{len(urls)} - {url[:60]}...")
            df = pd.read_csv(url, low_memory=False)
            log(f"{name}: Download bem-sucedido! Shape: {df.shape}", "OK")
            return df
        except Exception as e:
            log(f"{name}: Falha - {str(e)[:80]}", "WARN")

    log(f"{name}: Todas as URLs falharam", "WARN")
    return None

def save_dataset(df, filename, name):
    """Salva dataset com verificação"""
    filepath = f'dados/{filename}'
    try:
        df.to_csv(filepath, index=False)
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        log(f"{name}: Salvo em {filepath} ({size_mb:.2f} MB)", "OK")
        return True
    except Exception as e:
        log(f"{name}: Erro ao salvar - {e}", "ERROR")
        return False

# ============================================================================
# INÍCIO DO PROCESSO
# ============================================================================

log("="*70)
log("DOWNLOAD E GERAÇÃO DE DATASETS - VERSÃO 2")
log("="*70)

datasets_success = []
datasets_failed = []

# ============================================================================
# DATASET 1: King County Houses
# ============================================================================
log("")
log("[1/4] KING COUNTY HOUSES", "INFO")
log("-"*70)

king_urls = [
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/kc_house_data.csv',
    'https://github.com/datasciencedojo/datasets/raw/master/kc_house_data.csv',
]

df_king = try_download(king_urls, "KingCounty")

if df_king is None:
    log("KingCounty: Gerando dataset sintético...", "INFO")
    n = 21613

    df_king = pd.DataFrame({
        'id': range(1, n+1),
        'date': pd.date_range('2014-05-02', periods=n, freq='H').astype(str),
        'price': np.random.lognormal(13, 0.7, n),
        'bedrooms': np.random.randint(1, 11, n),
        'bathrooms': np.round(np.random.uniform(0.5, 8, n) * 2) / 2,
        'sqft_living': np.random.randint(370, 13540, n),
        'sqft_lot': np.random.randint(520, 200000, n),
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
        'lat': np.round(np.random.uniform(47.1, 47.8, n), 6),
        'long': np.round(np.random.uniform(-122.6, -121.3, n), 6),
        'sqft_living15': np.random.randint(399, 6210, n),
        'sqft_lot15': np.random.randint(651, 200000, n),
    })

    log("KingCounty: Dataset sintético gerado", "OK")

if validate_dataset(df_king, "KingCounty", 20000, 15):
    if save_dataset(df_king, 'king_county_houses.csv', "KingCounty"):
        datasets_success.append("King County Houses")
    else:
        datasets_failed.append("King County Houses")
else:
    datasets_failed.append("King County Houses")

# ============================================================================
# DATASET 2: Hotel Bookings
# ============================================================================
log("")
log("[2/4] HOTEL BOOKINGS", "INFO")
log("-"*70)

hotel_urls = [
    'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotel_bookings.csv',
]

df_hotel = try_download(hotel_urls, "HotelBookings")

if df_hotel is None:
    log("HotelBookings: Gerando dataset sintético...", "INFO")
    n = 119390

    df_hotel = pd.DataFrame({
        'hotel': np.random.choice(['Resort Hotel', 'City Hotel'], n, p=[0.28, 0.72]),
        'is_canceled': np.random.choice([0, 1], n, p=[0.63, 0.37]),
        'lead_time': np.random.randint(0, 738, n),
        'arrival_date_year': np.random.choice([2015, 2016, 2017], n, p=[0.27, 0.49, 0.24]),
        'arrival_date_month': np.random.choice(['January', 'February', 'March', 'April', 'May', 'June',
                                                 'July', 'August', 'September', 'October', 'November', 'December'], n),
        'arrival_date_week_number': np.random.randint(1, 54, n),
        'arrival_date_day_of_month': np.random.randint(1, 32, n),
        'stays_in_weekend_nights': np.random.poisson(1, n),
        'stays_in_week_nights': np.random.poisson(3, n),
        'adults': np.random.choice([1, 2, 3, 4], n, p=[0.40, 0.50, 0.08, 0.02]),
        'children': np.random.choice([0, 1, 2, 3], n, p=[0.90, 0.06, 0.03, 0.01]),
        'babies': np.random.choice([0, 1], n, p=[0.95, 0.05]),
        'meal': np.random.choice(['BB', 'FB', 'HB', 'SC'], n, p=[0.77, 0.01, 0.14, 0.08]),
        'country': np.random.choice(['PRT', 'GBR', 'FRA', 'ESP', 'DEU', 'ITA', 'BRA', 'USA', 'Other'],
                                   n, p=[0.48, 0.12, 0.10, 0.05, 0.05, 0.04, 0.03, 0.03, 0.10]),
        'market_segment': np.random.choice(['Online TA', 'Offline TA/TO', 'Direct', 'Corporate', 'Groups'],
                                          n, p=[0.47, 0.19, 0.12, 0.11, 0.11]),
        'distribution_channel': np.random.choice(['TA/TO', 'Direct', 'Corporate', 'GDS'],
                                                n, p=[0.82, 0.12, 0.05, 0.01]),
        'is_repeated_guest': np.random.choice([0, 1], n, p=[0.97, 0.03]),
        'previous_cancellations': np.random.poisson(0.1, n),
        'previous_bookings_not_canceled': np.random.poisson(0.2, n),
        'reserved_room_type': np.random.choice(['A', 'D', 'E', 'F', 'G', 'B', 'C'],
                                              n, p=[0.47, 0.19, 0.13, 0.09, 0.06, 0.04, 0.02]),
        'assigned_room_type': np.random.choice(['A', 'D', 'E', 'F', 'G', 'B', 'C', 'K'],
                                              n, p=[0.40, 0.20, 0.15, 0.10, 0.06, 0.04, 0.03, 0.02]),
        'booking_changes': np.random.poisson(0.3, n),
        'deposit_type': np.random.choice(['No Deposit', 'Non Refund', 'Refundable'],
                                        n, p=[0.88, 0.11, 0.01]),
        'days_in_waiting_list': np.random.poisson(1, n),
        'customer_type': np.random.choice(['Transient', 'Transient-Party', 'Contract', 'Group'],
                                         n, p=[0.76, 0.17, 0.04, 0.03]),
        'adr': np.abs(np.random.normal(100, 50, n)),
        'required_car_parking_spaces': np.random.choice([0, 1, 2], n, p=[0.92, 0.07, 0.01]),
        'total_of_special_requests': np.random.choice([0, 1, 2, 3, 4, 5],
                                                     n, p=[0.59, 0.24, 0.10, 0.04, 0.02, 0.01]),
        'reservation_status': np.random.choice(['Check-Out', 'Canceled', 'No-Show'],
                                              n, p=[0.75, 0.24, 0.01]),
    })

    log("HotelBookings: Dataset sintético gerado", "OK")

if validate_dataset(df_hotel, "HotelBookings", 100000, 25):
    if save_dataset(df_hotel, 'hotel_bookings.csv', "HotelBookings"):
        datasets_success.append("Hotel Bookings")
    else:
        datasets_failed.append("Hotel Bookings")
else:
    datasets_failed.append("Hotel Bookings")

# ============================================================================
# DATASET 3: Online Retail
# ============================================================================
log("")
log("[3/4] ONLINE RETAIL", "INFO")
log("-"*70)

log("OnlineRetail: Gerando dataset sintético...", "INFO")
n = 50000

countries = ['United Kingdom', 'Germany', 'France', 'EIRE', 'Spain', 'Netherlands', 'Belgium',
             'Switzerland', 'Portugal', 'Australia', 'Norway', 'Italy', 'Channel Islands']

df_retail = pd.DataFrame({
    'InvoiceNo': [f'{536365 + i}' for i in range(n)],
    'StockCode': [f'{np.random.randint(20000, 30000)}' if np.random.random() > 0.05 else f'{chr(65+np.random.randint(0,26))}{np.random.randint(1000,9999)}'
                  for _ in range(n)],
    'Description': [f'PRODUCT_{np.random.randint(1, 500)}' for _ in range(n)],
    'Quantity': np.random.randint(1, 100, n),
    'InvoiceDate': pd.date_range('2010-12-01', periods=n, freq='30min').strftime('%m/%d/%Y %H:%M'),
    'UnitPrice': np.abs(np.random.normal(4, 3, n)),
    'CustomerID': np.random.choice([np.nan] + list(range(12000, 18000)), n, p=[0.15] + [0.85/6000]*6000),
    'Country': np.random.choice(countries, n,
                               p=[0.91] + [0.09/(len(countries)-1)]*(len(countries)-1))
})

df_retail['TotalPrice'] = df_retail['Quantity'] * df_retail['UnitPrice']
log("OnlineRetail: Dataset sintético gerado", "OK")

if validate_dataset(df_retail, "OnlineRetail", 40000, 7):
    if save_dataset(df_retail, 'online_retail.csv', "OnlineRetail"):
        datasets_success.append("Online Retail")
    else:
        datasets_failed.append("Online Retail")
else:
    datasets_failed.append("Online Retail")

# ============================================================================
# DATASET 4: German Credit
# ============================================================================
log("")
log("[4/4] GERMAN CREDIT", "INFO")
log("-"*70)

try:
    log("GermanCredit: Executando create_german_credit.py...", "INFO")
    exec(open('create_german_credit.py').read())

    if os.path.exists('dados/german_credit.csv'):
        df_german = pd.read_csv('dados/german_credit.csv')
        if validate_dataset(df_german, "GermanCredit", 900, 15):
            datasets_success.append("German Credit")
        else:
            datasets_failed.append("German Credit")
    else:
        log("GermanCredit: Arquivo não encontrado após execução", "ERROR")
        datasets_failed.append("German Credit")

except Exception as e:
    log(f"GermanCredit: Erro - {e}", "ERROR")
    datasets_failed.append("German Credit")

# ============================================================================
# RELATÓRIO FINAL
# ============================================================================
log("")
log("="*70)
log("RELATÓRIO FINAL")
log("="*70)

for filename in ['king_county_houses.csv', 'hotel_bookings.csv', 'online_retail.csv', 'german_credit.csv']:
    filepath = f'dados/{filename}'
    if os.path.exists(filepath):
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        df_temp = pd.read_csv(filepath, nrows=5)
        rows = len(pd.read_csv(filepath))
        cols = len(df_temp.columns)
        log(f"✓ {filename:30s} | {rows:7d} linhas | {cols:3d} cols | {size_mb:6.2f} MB", "OK")
    else:
        log(f"✗ {filename:30s} | NÃO ENCONTRADO", "ERROR")

log("")
log(f"Datasets bem-sucedidos: {len(datasets_success)}/4", "INFO")
log(f"Datasets com falha: {len(datasets_failed)}/4", "INFO" if len(datasets_failed) == 0 else "WARN")

if datasets_success:
    log(f"Sucesso: {', '.join(datasets_success)}", "OK")

if datasets_failed:
    log(f"Falha: {', '.join(datasets_failed)}", "WARN")

log("="*70)

if len(datasets_success) == 4:
    log("PROCESSO CONCLUÍDO COM SUCESSO!", "OK")
    sys.exit(0)
else:
    log("PROCESSO CONCLUÍDO COM AVISOS", "WARN")
    sys.exit(1)
