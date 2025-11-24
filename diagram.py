import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data 1: tren musiman cabai rawit merah (Grafik 1) - Asumsi 2024
data_cabai = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Harga_Rp': [65500, 63500, 73000, 62500, 54500, 57000, 66500, 58500, 51000, 51500, 53500, 66500]
}
df_cabai = pd.DataFrame(data_cabai)
TAHUN_CABAI = "2024" 

# Data 2 & 3: harga rata-rata komoditas DKI Jakarta 2021 (Grafik 2 & 3)
data_jakarta = {
    'Komoditas': [
        'Daging Sapi Murni', 'Cabai Rawit Merah', 'Cabai Merah Keriting', 'Bawang Merah', 
        'Daging Ayam Ras', 'Bawang Putih (Bonggol)', 'Telur Ayam Ras', 'Minyak Goreng Kemasan', 
        'Gula Pasir Lokal/Curah', 'Beras Premium', 'Kedelai Biji Kering', 'Beras Medium'
    ],
    'Harga_Rp': [
        125000, 65000, 43000, 37000, 36000, 32000, 26000, 15000, 14000, 13500, 13000, 12500
    ]
}
df_jakarta = pd.DataFrame(data_jakarta)
TAHUN_JAKARTA = "2021"

# Data 4: tren harga nasional bulanan beras premium 2023 (Grafik 4)
data_beras_nasional = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
    'Harga_Rp': [13500, 13650, 13800, 13900, 13900, 13880, 13880, 14080, 14750, 15200, 15250, 15280]
}
df_beras_nasional = pd.DataFrame(data_beras_nasional)
TAHUN_BERAS_NASIONAL = "2023"

# Data 5: pergerakan harga beras premium di 5 Provinsi (Grafik 5)
data_beras_provinsi = {
    'Tanggal': pd.to_datetime(['2021-01-01', '2022-01-01', '2023-01-01', '2024-01-01', '2025-07-01']),
    'Banten': [11500, 11500, 13500, 15500, 15300],
    'Sulawesi Selatan': [11000, 11000, 12800, 14800, 14500],
    'Jawa Tengah': [11200, 11400, 13000, 15000, 15000],
    'Sumatera Utara': [14000, 15000, 17800, 17000, 16500],
    'Kalimantan Selatan': [12000, 12000, 13200, 15300, 15200]
}
df_beras_provinsi = pd.DataFrame(data_beras_provinsi).set_index('Tanggal')

# fungsi formatter

def simple_rupiah_formatter(x, pos):
    """Format angka menjadi Rp X.XXX"""
    return "Rp {:,}".format(int(x)).replace(',', '.')

# grafik garis C (tren tahunan harga cabai rawit merah)

print(" grafik: tren tahunan harga cabai rawit merah ")
plt.figure(figsize=(12, 7))
plt.plot(df_cabai['Bulan'], df_cabai['Harga_Rp'], marker='o', color='red', linestyle='-', linewidth=2)

for i, harga in enumerate(df_cabai['Harga_Rp']):
    plt.text(df_cabai['Bulan'][i], harga + 1500, 
             simple_rupiah_formatter(harga, None).replace('Rp ', ''), ha='center', va='bottom', fontsize=9)

plt.title(f"grafik: tren tahunan harga 'cabai rawit merah' rata-rata ({TAHUN_CABAI})", 
          fontsize=16, fontweight='bold', pad=20) 
