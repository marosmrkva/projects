# save as chmi_prg_15dec_07h.py
import io
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- nastavenia ---
# CHMI daily temperature CSV pre stanici Praha-Ruzynì (station id 11518)
csv_url = "https://opendata.chmi.cz/meteorology/climate/historical_csv/data/daily/temperature/dly-0-20000-0-11518-T.csv"

# rozsah rokov (poslednıch 15 vıskytov 15.12. -> vybral som roky 2010..2024)
years = list(range(2010, 2025))

out_folder = "output_chmi_prg"
os.makedirs(out_folder, exist_ok=True)

# --- stiahnutie CSV ---
print("Sahujem CSV z ÈHMÚ ...")
r = requests.get(csv_url, timeout=60)
r.raise_for_status()
print("Stiahnuté:", len(r.content), "bajtov")

# CSV má pravdepodobne polia ako: STATION,ELEMENT,DATE,VALUE, ... (lokalita a element)
# Naèítame s pandas (pokusíme sa zisti formát).
df = pd.read_csv(io.StringIO(r.content.decode('utf-8')), low_memory=False)

# Ukáka ståpcov
print("Ståpce:", df.columns.tolist())

# Oèakávanı formát: STATION,ELEMENT,DT,VALUE,FLAG,QUALITY
# Ak je to inak, uprav filter ïalej pod¾a názvov ståpcov.
# Pre denné T sú hodnoty v °C (môu by prázdne alebo s kvalitou).

# Pre názornos premeníme DT na datetime
dt_col = None
for c in df.columns:
    if c.lower() in ("dt","date","dt_utc","datum","datetime"):
        dt_col = c
        break
if dt_col is None:
    raise SystemExit("Nepodarilo sa nájs ståpec s dátumom v CSV. Skontroluj obsah súboru.")

df[dt_col] = pd.to_datetime(df[dt_col], utc=True, errors='coerce')

# Vyberieme záznamy pre 15.12. kadého zo zvolenıch rokov, termín 07:00 miestneho èasu.
# POZOR: CSV môe by v UTC; ÈHMÚ denné termíny sú udávané v miestnom strednom slneènom èase (local mean time)
# V praxi jsou termíny v CSV v UTC (napr. 'YYYY-MM-DDT07:00Z'). Skript nišie vyberie pod¾a UTC èasu 07:00.
# Ak potrebuješ striktne miestny èas (CET/CEST), upravíme.

df['year'] = df[dt_col].dt.year
df['month'] = df[dt_col].dt.month
df['day'] = df[dt_col].dt.day
df['hour'] = df[dt_col].dt.hour

# Zameriame sa na riadky s termínom 07:00 (hour == 7) a dátumom 15.12.
mask = (df['month'] == 12) & (df['day'] == 15) & (df['hour'] == 7)
df_sel = df.loc[mask].copy()

# Ak je v CSV viacero elementov (napr. T, TMA...), filtrujeme element 'T'
if 'ELEMENT' in df_sel.columns:

