# Praktikum 1 - Komputasi Numerik (Metode Regula Falsi)

Program ini dibuat dengan mengimplementasikan metode Regula Falsi untuk mencari akar persamaan,
dilengkapi dengan tampilan proses iterasi numerik dan grafik fungsinya.

## Persamaan yang Digunakan

f(x) = x³ - x - 2

Persamaan ini dipilih karena memiliki akar real yang dapat dicari
menggunakan metode Regula Falsi pada interval [1, 2].

## Cara Kerja Program

Program meminta user untuk memasukkan:
- Nilai x1 (batas kiri interval)
- Nilai x2 (batas kanan interval)  
- Jumlah iterasi yang diinginkan

Program akan menampilkan tabel iterasi di terminal dan grafik fungsi
beserta proses iterasinya secara visual.

## Hasil Kode

### Import Library

<img width="231" height="38" alt="Screenshot 2026-04-21 at 19 27 23" src="https://github.com/user-attachments/assets/338ef75c-e0c7-4a09-b7e7-0c70ff253820" />

* Memanggil dua toolkit yang dibutuhkan program. 
* matplotlib untuk urusan grafik. 
* numpy untuk urusan perhitungan matematika.

### Fungsi f(x)

<img width="231" height="35" alt="Screenshot 2026-04-21 at 19 27 37" src="https://github.com/user-attachments/assets/c880b96b-f04c-49c8-b910-24baa6334f36" />

* Mendefinisikan persamaan matematika yang digunakan.
* Setiap kali program perlu tahu nilai fungsi di titik tertentu, bagian ini yang dipanggil.

### Judul Program

<img width="429" height="89" alt="Screenshot 2026-04-21 at 19 27 54" src="https://github.com/user-attachments/assets/55b3b356-ddcc-4677-90e5-30ec5f03bb74" />

* Menampilkan header program di terminal saat pertama dijalankan.
* Biar tampilannya rapi dan informatif.

### Input User

<img width="405" height="52" alt="Screenshot 2026-04-21 at 19 28 15" src="https://github.com/user-attachments/assets/cacf8d72-01b0-46f0-bd05-c7e1c785bed4" />

* Program meminta tiga informasi dari pengguna.
* batas kiri, batas kanan, dan jumlah iterasi yang diinginkan.

### Validasi

<img width="489" height="60" alt="Screenshot 2026-04-21 at 19 28 36" src="https://github.com/user-attachments/assets/672b2b38-2cd8-4b31-a397-143d38ebc387" />

* Sebelum mulai menghitung, program mengecek apakah interval yang dimasukkan valid.
* Kalau f(x1) dan f(x2) tandanya sama, tidak ada akar di situ dan program memberi peringatan.

### Persiapan Iterasi

<img width="789" height="96" alt="Screenshot 2026-04-21 at 19 29 12" src="https://github.com/user-attachments/assets/00ae05e7-bcf0-45e6-bdb6-de43868b6cab" />

* Menyiapkan tempat penyimpanan data iterasi.
* Menginisialisasi x3_lama sebagai None karena belum ada iterasi sebelumnya.
* Lalu mencetak header tabel.

### Loop Iterasi

<img width="375" height="55" alt="Screenshot 2026-04-21 at 19 29 39" src="https://github.com/user-attachments/assets/05fad986-d13d-4822-a9e0-03c663443409" />

* Bagian inti program.
* Setiap putaran menghitung x3 baru menggunakan rumus Regula Falsi.
* Semakin banyak iterasi, semakin mendekati akar yang sebenarnya.

### Perhitungan Error

<img width="306" height="99" alt="Screenshot 2026-04-21 at 19 30 05" src="https://github.com/user-attachments/assets/54ea850e-eff4-4c56-8dfb-4dc68cdf60c9" />

* Mengukur seberapa besar perubahan x3 dibanding iterasi sebelumnya.
* Semakin kecil errornya, semakin dekat ke akar yang sebenarnya.

### Tampilkan Tabel

<img width="749" height="41" alt="Screenshot 2026-04-21 at 19 30 29" src="https://github.com/user-attachments/assets/1f8ae1b8-1fe8-405b-90cf-9d953f4aba4c" />

* Mencetak satu baris tabel untuk iterasi ke-i .
* Lalu menyimpan data x1, x2, x3 untuk keperluan grafik nanti.