plt.xlabel(f"Bulan ({TAHUN_CABAI})", fontsize=12)
plt.ylabel("Harga Rata-rata (Rp)", fontsize=12)
plt.xticks(rotation=90, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# diagram batang (harga rata-rata semua komditas DKI Jakarta)

print("\n grafik: harga rata-rata semua komoditas DKI Jakarta ")
plt.figure(figsize=(14, 7))
plt.bar(df_jakarta['Komoditas'], df_jakarta['Harga_Rp'], color='skyblue')

# label harga di atas batang (opsional)
for i, harga in enumerate(df_jakarta['Harga_Rp']):
    plt.text(i, harga + 2000, 
             simple_rupiah_formatter(harga, None), ha='center', va='bottom', fontsize=8)

plt.title(f"grafik: harga rata-rata komoditas pokok DKI Jakarta ({TAHUN_JAKARTA})", 
          fontsize=16, fontweight='bold')
plt.xlabel("Komoditas")
plt.ylabel("Harga Rata-rata (Rp)")
plt.xticks(rotation=90, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# diagram batang (perbandingan harga komoditas top 3 DKI Jakarta)

print("\n grafik: perbandingan harga komoditas Top 3 DKI Jakarta ---")
df_top3 = df_jakarta.sort_values(by='Harga_Rp', ascending=False).head(3)
colors = ['darkred', 'red', 'lightcoral'] 

plt.figure(figsize=(8, 6))
plt.bar(df_top3['Komoditas'], df_top3['Harga_Rp'], color=colors)

for i, harga in enumerate(df_top3['Harga_Rp']):
    plt.text(i, harga + 3000, 
             simple_rupiah_formatter(harga, None), ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title(f"grafik: perbandingan harga komoditas top 3 DKI Jakarta ({TAHUN_JAKARTA})", 
          fontsize=16, fontweight='bold')
plt.xlabel("Komoditas")
plt.ylabel("Harga Rata-rata (Rp)")
plt.xticks(rotation=0, ha='center') 
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# grafik garis (tren harga nasional bulanan beras premium)

print("\n grafik: tren harga nasional bulanan beras premium ")
plt.figure(figsize=(10, 6))

# membuat diagram garis (Line Plot)
plt.plot(df_beras_nasional['Bulan'], df_beras_nasional['Harga_Rp'], marker='o', color='navy', linewidth=2)

# mengatur batas sumbu Y
# batas bawah diatur mendekati harga terendah agar tren lebih terlihat jelas.
plt.ylim(13000, max(df_beras_nasional['Harga_Rp']) + 300) 

# Menambahkan Label Angka di atas Titik
for i, harga in enumerate(df_beras_nasional['Harga_Rp']):
    plt.text(df_beras_nasional['Bulan'][i], harga + 80, 
             simple_rupiah_formatter(harga, None).replace('Rp ', ''), ha='center', va='bottom', fontsize=8)

# menambahkan anotasi kenaikan harga signifikan
plt.annotate('kenaikan signifikan dimulai', 
             xy=('Agu', 14080), 
             xytext=('Jul', 14500),
             arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
             fontsize=10, 
             color='red',
             fontweight='bold')

plt.title(f'grafik: tren harga nasional bulanan "beras premium" ({TAHUN_BERAS_NASIONAL})', 
          fontsize=16, fontweight='bold')
plt.xlabel(f"Bulan ({TAHUN_BERAS_NASIONAL})")
plt.ylabel("Harga Rata-rata (Rp)")
plt.grid(axis='y', linestyle='--')
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.tight_layout()
plt.show()

#grafik garis (pergerakan harga beras premium di 5 provinsi (garis multi-tahun))

print("\n grafik: pergerakan harga beras premium di 5 Provinsi ")
plt.figure(figsize=(12, 7))

for col in df_beras_provinsi.columns:
    plt.plot(df_beras_provinsi.index, df_beras_provinsi[col], marker='o', label=col, linewidth=2)

# Label Teks untuk Titik Data Terakhir (Juli 2025)
for col in df_beras_provinsi.columns:
    harga_terakhir = df_beras_provinsi[col].iloc[-1]
    tanggal_terakhir = df_beras_provinsi.index[-1]
    
    plt.text(tanggal_terakhir, harga_terakhir, 
             f'{col.split(" ")[0]}', 
             fontsize=9, ha='left', va='center')

# Pengaturan Grafik
plt.title(
    'grafik: Pergerakan Harga "Beras Premium" di 5 Provinsi (2021 - 2025)', 
    fontsize=16, 
    fontweight='bold', 
    pad=20
)
plt.xlabel("Tahun", fontsize=12)
plt.ylabel("Harga Rata-rata (Rp/Kg)", fontsize=12)

# Mengatur sumbu X untuk menampilkan Tahun
plt.xticks(df_beras_provinsi.index, 
           [f'{t.year}' for t in df_beras_provinsi.index], 
           rotation=0, ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(
    title='Provinsi', 
    loc='upper center', 
    ncol=3,
    bbox_to_anchor=(0.5, -0.2) 
)
plt.gca().yaxis.set_major_formatter(FuncFormatter(simple_rupiah_formatter))
plt.tight_layout(rect=[0, 0.1, 1, 1]) 
plt.show()
