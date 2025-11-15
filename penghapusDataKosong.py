import pandas as pd

# ==========================================================
# 1. BACA DATA CSV
# ==========================================================

file_path = "data-pangan-mentah.csv"

print(f"Membaca file: {file_path} ...")
df = pd.read_csv(file_path, skiprows=2)
print("✔ File berhasil dibaca!\n")

# ==========================================================
# 2. CARI BARIS YANG TIDAK LENGKAP
# ==========================================================

print("=== Mengecek baris yang tidak lengkap ===\n")

# Baris yang mengandung nilai kosong
df_kosong = df[df.isnull().any(axis=1)]

if df_kosong.empty:
    print("✔ Tidak ada data kosong. Semua baris lengkap.\n")
else:
    print(f"❌ Ditemukan {len(df_kosong)} baris yang tidak lengkap.\n")

    # Simpan log penghapusan
    log_file = "LOG_PENGHAPUSAN.xlsx"
    df_kosong.to_excel(log_file, index=False)
    print(f"✔ Log baris kosong disimpan ke: {log_file}\n")

    # Tampilkan detail kolom mana yang kosong
    for idx, row in df_kosong.iterrows():
        kolom_kosong = row[row.isnull()].index.tolist()
        print(f"- Baris {idx} dihapus karena kolom kosong: {kolom_kosong}")

# ==========================================================
# 3. HAPUS BARIS KOSONG DAN SIMPAN DATA BERSIH
# ==========================================================

df_bersih = df.dropna()

output_clean = "data_pangan_bersih.xlsx"
df_bersih.to_excel(output_clean, index=False)

print("\n=== DATA BERSIH TELAH DIBUAT ===")
print(f"✔ Total baris awal: {len(df)}")
print(f"✔ Total baris dihapus: {len(df_kosong)}")
print(f"✔ Total baris setelah dibersihkan: {len(df_bersih)}")
print(f"✔ File data bersih disimpan sebagai: {output_clean}")
