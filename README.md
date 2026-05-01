# Praktikum 1 - Komputasi Numerik (Metode Secant)

Program ini dibuat dengan mengimplementasikan metode Secant untuk mencari akar persamaan,
dilengkapi dengan tampilan proses iterasi numerik pada terminal.

## Contoh Persamaan yang Digunakan

f(x) = x³ - x - 2

Persamaan ini dipilih karena memiliki akar real yang dapat dicari
menggunakan metode Secant dengan dua nilai awal.

## Cara Kerja Program

Program meminta user untuk memasukkan:

- Fungsi f(x)
- Nilai x0 (nilai awal pertama)
- Nilai x1 (nilai awal kedua)
- Jumlah iterasi maksimum
- Toleransi error

Program akan menampilkan tabel iterasi di terminal
hingga menemukan akar yang mendekati solusi.

---

## Isi Kode

### Import Library

```python
import math
import re
```

### Validasi Input Fungsi (Regex)

```python
def validasi_fungsi(expr):
    fungsi_diizinkan = r'\b(sin|cos|tan|exp|log|sqrt|pi|e)\b'
    expr_bersih = re.sub(fungsi_diizinkan, '1', expr)
    expr_bersih = re.sub(r'\*\*', '*', expr_bersih)
    pola_diizinkan = r'^[\dx\s\+\-\*\/\^\(\)\.\,]+$'
    if not re.match(pola_diizinkan, expr_bersih):
        return False
    return True
```

- Memvalidasi input fungsi sebelum diproses oleh `eval()`.
- Menghapus nama fungsi matematika yang diizinkan (`sin`, `cos`, `tan`, dll.) terlebih dahulu, lalu mengecek sisa karakter.
- Hanya mengizinkan karakter: angka, `x`, operator (`+`, `-`, `*`, `/`, `^`), tanda kurung, titik, dan koma.
- Mencegah input berbahaya (seperti injeksi kode) masuk ke `eval()`.

### Fungsi f(x)

```python
def buat_fungsi(expr):
    def f(x):
        return eval(expr, {"__builtins__": None}, {
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        })
    return f
```

- Fungsi dibuat secara dinamis dari input user.
- Menggunakan `eval()` untuk menghitung nilai f(x).

### Judul Program

```python
print("=" * 80)
print("PROGRAM PENCARIAN AKAR PERSAMAAN - METODE SECANT")
print("=" * 80)
```

- Menampilkan header program di terminal.
- Membantu memperjelas fungsi program saat dijalankan.

### Input User

```python
fungsi_input = input("Masukkan fungsi f(x): ")
if not validasi_fungsi(fungsi_input):
    print("[✗] Input fungsi tidak valid! Hanya gunakan: x, angka, +, -, *, /, **, (, ), sin, cos, tan, exp, log, sqrt, pi, e")
    exit()
x0 = float(input("Masukkan nilai awal x0: "))
x1 = float(input("Masukkan nilai awal x1: "))
maks_iterasi = int(input("Masukkan jumlah iterasi maksimum: "))
toleransi = float(input("Masukkan toleransi error: "))
```

- Program meminta input fungsi dan nilai awal.
- Input fungsi divalidasi terlebih dahulu menggunakan regex sebelum diproses.
- Jika input tidak valid, program langsung berhenti dengan pesan error.

### Validasi

```python
if (f(x1) - f(x0)) == 0:
    print("Terjadi pembagian dengan nol.")
```

- Mengecek kemungkinan pembagian nol dalam metode Secant.
- Jika terjadi, program dihentikan.

### Persiapan Iterasi

```python
print("=" * 95)
print(f"{'Iterasi':<10}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x2)':<15}{'Error':<15}")
print("=" * 95)
```

- Menyiapkan tampilan tabel iterasi.
- Menampilkan kolom: iterasi, x0, x1, x2, f(x2), dan error.

### Loop Iterasi

```python
for i in range(1, maks_iterasi + 1):
```

- Menggunakan rumus metode Secant untuk menghitung x2.
- Setiap iterasi menghasilkan pendekatan baru terhadap akar.

### Perhitungan Error

```python
error = abs(x2 - x1)
```

- Error dihitung dari selisih nilai x antar iterasi.
- Digunakan untuk menentukan kapan iterasi berhenti.

### Tampilkan Tabel

```python
print(f"{i:<10}{x0:<15.6f}{x1:<15.6f}{x2:<15.6f}{fx2:<15.6f}{error:<15.6f}")
```

- Menampilkan hasil setiap iterasi dalam bentuk tabel.
- Memudahkan pengguna melihat proses konvergensi.

### Update Nilai

```python
x0 = x1
x1 = x2
```

- Nilai x0 dan x1 diperbarui setiap iterasi.
- Digunakan untuk perhitungan selanjutnya.

### Hasil Akhir

```python
print(f"[✓] Akar ditemukan: x = {akar:.6f}")
print(f"[✓] Nilai f(x): {f(akar):.6f}")
```

- Menampilkan nilai akar yang ditemukan.
- Menampilkan nilai f(x) sebagai validasi.

---

## Cara Menjalankan

1. Clone repo

```
git clone https://github.com/Huspy8108/praktikum1_secant.py.git
```

2. Masuk folder

```
cd praktikum1_secant.py
```

3. Jalankan program

```
python praktikum1_secant.py
```

4. Contoh Input

```
* Masukkan fungsi f(x): x**3 - x - 2
* Masukkan nilai awal x0: 1
* Masukkan nilai awal x1: 2
* Masukkan jumlah iterasi maksimum: 10
* Masukkan toleransi error: 0.000001
```

### Contoh Output

```
==============================================================================================================
Iterasi    x0           x1           x2           f(x2)        Error
==============================================================================================================
1          1.000000     2.000000     1.333333     -0.962963    0.666667
2          1.333333     2.000000     1.462687     -0.333339    0.129353
...
==============================================================================================================
[✓] Akar ditemukan: x = 1.521380
```

### Dependensi (Yang Dibutuhkan)

| Library  | Kegunaan                              | Cara Install         |
| -------- | ------------------------------------- | -------------------- |
| Python 3 | Bahasa pemrograman utama              | python.org/downloads |
| re       | Validasi input fungsi (built-in)      | Sudah tersedia       |

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
