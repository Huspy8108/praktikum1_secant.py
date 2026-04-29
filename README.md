# Praktikum 1 - Komputasi Numerik (Metode Secant)
Tugas praktikum kelompok 12 - Program ini dibuat dengan mengimplementasikan metode Secant untuk mencari akar persamaan, dilengkapi dengan tampilan proses iterasi numerik pada terminal.

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

## Instalasi dari Nol

### Python 3

**Mac:**
1. Buka https://www.python.org/downloads/
2. Klik tombol kuning "Download Python 3.x.x"
3. Buka file .pkg yang terdownload
4. Ikuti langkah instalasi sampai selesai
5. Cek di terminal:

   python3 --version

**Windows:**
1. Buka https://www.python.org/downloads/
2. Klik "Download Python 3.x.x"
3. Buka file .exe yang terdownload
4. Centang "Add Python to PATH" 
5. Klik Install Now
6. Cek di Command Prompt:
   
   python3 --version

### matplotlib & numpy

**Mac & Linux:**
1. Buka terminal
2. Ketik:
   pip3 install matplotlib
3. Tunggu sampai muncul "Successfully installed"
4. Cek instalasi:
   pip3 show matplotlib

**Windows:**
1. Buka Command Prompt
2. Ketik:
   pip3 install matplotlib
3. Tunggu sampai muncul "Successfully installed"
4. Cek instalasi:
   pip show matplotlib

> numpy akan otomatis ikut terinstall bersama matplotlib,
> jadi tidak perlu install terpisah.

