import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib.ticker import FuncFormatter

# 1. Fungsi Bantuan untuk Format Rupiah 

def simple_rupiah_formatter(x, pos):
    """Format angka menjadi Rp X.XXX"""
    if x >= 1000:
        # Menambahkan titik sebagai pemisah ribuan
        return "Rp {:,}".format(int(x)).replace(',', '.')
    return f"Rp {int(x)}"

# 2. Data yang Digunakan (Diagram 1, 2, 3: TETAP)

# Data Top Provinsi Termahal (Untuk Diagram 1 & 2)
df_provinsi_top10 = pd.DataFrame({
    'Provinsi': [
        'Papua Pegunungan', 'Papua Tengah', 'Kalimantan Utara', 'Papua', 'Papua Barat', 
        'Papua Selatan', 'Kalimantan Tengah', 'Maluku Utara', 'Kalimantan Barat', 'Papua Barat Daya'
    ],
    # Harga di gambar dalam ribuan (misal 55.459 berarti Rp 55.459)
    'Harga_Rp': [55459, 45817, 41595, 41352, 40555, 39773, 39463, 38701, 38564, 38329]
})

# Data Tren Harga Cabai Rawit Merah (Untuk Diagram 3)
df_cabai_tren = pd.DataFrame({
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Harga_Rp': [65500, 63500, 73000, 62500, 54500, 57000, 66500, 58500, 51000, 51500, 53500, 66500]
})
TAHUN_CABAI = 2024


# 2b. Data KHUSUS Diagram 4: Harga Tertinggi Daging Sapi (Top 10 Provinsi - SIMULASI TAHUN 2023)

data_daging_2023_top10 = {
    'Provinsi': [
        'DI Yogyakarta', 'Jawa Tengah', 'Banten', 'Jawa Barat', 'Sumatera Utara', 
        'Papua Barat', 'Kalimantan Utara', 'Maluku Utara', 'Papua Tengah', 'Papua Pegunungan'
    ],
    # Harga simulasi (Rp) tahun 2023
    'Harga_Tertinggi_2023_Rp': [
        118000, 120000, 126000, 128000, 135000, 
        145000, 148000, 155000, 168000, 175000
    ]
}
df_daging_sapi_2023 = pd.DataFrame(data_daging_2023_top10)

# Urutkan dari yang termurah ke termahal untuk grafik batang horizontal yang rapi
df_daging_sapi_plot = df_daging_sapi_2023.sort_values(by='Harga_Tertinggi_2023_Rp', ascending=True)


# --- 2c. Data KHUSUS Diagram 5: Pergerakan Harga Beras Premium (5 Wilayah Baru) ---
data_beras_provinsi_baru = {
    'Tahun': [2021, 2022, 2023, 2024, 2025],
    'Aceh': [12000, 12200, 13800, 15800, 15500],
    'Riau': [12500, 12800, 14500, 16500, 16000],
    'Semarang (Jawa Tengah)': [11500, 11700, 13200, 15200, 15200],
    'Bali': [13000, 13500, 15000, 17000, 16800],
    'Papua': [16000, 17000, 19500, 21000, 20500]
}
df_beras_provinsi = pd.DataFrame(data_beras_provinsi_baru).set_index('Tahun')


# 3. Plotting Diagram

# Diagram 1 (Top 10 Provinsi Termahal (Batang Horizontal))
df_top10 = df_provinsi_top10.copy().sort_values(by='Harga_Rp', ascending=True) 

plt.figure(figsize=(10, 7))
bars = plt.barh(df_top10['Provinsi'], df_top10['Harga_Rp'] * 1000, color='#9ACEDD') 
for bar in bars:
    width = bar.get_width()
    # Format X.XXX (menggunakan titik sebagai pemisah ribuan)
    label = f"{width / 1000:,.3f}".replace(',', '_').replace('.', ',').replace('_', '.') 
    plt.text(width + 500, bar.get_y() + bar.get_height()/2, 
             label, 
             ha='left', va='center', fontsize=9)

