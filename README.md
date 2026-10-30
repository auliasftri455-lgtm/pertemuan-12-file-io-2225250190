# Pertemuan 12 - File I/O dan Error Handling

Nama: Aulia Safitri
NIM: 2225250190
Kelas: 3B

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM,nilai

## Cara Menjalankan
python tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Semua data valid | Semua data diproses | 5 data valid diproses | Berhasil |
| Nilai invalid | Baris invalid dilewati | A004,abc dilewati | Berhasil |
| Baris kosong | Baris kosong dilewati | Belum diuji | Belum diuji |
| File hilang | Program tidak crash | Belum diuji | Belum diuji |
| Nilai 60 | Dihitung lulus | Belum diuji | Belum diuji |

## Refleksi
Program dapat menangani data nilai yang tidak valid menggunakan ValueError. Dengan demikian, data lain tetap dapat diproses tanpa menghentikan seluruh program.

## Kuis Formatif

1. **Apa manfaat menggunakan with saat membuka file?**
`with` digunakan agar file tertutup secara otomatis setelah proses selesai, sehingga pengelolaan file lebih aman dan praktis.

2. **Apa perbedaan mode r, w, dan a?**
- `r` (read): untuk membaca file.
- `w` (write): untuk menulis file dari awal dan menimpa isi lama.
- `a` (append): untuk menambahkan data di akhir file tanpa menghapus isi sebelumnya.

3. **Apa risiko menggunakan mode w pada file yang sudah berisi data?**
Isi lama pada file akan terhapus atau tertimpa oleh data yang baru ditulis.

4. **Apa fungsi encoding="utf-8"?**
Untuk mengatur encoding karakter agar teks dapat dibaca dan disimpan dengan konsisten, termasuk karakter khusus.

5. **Apa perbedaan read(), readline(), dan iterasi for pada file?**
- `read()` membaca seluruh isi file sebagai satu string.
- `readline()` membaca satu baris.
- `for` membaca file baris demi baris.

6. **Mengapa strip() sering digunakan setelah membaca baris?**
Untuk menghapus spasi dan karakter baris baru di awal atau akhir teks sehingga data lebih mudah diproses.

7. **Kapan FileNotFoundError dapat terjadi?**
Ketika program mencoba membuka atau membaca file yang tidak ditemukan pada lokasi yang ditentukan.

8. **Kapan ValueError dapat terjadi pada pemrosesan file nilai?**
Ketika nilai yang seharusnya berupa angka berisi teks atau format data tidak sesuai sehingga gagal dikonversi menjadi angka.

9. **Mengapa exception sebaiknya ditangani secara spesifik?**
Agar jenis kesalahan dapat diketahui dengan jelas dan kesalahan pemrograman lain tidak tersembunyi.

10. **Perintah apa yang mengirim commit lokal ke GitHub?**
Perintah `git push` digunakan untuk mengirim commit lokal ke repositori GitHub.