import pandas as pd
import os

# 1. File input CSV
file_path = "data-pangan-mentah.csv"

# 2. File output Excel
output_excel = "HASIL PEMISAH DATA PANGAN.xlsx"

# 3. Komoditas yang ingin dipisahkan
kata_kunci_komoditas = [
    "Beras Premium",
    "Bawang Merah",
    "Cabai Rawit Merah",
    "Telur Ayam Ras",
    "Daging Ayam Ras",
    "Daging Sapi Murni",
    "Bawang Putih (Bonggol)",
    "Minyak Goreng Kemasan",
    "Ikan Tongkol",
    "Kedelai Biji Kering"
]

try:
    # 4. Load data CSV
    print(f"Membaca file: {file_path}")
    df = pd.read_csv(file_path, skiprows=2)
    print("✔ File CSV berhasil dibaca\n")

    # 5. Validasi kolom
    kolom_komoditas = "Komoditas"
    if kolom_komoditas not in df.columns:
        print(f"❌ ERROR: Kolom '{kolom_komoditas}' tidak ditemukan!")
        print("Kolom tersedia:", df.columns.tolist())
        raise SystemExit

    # 6. Mulai membuat file Excel dengan banyak sheet
    with pd.ExcelWriter(output_excel, engine="xlsxwriter") as writer:

        for komoditas in kata_kunci_komoditas:

            # Filter data sesuai komoditas
            df_k = df[df[kolom_komoditas] == komoditas]

            if df_k.empty:
                print(f"⚠ Tidak ada data untuk komoditas: {komoditas}")
                continue

            # Nama sheet disesuaikan
            nama_sheet = komoditas[:31]  # batas max 31 char

            # Masukkan data ke sheet
            df_k.to_excel(writer, sheet_name=nama_sheet, index=False)

            # Tambahkan Table Excel
            workbook  = writer.book
            worksheet = writer.sheets[nama_sheet]

            rows, cols = df_k.shape

            worksheet.add_table(
                0, 0, rows, cols - 1,
                {
                    "columns": [{"header": col} for col in df_k.columns],
                    "style": "Table Style Medium 9"
                }
            )

            print(f"✔ Sheet dibuat untuk komoditas: {komoditas}")

    print("\n=== Semua sheet berhasil disimpan ke file Excel ===")
    print(output_excel)

except FileNotFoundError:
    print(f"❌ ERROR: File '{file_path}' tidak ditemukan!")

except Exception as e:
    print(f"❌ Terjadi error tak terduga: {e}")
