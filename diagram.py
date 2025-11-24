import pandas as pd
import matplotlib.pyplot as plt

# data 1: tren musiman cabai rawit merah (Grafik C)
data_cabai = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Harga_Rp': [65500, 63500, 73000, 62500, 54500, 57000, 66500, 58500, 51000, 51500, 53500, 66500]
}
df_cabai = pd.DataFrame(data_cabai)

# data 2 & 5: harga rata-rata Komoditas di DKI Jakarta 2021 (Grafik 2)
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

# Data 3: Pergerakan Harga Beras Premium di 5 Provinsi (Grafik 5)
# Hanya mengambil beberapa titik data penting untuk simulasi tren
data_beras_provinsi = {
    'Tanggal': pd.to_datetime(['2021-01-01', '2022-01-01', '2023-01-01', '2024-01-01', '2025-07-01']),
    'Banten': [11500, 11500, 13500, 15500, 15300],
    'Sulawesi Selatan': [11000, 11000, 12800, 14800, 14500],
    'Jawa Tengah': [11200, 11400, 13000, 15000, 15000],
    'Sumatera Utara': [14000, 15000, 17800, 17000, 16500],
    'Kalimantan Selatan': [12000, 12000, 13200, 15300, 15200]
}
df_beras_provinsi = pd.DataFrame(data_beras_provinsi).set_index('Tanggal')


# data 4: tren harga nasional bulanan beras premium 2023 (Grafik 7)
data_beras_nasional = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
    'Harga_Rp': [13500, 13650, 13800, 13900, 13900, 13880, 13880, 14080, 14750, 15200, 15250, 15280]
}
df_beras_nasional = pd.DataFrame(data_beras_nasional)


# fungsi untuk mengatur format rupiah pada sumbu Y 
from matplotlib.ticker import FuncFormatter

def rupiah_formatter(x, pos):
    """Format angka menjadi Rp K, Juta, dsb."""
    if x >= 1e6:
        return 'Rp{:1.1f}Jt'.format(x * 1e-6)
    elif x >= 1e3:
        return 'Rp{:1.0f}Ribu'.format(x * 1e-3)
    return 'Rp{:1.0f}'.format(x)

# diagram garis (tren musiman cabai rawit merah)

plt.figure(figsize=(10, 6))
plt.plot(df_cabai['Bulan'], df_cabai['Harga_Rp'], marker='o', color='red')
plt.title("Grafik: Tren Musiman Harga 'Cabai Rawit Merah' (Rata-rata)", fontsize=14)
plt.xlabel("Bulan")
plt.ylabel("Harga Rata-rata (Rp)")
plt.grid(axis='y', linestyle='--')
plt.gca().yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))
plt.tight_layout()
plt.show()

# diagram batang (harga rata-rata komoditas DKI Jakarta (Semua))

plt.figure(figsize=(12, 7))
plt.bar(df_jakarta['Komoditas'], df_jakarta['Harga_Rp'], color='pink')
plt.title("Grafik: Harga Rata-rata Komoditas di DKI Jakarta (2021)", fontsize=14)
plt.xlabel("Komoditas")
plt.ylabel("Harga Rata-rata (Rp)")
plt.xticks(rotation=90, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))
plt.tight_layout()
plt.show()

# diagram garis (pergerakan harga beras premium di 5 Provinsi)

plt.figure(figsize=(12, 7))
for col in df_beras_provinsi.columns:
    plt.plot(df_beras_provinsi.index, df_beras_provinsi[col], marker='o', label=col)

plt.title('Grafik: Pergerakan Harga "Beras Premium" di 5 Provinsi', fontsize=14)
plt.xlabel("Tanggal")
plt.ylabel("Harga Rata-rata (Rp)")
plt.grid(axis='y', linestyle='--')
plt.legend(loc='upper left', ncol=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))
plt.tight_layout()
plt.show()

#  diagram garis (tren harga nasional bulanan beras premium 2023)

plt.figure(figsize=(10, 6))
plt.plot(df_beras_nasional['Bulan'], df_beras_nasional['Harga_Rp'], marker='o', color='navy')
plt.title('Grafik: Tren Harga Nasional Bulanan "Beras Premium" (2023)', fontsize=14)
plt.xlabel("Bulan")
plt.ylabel("Harga Rata-rata (Rp)")
plt.grid(axis='y', linestyle='--')
plt.gca().yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))
plt.tight_layout()
plt.show()

# diagram batang (perbandingan harga komoditas top 3 di DKI Jakarta)

df_top3 = df_jakarta.head(3)
plt.figure(figsize=(8, 6))
plt.bar(df_top3['Komoditas'], df_top3['Harga_Rp'], color=['darkred', 'red', 'lightcoral'])
plt.title("Grafik: Perbandingan Harga Komoditas Top 3 DKI Jakarta (2021)", fontsize=14)
plt.xlabel("Komoditas")
plt.ylabel("Harga Rata-rata (Rp)")
plt.gca().yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))
plt.tight_layout()
plt.show()

