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

- `math` menyediakan fungsi matematika seperti `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `pi`, dan `e`.
- `re` digunakan untuk preprocessing ekspresi fungsi dari input user (konversi otomatis perkalian implisit dan operator pangkat).

### Fungsi buat_fungsi(expr)

```python
def buat_fungsi(expr):
<<<<<<< HEAD
   expr = expr.replace("^", "**")                      
    expr = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', expr)
    expr = re.sub(r'(\))(\w)', r'\1*\2', expr)          
   def f(x):
=======
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', expr)
    expr = re.sub(r'(\))(\w)', r'\1*\2', expr)
    def f(x):
>>>>>>> 8c40d871141a9a3087e239eb82866d6a524aebe8
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

Fungsi ini memproses ekspresi input user dalam 3 tahap sebelum dievaluasi:

- `^` diganti menjadi `**` sehingga user bisa menulis `x^2` maupun `x**2`.
- Perkalian implisit antara angka dan variabel/fungsi otomatis ditambahkan `*`, contoh: `2x` → `2*x`, `2sin(x)` → `2*sin(x)`.
- Perkalian implisit setelah kurung tutup juga ditangani, contoh: `(x+1)x` → `(x+1)*x`.
- `eval()` dijalankan di namespace terbatas — hanya variabel `x` dan fungsi math yang diizinkan, sehingga input berbahaya tidak bisa dieksekusi.

### Judul dan Contoh Fungsi

```python
print("PROGRAM PENCARIAN AKAR PERSAMAAN - METODE SECANT")
print("Contoh penulisan fungsi:")
print("Pangkat Terbesar wajib didepan")
print("  x**3 - x - 2")
print("  cos(x) - x")
print("  exp(-x) - x")
```

- Menampilkan header program dan contoh format penulisan fungsi yang valid.
- Mengingatkan user bahwa pangkat terbesar harus ditulis di depan agar pembacaan fungsi konsisten.

### Input User

```python
fungsi_input = input("Masukkan fungsi f(x): ")
x0 = float(input("Masukkan nilai awal x0: "))
x1 = float(input("Masukkan nilai awal x1: "))
maks_iterasi = int(input("Masukkan jumlah iterasi maksimum: "))
toleransi = float(input("Masukkan toleransi error (contoh 0.000001): "))
```

- Program meminta 5 parameter dari user: ekspresi fungsi, dua titik awal `x0` dan `x1`, batas iterasi maksimum, dan toleransi error.
- Ekspresi fungsi langsung diproses oleh `buat_fungsi()` dan disimpan sebagai objek fungsi `f`.

### Header Tabel Iterasi

```python
print("\n" + "=" * 95)
print(f"{'Iterasi':<10}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x2)':<15}{'Error':<15}")
print("=" * 95)
```

- Menyiapkan tampilan tabel iterasi dengan kolom: Iterasi, x0, x1, x2, f(x2), dan Error.
- Menggunakan f-string alignment (`:<10`, `:<15`) agar setiap kolom memiliki lebar tetap dan mudah dibaca.

### Loop Iterasi

```python
for i in range(1, maks_iterasi + 1):
    fx0 = f(x0)
    fx1 = f(x1)
    if fx1 - fx0 == 0:
        print("Terjadi pembagian dengan nol.")
        break
    x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
    fx2 = f(x2)
    error = abs(x2 - x1)
    print(f"{i:<10}{x0:<15.6f}{x1:<15.6f}{x2:<15.6f}{fx2:<15.6f}{error:<15.6f}")
    if error < toleransi or abs(fx2) < toleransi:
        akar = x2
        break
    x0 = x1
    x1 = x2
    akar = x2
```

- Setiap iterasi menghitung `f(x0)` dan `f(x1)`, lalu menerapkan rumus Secant untuk mendapatkan `x2`.
- Jika `f(x1) - f(x0) == 0`, iterasi dihentikan untuk mencegah pembagian dengan nol.
- Error dihitung dari selisih absolut `|x2 - x1|`.
- Iterasi berhenti jika `error < toleransi` atau `|f(x2)| < toleransi` (konvergen), atau jika batas iterasi maksimum tercapai.
- Nilai `x0` dan `x1` diperbarui setiap iterasi (`x0 = x1`, `x1 = x2`) untuk perhitungan berikutnya.
- `akar = x2` diperbarui di setiap iterasi agar jika loop habis tanpa break, nilai terakhir tetap tersimpan.

### Hasil Akhir

```python
if akar is not None:
    print(f"nilai akar = {akar:.6f}")
    print(f"nilai f(x): {f(akar):.6f}")
else:
    print("[!] Akar belum ditemukan.")
```
<<<<<<< HEAD
print(f"akar ditemukan: x = {akar:.6f}")
print(f"nilai f(x): {f(akar):.6f}")
```
* Menampilkan nilai akar yang ditemukan.
* Menampilkan nilai f(x) sebagai validasi.
=======

- Menampilkan nilai akar yang ditemukan beserta nilai `f(akar)` sebagai verifikasi (idealnya mendekati 0).
- Jika iterasi habis tanpa konvergen, program menampilkan pesan `[!] Akar belum ditemukan.`
>>>>>>> 8c40d871141a9a3087e239eb82866d6a524aebe8

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
Masukkan fungsi f(x): x**3 - x - 2
Masukkan nilai awal x0: 1
Masukkan nilai awal x1: 2
Masukkan jumlah iterasi maksimum: 10
Masukkan toleransi error (contoh 0.000001): 0.000001
```

### Contoh Output

```
===============================================================================================
Iterasi    x0             x1             x2             f(x2)          Error
===============================================================================================
1          1.000000       2.000000       1.333333       -0.962963      0.666667
2          1.333333       2.000000       1.462687       -0.333339      0.129353
...
===============================================================================================
nilai akar = 1.521380
nilai f(x): 0.000000
```

### Dependensi (Yang Dibutuhkan)

| Library  | Kegunaan                                   | Cara Install         |
| -------- | ------------------------------------------ | -------------------- |
| Python 3 | Bahasa pemrograman utama                   | python.org/downloads |
| math     | Fungsi matematika (sin, cos, log, dst)     | Sudah tersedia       |
| re       | Preprocessing ekspresi fungsi (built-in)   | Sudah tersedia       |

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