### Update Interval

<img width="171" height="117" alt="Screenshot 2026-04-21 at 19 30 57" src="https://github.com/user-attachments/assets/ac24e530-027d-4b1a-9e13-e52c1c3fa4ac" />

* Memperbarui interval berdasarkan posisi akar. 
* Kalau akar ada di kiri, x2 digeser ke x3.
* Kalau di kanan, x1 digeser ke x3.
* Lalu x3 disimpan sebagai pembanding iterasi berikutnya.

### Hasil Akhir

<img width="498" height="49" alt="Screenshot 2026-04-21 at 19 31 17" src="https://github.com/user-attachments/assets/86c74ca9-9572-4e71-9186-164d8d54909c" />

* Setelah semua iterasi selesai, menampilkan estimasi akar terbaik yang didapat beserta nilai fungsinya.

### Persiapan Grafik

<img width="391" height="71" alt="Screenshot 2026-04-21 at 19 31 57" src="https://github.com/user-attachments/assets/6cf59a62-ec13-4568-a0c5-2a68505e23bf" />

* Membuat 500 titik koordinat untuk menggambar kurva yang mulus.
* Lalu menyiapkan kanvas/tampilan dengan dua grafik berdampingan.

### Grafik Kiri

<img width="424" height="126" alt="Screenshot 2026-04-21 at 19 32 30" src="https://github.com/user-attachments/assets/18b869c2-116b-433d-8e93-fcce95eb4d87" />

* Menggambar kurva f(x) lengkap di grafik kiri.
* Akan terlihat jelas di mana kurva memotong sumbu X, maka disitulah letak akarnya.

### Grafik Kanan

<img width="575" height="105" alt="Screenshot 2026-04-21 at 19 33 14" src="https://github.com/user-attachments/assets/18cd6405-185b-443c-9dab-39e266e390fc" />

* Menggambar proses iterasi di grafik kanan.
* Setiap iterasi ditampilkan dengan warna berbeda.
* Sehingga terlihat bagaimana garis Regula Falsi semakin mendekati akar.

### Tampilkan Grafik

<img width="323" height="119" alt="Screenshot 2026-04-21 at 19 33 49" src="https://github.com/user-attachments/assets/d06849f4-f2bb-40a2-ba42-ec46272af4ea" />

* Mengatur jarak antar grafik agar tidak tumpang tindih.
* Lalu menampilkan kedua grafik ke layar.

## Cara Menjalankan

Pastikan Python 3 dan matplotlib sudah terinstall:

pip3 install matplotlib

Jalankan program:

python3 praktikum1regulafalsi.py

Contoh input:
- x1 = 1
- x2 = 2
- iterasi = 5

## Contoh Output

Setelah 5 iterasi, estimasi akar yang didapat adalah x ≈ 1.5199
dengan nilai f(1.5199) ≈ -0.008675 (mendekati 0).

## Cara Menjalankan

### 1. Clone repo

    git clone https://github.com/novldrsh/praktikumkomnum1.git

### 2. Masuk folder

    cd praktikumkomnum1

### 3. Jalankan program

    python3 praktikum1regulafalsi.py

### 4. Contoh Input 

    x1 = 1
    x2 = 2
    iterasi = 5

---

## Contoh Output

    ==============================================================================================================
    Iterasi    x1           x2           x3           f(x3)        Error Abs      Error Rel
    ==============================================================================================================
    1          1.000000     2.000000     1.333333     -0.962963    0.000000       0.000000
    2          1.333333     2.000000     1.462687     -0.333339    0.129353       0.088435
    3          1.462687     2.000000     1.504019     -0.101818    0.041332       0.027481
    4          1.504019     2.000000     1.516331     -0.029895    0.012312       0.008119
    5          1.516331     2.000000     1.519919     -0.008675    0.003588       0.002361
    ==============================================================================================================

    [✓] Estimasi akar setelah 5 iterasi: x = 1.519919

---

## Dependensi (Yang Dibutuhkan)

| Library    | Kegunaan                       | Cara Install                |
|------------|--------------------------------|-----------------------------|
| Python 3   | Bahasa pemrograman utama       | python.org/downloads        |
| matplotlib | Menampilkan grafik             | pip3 install matplotlib     |
| numpy      | Perhitungan matematika & array | Otomatis bersama matplotlib |

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
