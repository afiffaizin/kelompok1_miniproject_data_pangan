import pandas as pd

filePath = "HasilPemisahDataPangan.xlsx"

# daftar provinsi yang kamu mau ambil
provinsi = ["Aceh", "Riau", "Maluku", "Bali", "Papua"]

# baca file
data = pd.read_excel(filePath, sheet_name = "Beras Premium")

# filter hanya provinsi pilihan
data = data[data["Nama Provinsi"].isin(provinsi)]

# filter harga valid
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

# ubah harga ke angka
def parseHarga(x):
    x = str(x).replace("Rp","").replace(".","").replace(",","").replace(" ","")
    return float(x)

data["Rata Rata Harga"] = data["Harga"].apply(parseHarga)

# hitung rata-rata per tahun per provinsi
tabel = (
    data.groupby(["Tahun", "Nama Provinsi"])["Rata Rata Harga"]
    .mean()
    .reset_index()
    .sort_values(["Tahun", "Nama Provinsi"])
)

# pilih kolom sesuai format kamu
tabel = tabel[["Tahun", "Nama Provinsi", "Rata Rata Harga"]]

# format rupiah
def formatRupiah(x):
    return "Rp {:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")

tabel["Rata Rata Harga"] = tabel["Rata Rata Harga"].apply(formatRupiah)

print(tabel)

# simpan ke excel
tabel.to_excel("Harga_Beras_Premium_5_Prov_2021-2025.xlsx", index=False)

