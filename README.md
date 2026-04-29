# Praktikum 1 - Komputasi Numerik (Metode Secant)
Tugas praktikum kelompok 12 dengan metode secant untuk mencari akar persamaan
# Praktikum 1 - Komputasi Numerik (Metode Secant)

Program ini dibuat dengan mengimplementasikan metode Secant untuk mencari akar persamaan, dilengkapi dengan tampilan proses iterasi numerik pada terminal.

## Persamaan yang Digunakan

f(x) = x³ - x - 2

Persamaan ini digunakan karena memiliki akar real yang dapat dicari menggunakan metode Secant dengan dua nilai awal.

---

## Persiapan Iterasi

- Menyiapkan fungsi f(x)
- Menginput nilai awal x0 dan x1
- Menentukan jumlah iterasi dan toleransi
- Menampilkan header tabel hasil iterasi

---

## Proses Iterasi (Metode Secant)

- Setiap iterasi menghitung nilai x2 dengan rumus metode Secant
- Nilai x2 akan semakin mendekati akar sebenarnya
- Error dihitung dari selisih antar iterasi
- Iterasi berhenti jika error < toleransi atau iterasi maksimum tercapai

---

## Tampilan Output

Program akan menampilkan:
- Iterasi ke-n
- Nilai x0, x1, x2
- Nilai f(x2)
- Error

Sehingga pengguna dapat melihat proses konvergensi menuju akar.

---

## Cara Menjalankan

Pastikan Python sudah terinstall.

Jalankan program:

```bash
python praktikum1_secant.py
