import pandas as pd


#Baca file
file_path = "data_pangan_bersih.xlsx"
data = pd.read_excel(file_path)

#Ambil kolom komoditas dan harga
data = data[["Komoditas", "Harga"]]


#Filter baris yang benar-benar ada harga
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

#Ubah harga ke numerik
def parseHarga(x):
    x = str(x)
    x = x.replace("Rp", "").replace(",", "").replace(".", "")
    return float(x)

data["Harga Tertinggi"] = data["Harga"].apply(parseHarga)

#Cari harga tertinggi per komoditas
hargaTertinggi = data.groupby("Komoditas")["Harga Tertinggi"].max().reset_index().sort_values("Harga Tertinggi", ascending=True)

#format rupiah
def formatRupiah(x):
    return "Rp {:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")

hargaTertinggi["Harga Tertinggi"] = hargaTertinggi["Harga Tertinggi"].apply(formatRupiah)

print("TOP 10 Komoditas Termahal:\n")
print(hargaTertinggi.head(10)) #Tampilkan 10 teratas

#Simpan ke Excel
hargaTertinggi.to_excel("Komoditas_Termahal.xlsx", index=False)


print("\nSelesai! File tersimpan: Komoditas_Termahal.xlsx")

