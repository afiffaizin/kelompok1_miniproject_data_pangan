import pandas as pd
import matplotlib.pyplot as plt

#Baca file
file_path = "DATA PANGAN MENTAH.xlsx"
data = pd.read_excel(file_path, header=1)

#Ambil kolom komoditas dan harga
data = data[["Unnamed: 2", "Unnamed: 5"]]
data.columns = ["Komoditas", "Harga"]

#Filter baris yang benar-benar ada harga
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

#Ubah harga ke numerik
def parseHarga(x):
    x = str(x)
    x = x.replace("Rp", "").replace(",", "").replace(".", "")
    return float(x)

data["HargaNum"] = data["Harga"].apply(parseHarga)

#Cari harga tertinggi per komoditas
hargaTertinggi = data.groupby("Komoditas")["HargaNum"].max().sort_values(ascending=False)

print("TOP 20 Komoditas Termahal:\n")
print(hargaTertinggi.head(20))

#Simpan ke Excel
hasil = hargaTertinggi.reset_index().rename(columns={"HargaNum": "HargaTertinggi"})
hasil.to_excel("Hasil_Komoditas_Termahal.xlsx", index=False)

#Grafik (Top 20)
top20 = hasil.head(20)

plt.figure(figsize=(10, 6))
plt.barh(top20["Komoditas"][::-1], top20["HargaTertinggi"][::-1])
plt.title("Top 20 Komoditas dengan Harga Tertinggi")
plt.xlabel("Harga (Rp)")
plt.tight_layout()
plt.show()

print("\nSelesai! File tersimpan: Hasil_Komoditas_Termahal.xlsx")

