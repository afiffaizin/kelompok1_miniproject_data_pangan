import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


# --- 1. Definisi Nama File ---
files = {
    'komoditas': 'komoditas_termahal.xlsx',
    'provinsi': 'top5_provinsifix.xlsx',
    'tren': 'Tren_Cabai_Rawit_Merah.xlsx',
    'daging': 'Perbandingan_harga_max_Daging_Sapi_2023.xlsx',
    'beras': 'Harga_Beras_Premium_5_Prov_2021-2025.xlsx' # File baru
}

# --- 2. Load Data ---
try:
    df_komoditas = pd.read_excel(files['komoditas'])
    df_provinsi = pd.read_excel(files['provinsi'])
    df_tren = pd.read_excel(files['tren'])
    df_daging = pd.read_excel(files['daging'])
    df_beras = pd.read_excel(files['beras'])
except Exception as e:
    print(f"Terjadi error saat membaca file: {e}")

# --- 3. Cleaning Data ---
def clean_currency(x):
    if isinstance(x, str):
        # Hapus 'Rp', hapus titik ribuan, ganti koma desimal dengan titik
        clean_str = x.replace('Rp', '').replace('.', '').replace(',', '.').strip()
        return float(clean_str)
    return x
# Terapkan cleaning
df_komoditas['Harga Tertinggi'] = df_komoditas['Harga Tertinggi'].apply(clean_currency)
df_provinsi['Rata Rata Harga'] = df_provinsi['Rata Rata Harga'].apply(clean_currency)
df_tren['Rata Rata Harga'] = df_tren['Rata Rata Harga'].apply(clean_currency)
df_daging['HargaNum'] = df_daging['HargaNum'].apply(clean_currency)
df_beras['Rata Rata Harga'] = df_beras['Rata Rata Harga'].apply(clean_currency)

# sorting khusus untuk tren cabai berdasarkan bulan
bulan_order = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
               'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
df_tren['Bulan'] = pd.Categorical(df_tren['Bulan'], categories=bulan_order, ordered=True)
df_tren_sorted = df_tren.sort_values('Bulan')


# --- 4. Plotting ---

# Plot 1: Komoditas Termahal (Horizontal Bar)
plt.figure(figsize=(12, 8))
plt.barh(df_komoditas['Komoditas'], df_komoditas['Harga Tertinggi'], color='skyblue')
plt.xlabel('Harga Tertinggi (Rp)')
plt.title('Komoditas Termahal')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.tight_layout()
plt.show()

# Plot 2: Top 5 Provinsi (Vertical Bar)
plt.figure(figsize=(10, 6))
plt.bar(df_provinsi['Nama Provinsi'], df_provinsi['Rata Rata Harga'], color='lightgreen')
plt.ylabel('Rata-rata Harga (Rp)')
plt.title('Top 5 Provinsi dengan Rata-rata Harga Komoditas Tertinggi')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.tight_layout()
plt.show()

# Plot 3: Tren Harga Cabai (Line Chart)
plt.figure(figsize=(12, 6))
plt.plot(df_tren['Bulan'], df_tren['Rata Rata Harga'], marker='o', linestyle='-', color='red', linewidth=2)
plt.ylabel('Rata-rata Harga (Rp)')
plt.title('Tren Harga Cabai Rawit Merah Tahun 2024')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.tight_layout()
plt.show()

# Plot 4: Perbandingan Harga Daging Sapi (Horizontal Bar)
plt.figure(figsize=(12, 8))
plt.barh(df_daging['Nama Provinsi'], df_daging['HargaNum'], color='salmon')
plt.xlabel('Harga Tertinggi (Rp)')
plt.title('Perbandingan Harga Tertinggi Daging Sapi 2023 per Provinsi')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.tight_layout()
plt.show()

# Plot 5: Pergerakan Harga Beras Premium (Multi-Line Chart) - BARU
plt.figure(figsize=(12, 6))
# Menggunakan seaborn agar otomatis membuat garis berbeda warna untuk tiap provinsi
sns.lineplot(data=df_beras, x='Tahun', y='Rata Rata Harga', hue='Nama Provinsi', marker='o', palette='tab10')
plt.title('Pergerakan Harga Beras Premium (2021-2025)')
plt.ylabel('Rata-rata Harga (Rp)')
plt.xlabel('Tahun')
plt.grid(True, linestyle='--', alpha=0.7)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True)) # Pastikan tahun berupa angka bulat
plt.legend(title='Nama Provinsi', bbox_to_anchor=(1.05, 1), loc='upper left') # Legenda di luar
plt.tight_layout()
plt.show()