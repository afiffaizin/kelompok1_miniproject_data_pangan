import pandas as pd
import matplotlib.pyplot as plt

file_path = "DATA PANGAN MENTAH.xlsx"
data = pd.read_excel(file_path, header=1)

# rename kolom supaya rapi
data = data.rename(columns={
    "Unnamed: 0": "kode_provinsi",
    "Unnamed: 1": "provinsi",
    "Unnamed: 2": "komoditas",
    "Unnamed: 3": "tahun",
    "Unnamed: 4": "bulan",
    "Unnamed: 5": "harga"
})

# ambil baris yang ada "Rp"
data = data[data["harga"].astype(str).str.contains("Rp", na=False)]

# ubah Rp12,072 -> 12072
def parse_rupiah(s):
    s = str(s).replace("Rp", "").replace(".", "").replace(",", "")
    return float(s)

data["harga_num"] = data["harga"].apply(parse_rupiah)

# groupby komoditas → ambil harga tertinggi
harga_maks = data.groupby("komoditas")["harga_num"].max().sort_values(ascending=False)

print(harga_maks.head(20))

# buat dataframe rapi
df_harga = harga_maks.reset_index().rename(columns={"harga_num": "harga_tertinggi"})

# Simpan ke Excel saja (tanpa CSV)
df_harga.to_excel("hasil_komoditas_termahal.xlsx", index=False)

# GRAFIK
plt.figure(figsize=(10, 6))
plt.barh(df_harga["komoditas"].head(20)[::-1], df_harga["harga_tertinggi"].head(20)[::-1])
plt.xlabel("Harga Tertinggi (Rp)")
plt.title("Top 20 Komoditas dengan Harga Tertinggi")
plt.tight_layout()
plt.show()

print("Selesai!")
