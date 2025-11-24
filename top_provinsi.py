import pandas as pd


# baca file excel, header ada di baris ke-3 (index 2)
file_path = "data_pangan_bersih.xlsx"
data = pd.read_excel(file_path)

# ambil kolom provinsi, komoditas, harga
data = data[["Nama Provinsi", "Komoditas", "Harga"]]

# filter hanya baris yang punya harga (ada Rp)
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

# fungsi untuk ubah "Rp12,072" → 12072
def parseHarga(x):
    x = str(x).replace("Rp", "").replace(".", "").replace(",", "")
    return float(x)

# kolom harga angka
data["Rata Rata Harga"] = data["Harga"].apply(parseHarga)

# hitung rata-rata harga komoditas per provinsi
rataProvinsi = (
    data.groupby("Nama Provinsi")["Rata Rata Harga"]
    .mean()
    .reset_index()
    .sort_values("Rata Rata Harga", ascending=False)
)

# format rupiah
def formatRupiah(x):
    return "Rp {:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")

rataProvinsi["Rata Rata Harga"] = rataProvinsi["Rata Rata Harga"].apply(formatRupiah)

# ambil 5 teratas
top5 = rataProvinsi.head(5)

print("\n=== Rata-Rata Harga Komoditas per Provinsi ===")
print(rataProvinsi.head(5))  # tampilkan 5 teratas

# simpan ke excel
top5.to_excel("top_provinsifix.xlsx", index=False)




print("\nSelesai. Hasil tersimpan di: top_provinsifix.xlsx")
