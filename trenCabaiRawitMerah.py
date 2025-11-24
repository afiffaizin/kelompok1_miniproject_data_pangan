import pandas as pd

# baca file excel
filePath = "data_pangan_bersih.xlsx"
data = pd.read_excel(filePath)

# ambil kolom
data = data[["Nama Provinsi", "Komoditas", "Tahun", "Bulan", "Harga"]]

# filter cabai rawit merah
komo = data["Komoditas"].astype(str).str.lower()
data = data[komo.str.contains("cabai rawit merah")]

# filter hanya tahun 2024
data = data[data["Tahun"] == 2024]

# harga harus ada "Rp"
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

# ubah harga jadi angka
def parseHarga(x):
    x = str(x).replace("Rp","").replace(".","").replace(",","").replace(" ","")
    return float(x)

# kolom harga angka
data["Rata Rata Harga"] = data["Harga"].apply(parseHarga)

# mapping bulan → angka (untuk sorting)
bulanMap = {
    "januari":1,"februari":2,"maret":3,"april":4,"mei":5,"juni":6,
    "juli":7,"agustus":8,"september":9,"oktober":10,"november":11,"desember":12
}

# fungsi bulan ke angka
def bulanKeAngka(x):
    return bulanMap.get(str(x).strip().lower(), 1)

data["BulanNum"] = data["Bulan"].apply(bulanKeAngka)

# hitung rata-rata berdasarkan tahun & bulan
tabel = (
    data.groupby(["Tahun", "Bulan", "BulanNum"])["Rata Rata Harga"]
    .mean()
    .reset_index()
    .sort_values(["Tahun", "BulanNum"])   # urutnya tetap benar
)


# hapus kolom bantu BulanNum
tabel = tabel[["Tahun", "Bulan", "Rata Rata Harga"]]

# format rupiah
def formatRupiah(x):
    return "Rp {:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")

tabel["Rata Rata Harga"] = tabel["Rata Rata Harga"].apply(formatRupiah)

print(tabel.head(12))

# simpan
tabel.to_excel("Tren_Cabai_Rawit_Merah.xlsx", index=False)
