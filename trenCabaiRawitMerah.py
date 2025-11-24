import pandas as pd

# baca file excel
filePath = "data_pangan_bersih.xlsx"
data = pd.read_excel(filePath)

# ambil kolom
data = data[["Nama Provinsi", "Komoditas", "Tahun", "Bulan", "Harga"]]

# filter cabai rawit merah
komo = data["Komoditas"].astype(str).str.lower()
data = data[
    komo.str.contains("cabai")
    & komo.str.contains("rawit")
    & komo.str.contains("merah")
]

# harga harus ada "Rp"
data = data[data["Harga"].astype(str).str.contains("Rp", na=False)]

# ubah harga jadi angka
def parseHarga(x):
    s = str(x).replace("Rp","").replace(".","").replace(",","").replace(" ","")
    return float(s)

data["HargaNum"] = data["Harga"].apply(parseHarga)

# mapping bulan → angka (untuk sorting saja)
bulanMap = {
    "januari":1,"februari":2,"maret":3,"april":4,"mei":5,"juni":6,
    "juli":7,"agustus":8,"september":9,"oktober":10,"november":11,"desember":12
}

def bulanKeAngka(x):
    return bulanMap.get(str(x).strip().lower(), 1)

data["BulanNum"] = data["Bulan"].apply(bulanKeAngka)

# hitung rata-rata berdasarkan tahun & bulan
tabel = (
    data.groupby(["Tahun", "Bulan", "BulanNum"])["HargaNum"]
    .mean()
    .reset_index()
    .sort_values(["Tahun", "BulanNum"])   # urutnya tetap benar
)


# hapus kolom bantu BulanNum
tabel = tabel[["Tahun", "Bulan", "HargaNum"]]

# rename kolom biar rapi
tabel.columns = ["Tahun", "Bulan", "Rata Rata Harga"]

# format rupiah
def formatRupiah(x):
    return "Rp {:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")

tabel["Rata Rata Harga"] = tabel["Rata Rata Harga"].apply(formatRupiah)

print(tabel.head(12))

# simpan
tabel.to_excel("Tren_Cabai_Rawit_Merah_Tahun_Bulan.xlsx", index=False)
