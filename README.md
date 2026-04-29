# Praktikum 1 - Komputasi Numerik (Metode Secant)

Program ini dibuat dengan mengimplementasikan metode Secant untuk mencari akar persamaan,
dilengkapi dengan tampilan proses iterasi numerik pada terminal.

## Persamaan yang Digunakan

f(x) = x³ - x - 2

Persamaan ini digunakan karena memiliki akar real yang dapat dicari
menggunakan metode Secant dengan dua nilai awal.

---

## Cara Kerja Program

Program meminta user untuk memasukkan:
- Fungsi f(x)
- Nilai awal x0
- Nilai awal x1  
- Jumlah iterasi maksimum
- Toleransi error

Program akan menampilkan tabel iterasi di terminal
hingga menemukan akar yang mendekati solusi.

---

## Hasil Kode

### Import Library

* Menggunakan library `math` untuk fungsi matematika.
* Digunakan untuk menghitung sin, cos, log, dan lainnya jika diperlukan.

### Fungsi f(x)

* Fungsi dibuat secara dinamis dari input user.
* Menggunakan `eval()` untuk menghitung nilai f(x).

### Judul Program

* Menampilkan header program di terminal.
* Membantu memperjelas fungsi program saat dijalankan.

### Input User

* Program meminta input fungsi dan nilai awal.
* User bisa memasukkan berbagai bentuk fungsi.

### Persiapan Iterasi

* Menyiapkan tampilan tabel iterasi.
* Menampilkan kolom: iterasi, x0, x1, x2, f(x2), dan error.

### Loop Iterasi

* Menggunakan rumus metode Secant untuk menghitung x2.
* Setiap iterasi menghasilkan pendekatan baru terhadap akar.

### Perhitungan Error

* Error dihitung dari selisih nilai x antar iterasi.
* Digunakan untuk menentukan kapan iterasi berhenti.

### Tampilkan Tabel

* Menampilkan hasil setiap iterasi dalam bentuk tabel.
* Memudahkan pengguna melihat proses konvergensi.

### Update Nilai

* Nilai x0 dan x1 diperbarui setiap iterasi.
* Digunakan untuk perhitungan selanjutnya.

### Hasil Akhir

* Menampilkan nilai akar yang ditemukan.
* Menampilkan nilai f(x) sebagai validasi.

---

## Cara Menjalankan

Jalankan program:

```bash
python praktikum1_secant.py
