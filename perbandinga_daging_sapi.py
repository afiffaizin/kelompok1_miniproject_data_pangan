import pandas as pd

# baca file
filePath = "HasilPemisahDataPangan.xlsx"
data = pd.read_excel(filePath, sheet_name = "Daging Sapi Murni")

# ambil kolom yang diperlukan
data = data[["Nama Provinsi", "Komoditas", "Tahun", "Harga"]]

# filter tahun 2023
data = data[data["Tahun"] == 2023]

# filter harga yang ada Rp
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

# ubah harga jadi numerik
def parseHarga(x):
    x = str(x).replace("Rp","").replace(".","").replace(",","").replace(" ","")
    return float(x)

data["HargaNum"] = data["Harga"].apply(parseHarga)

# HARGA TERTINGGI per provinsi (MAX)
tabel = (
    data.groupby("Nama Provinsi")["HargaNum"]
    .max()
    .reset_index()
    .sort_values("HargaNum", ascending=False)
)

# format ke rupiah
def formatRupiah(x):
    return "Rp {:,}".format(int(x)).replace(",", ".")

tabel["HargaNum"] = tabel["HargaNum"].apply(formatRupiah)

print("\n=== Harga Tertinggi Daging Sapi Tahun 2023 per Provinsi ===")
print(tabel)

# simpan ke excel
tabel.to_excel("Perbandingan_harga_max_Daging_Sapi_2023.xlsx", index=False)
