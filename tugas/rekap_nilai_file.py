def baca_data(nama_file):
    hasil = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    hasil.append((nim, nilai))
                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return hasil


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    jumlah_data = len(data)
    daftar_nilai = [nilai for nim, nilai in data]

    rata_rata = sum(daftar_nilai) / jumlah_data
    nilai_minimum = min(daftar_nilai)
    nilai_maksimum = max(daftar_nilai)
    jumlah_lulus = sum(1 for nilai in daftar_nilai if nilai >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_minimum}\n")
        file.write(f"Nilai maksimum: {nilai_maksimum}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)
tulis_rekap(output_file, data)

print("Proses rekap selesai.")