import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Baca file Excel (header mulai baris ke-2)
df = pd.read_excel("DATA PANGAN MENTAH.xlsx", header=1)

# 2. Rename kolom biar rapi
df = df.rename(columns={
    "Unnamed: 0": "kode_provinsi",
    "Unnamed: 1": "provinsi",
    "Unnamed: 2": "komoditas",
    "Unnamed: 3": "tahun",
    "Unnamed: 4": "bulan",
    "Unnamed: 5": "harga"
})

# 3. Ambil hanya baris yang berisi harga (ada tulisan "Rp")
df = df[df["harga"].astype(str).str.contains("Rp", na=False)].copy()

# 4. Bersihkan harga → ubah "Rp12,072" menjadi 12072
df["harga_num"] = (
    df["harga"]
    .str.replace("Rp", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# 5. Cari harga tertinggi per komoditas
harga_maks = df.groupby("komoditas")["harga_num"].max()

# 6. Urutkan dari harga tertinggi
harga_maks = harga_maks.sort_values(ascending=False)

# 7. Cetak hasil
print(harga_maks)

# 8. Komoditas termahal
komoditas_termahal = harga_maks.idxmax()
harga_tertinggi = harga_maks.max()

print("\nKomoditas Termahal:")
print(f"{komoditas_termahal} — Rp{harga_tertinggi:,.0f}")


# 9. Simpan hasil ke file CSV
harga_maks.to_csv("harga_tertinggi_per_komoditas.csv", header=["harga_tertinggi"])
output_csv = "harga_tertinggi_per_komoditas.csv"
output_xlsx = "harga_tertinggi_per_komoditas.xlsx"

# konversi Series -> DataFrame untuk menyertakan nama kolom
df_harga_maks = harga_maks.reset_index().rename(columns={"harga_num": "harga_tertinggi"})
df_harga_maks.to_csv(output_csv, index=False)
df_harga_maks.to_excel(output_xlsx, index=False)
print(f"\nTabel tersimpan: {os.path.abspath(output_csv)} dan {os.path.abspath(output_xlsx)}")

# 10. Tampilkan tabel rapi (contoh: Top 20)
TOP_N = 20
print(f"\nTop {TOP_N} Komoditas berdasarkan harga tertinggi:")
print(df_harga_maks.head(TOP_N).to_string(index=False))
  # kalau pakai Jupyter, ini akan tampil rapi

# 11. Buat grafik bar (semua komoditas atau top N untuk kejelasan)
plot_top_n = 25  # ganti sesuai kebutuhan (None = semua)
if plot_top_n is None:
    plot_df = df_harga_maks
else:
    plot_df = df_harga_maks.head(plot_top_n)

# Matplotlib plot
plt.figure(figsize=(12, 6))
plt.barh(plot_df["komoditas"][::-1], plot_df["harga_tertinggi"][::-1])  # horizontal bar, terurut naik
plt.xlabel("Harga Tertinggi (Rp)")
plt.title(f"Top {len(plot_df)} Komoditas Berdasarkan Harga Tertinggi")
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"Rp{int(x):,}"))
plt.tight_layout()

# Simpan gambar
output_png = "grafik_komoditas_termahal.png"
plt.savefig(output_png, dpi=300)
print(f"Grafik tersimpan: {os.path.abspath(output_png)}")

# Tampilkan plot (jika dijalankan di environment dengan GUI atau Jupyter)
plt.show()