plt.title("Diagram 1: Top 10 Provinsi dengan Rata-Rata Harga Komoditas Termahal", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Rata-Rata Harga (Rp)", fontsize=10)
plt.ylabel("Provinsi", fontsize=10)
plt.gca().xaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# Diagram 2 (Top 5 Provinsi Termahal (Batang Vertikal))
df_top5 = df_provinsi_top10.head(5).sort_values(by='Harga_Rp', ascending=False)

plt.figure(figsize=(8, 6))
bars = plt.bar(df_top5['Provinsi'], df_top5['Harga_Rp'] * 1000, color='#F08080') 

for bar in bars:
    yval = bar.get_height()
    # Format X.XXX (menggunakan titik sebagai pemisah ribuan)
    label = f"{yval / 1000:,.3f}".replace(',', '_').replace('.', ',').replace('_', '.') 
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1000, 
             label, 
             ha='center', va='bottom', fontsize=9)

plt.title("Diagram 2: Top 5 Provinsi dengan Rata-Rata Harga Komoditas Termahal", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Provinsi", fontsize=10)
plt.ylabel("Rata-Rata Harga (Rp)", fontsize=10)
plt.xticks(rotation=0, ha='center', fontsize=9)
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# Diagram 3 (Tren Harga Cabai Rawit Merah (Garis))
plt.figure(figsize=(10, 6))

plt.plot(df_cabai_tren['Bulan'], df_cabai_tren['Harga_Rp'], marker='o', color='#E74C3C', linestyle='-', linewidth=2)

for i, harga in enumerate(df_cabai_tren['Harga_Rp']):
    # Label Harga di setiap titik data (dibuat format X.XXX)
    plt.text(df_cabai_tren['Bulan'][i], harga + 500, 
             f"{harga/1000:,.3f}".replace(',', '_').replace('.', ',').replace('_', '.'), 
             ha='center', va='bottom', fontsize=8)

plt.title(f"Diagram 3: Tren Tahunan Harga 'Cabai Rawit Merah' Rata-Rata ({TAHUN_CABAI})", 
          fontsize=14, fontweight='bold', pad=20) 
plt.xlabel(f"Bulan ({TAHUN_CABAI})", fontsize=10)
plt.ylabel("Harga Rata-Rata (Rp)", fontsize=10)
plt.xticks(rotation=90, fontsize=8)
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# Diagram 4 (Perbandingan Harga Tertinggi Daging Sapi (Batang Horizontal TOP 10 TAHUN 2023))
plt.figure(figsize=(10, 7)) 

# Warna oranye seperti di gambar: #FFA07A
bars = plt.barh(df_daging_sapi_plot['Provinsi'], df_daging_sapi_plot['Harga_Tertinggi_2023_Rp'], color='#FFA07A') 

# Menambahkan label harga di ujung batang
for bar in bars:
    width = bar.get_width()
    label = simple_rupiah_formatter(width, None) 
    plt.text(width + 1000, bar.get_y() + bar.get_height()/2, 
             label, 
             ha='left', va='center', fontsize=9) 

plt.title("Diagram 4: Top 10 Provinsi dengan Harga Tertinggi Daging Sapi (Simulasi Tahun 2023)", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Harga Tertinggi (Rp)", fontsize=10)
plt.ylabel("Provinsi", fontsize=10)
plt.gca().xaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.yticks(fontsize=10) 
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# Diagram 5 (Pergerakan Harga Beras Premium (Garis Multi-Tahun 5 Wilayah Baru))
plt.figure(figsize=(10, 6))

colors = {
    'Aceh': '#2980B9', 
    'Riau': '#E67E22', 
    'Semarang (Jawa Tengah)': '#27AE60', 
    'Bali': '#C0392B', 
    'Papua': '#8E44AD' 
}

for col in df_beras_provinsi.columns:
    plt.plot(df_beras_provinsi.index, df_beras_provinsi[col], 
             marker='o', 
             label=col, 
             linewidth=2, 
             color=colors[col])
    
    harga_terakhir = df_beras_provinsi[col].iloc[-1]
    # Label wilayah di ujung garis untuk identifikasi
    plt.text(df_beras_provinsi.index[-1] + 0.1, 
             harga_terakhir, 
             col.split(' ')[0], # Hanya ambil kata pertama untuk label singkat di ujung garis
             fontsize=9, 
             ha='left', 
             va='center', 
             color=colors[col])

plt.xticks(df_beras_provinsi.index) 
plt.xlabel("Tahun", fontsize=10)
plt.ylabel("Harga Rata-rata (Rp/Kg)", fontsize=10)

plt.title('Diagram 5: Pergerakan Harga "Beras Premium" di 5 Wilayah (2021 - 2025)', 
          fontsize=14, fontweight='bold', pad=20)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.tight_layout()
plt.show()
