import pandas as pd
import matplotlib.pyplot as plt

# baca file excel, header ada di baris ke-3 (index 2)
file_path = "DATA PANGAN MENTAH.xlsx"
data = pd.read_excel(file_path, header=2)

# ambil kolom provinsi, komoditas, harga
data = data[["Nama Provinsi", "Komoditas", "Harga"]]

# filter hanya baris yang punya harga (ada Rp)
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

# fungsi sederhana untuk ubah "Rp12,072" → 12072
def parseHarga(x):
    x = str(x).replace("Rp", "").replace(".", "").replace(",", "")
    return float(x)

# kolom harga angka
data["HargaNum"] = data["Harga"].apply(parseHarga)

# hitung rata-rata harga komoditas per provinsi
rataProvinsi = (
    data.groupby("Nama Provinsi")["HargaNum"]
    .mean()
    .sort_values(ascending=False)
)

print("\n=== Rata-Rata Harga Komoditas per Provinsi ===")
print(rataProvinsi.head(15))

# simpan ke excel
rataProvinsi.to_excel("Rata_Rata_Harga_Provinsi.xlsx")

# ambil top 15 untuk grafik
top15 = rataProvinsi.head(15)

# grafik
plt.figure(figsize=(10, 6))
plt.barh(top15.index[::-1], top15.values[::-1])
plt.title("Top 15 Provinsi Dengan Rata-Rata Harga Komoditas Tertinggi")
plt.xlabel("Rata-Rata Harga (Rp)")
plt.tight_layout()
plt.show()

print("\nSelesai. Hasil tersimpan di: Rata_Rata_Harga_Provinsi.xlsx")
