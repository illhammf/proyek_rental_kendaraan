# Laporan Proyek
## Sistem Rental Kendaraan Berbasis Object-Oriented Programming

## BAB I PENDAHULUAN

### 1.1 Latar Belakang
Rental kendaraan merupakan layanan yang menyediakan kendaraan untuk digunakan pelanggan dalam jangka waktu tertentu. Proses rental secara manual sering menimbulkan masalah. Data kendaraan sulit dipantau. Status kendaraan dapat tercatat ganda. Data pelanggan dan transaksi juga rentan hilang jika hanya dicatat pada buku atau lembar kerja sederhana.

Sistem rental kendaraan berbasis Python dapat membantu proses pencatatan tersebut. Sistem menyimpan data kendaraan, pelanggan, transaksi, dan laporan. Program ini dibangun menggunakan paradigma Object-Oriented Programming. Pendekatan OOP sesuai karena objek dalam sistem rental memiliki karakteristik dan perilaku yang jelas. Kendaraan, mobil, motor, pelanggan, dan transaksi dapat dimodelkan sebagai class.

### 1.2 Rumusan Masalah
1. Bagaimana merancang sistem rental kendaraan menggunakan konsep OOP?
2. Bagaimana menerapkan inheritance, encapsulation, polymorphism, composition, constructor, dan method pada Python?
3. Bagaimana membuat fitur penyewaan, pengembalian, penyimpanan data, dan laporan sederhana?

### 1.3 Tujuan
1. Membuat aplikasi rental kendaraan berbasis terminal menggunakan Python.
2. Menerapkan konsep OOP secara jelas dan terstruktur.
3. Menyediakan fitur pengelolaan kendaraan, pelanggan, transaksi, pengembalian, dan laporan.

## BAB II ANALISIS KEBUTUHAN

### 2.1 Kebutuhan Fungsional
Sistem harus dapat menambahkan kendaraan, menampilkan kendaraan, menambahkan pelanggan, menampilkan pelanggan, membuat transaksi sewa, menghitung biaya sewa, melakukan pengembalian, menyimpan data, memuat data, menampilkan statistik, dan membuat laporan.

### 2.2 Kebutuhan Nonfungsional
Sistem harus mudah dijalankan di VS Code. Sistem tidak memerlukan library eksternal. Data disimpan menggunakan JSON agar sederhana dan mudah diperiksa. Kode diberi komentar agar dapat dipahami oleh mahasiswa.

### 2.3 Aktor Sistem
Aktor utama adalah petugas rental. Petugas memasukkan data kendaraan, pelanggan, dan transaksi.

## BAB III PERANCANGAN SISTEM

### 3.1 Class yang Digunakan
Class utama yang digunakan yaitu Kendaraan, Mobil, Motor, Pelanggan, Transaksi, Rental, FileManager, dan Laporan.

### 3.2 Relasi Class
Mobil dan Motor mewarisi Kendaraan. Transaksi memiliki objek Pelanggan dan Kendaraan. Rental memiliki FileManager dan Laporan. Relasi tersebut menunjukkan inheritance dan composition.

### 3.3 Alur Program
Program dimulai dengan membuat objek Rental. Sistem memuat data dari file JSON. Jika belum ada data, sistem membuat data contoh. Pengguna memilih menu. Setiap menu menjalankan method sesuai kebutuhan. Saat keluar, data disimpan kembali ke JSON.

## BAB IV IMPLEMENTASI

### 4.1 Implementasi Class Kendaraan
Class Kendaraan menyimpan atribut umum seperti kode, merk, model, tahun, plat nomor, tarif harian, dan status. Atribut tarif, plat, dan status dienkapsulasi agar perubahan data tetap tervalidasi.

### 4.2 Implementasi Class Mobil dan Motor
Class Mobil dan Motor mewarisi Kendaraan. Keduanya mengoverride method hitung_biaya_sewa. Mobil dapat menambahkan biaya supir. Motor dapat menambahkan biaya helm.

### 4.3 Implementasi Class Pelanggan
Class Pelanggan menyimpan data penyewa. Data yang disimpan meliputi ID pelanggan, nama, nomor KTP, nomor HP, dan alamat.

### 4.4 Implementasi Class Transaksi
Class Transaksi menghubungkan pelanggan dengan kendaraan. Class ini menghitung total biaya, tanggal kembali, status transaksi, dan ringkasan transaksi.

### 4.5 Implementasi Class Rental
Class Rental menjadi pengelola utama. Class ini menyimpan daftar kendaraan, pelanggan, dan transaksi. Class ini juga menjalankan fitur tambah data, cari data, sewa kendaraan, pengembalian, simpan data, muat data, dan laporan.

## BAB V PENGUJIAN

Pengujian dilakukan menggunakan file `tests/test_rental.py`. Terdapat 5 skenario pengujian. Skenario tersebut menguji penambahan kendaraan, penambahan pelanggan, polymorphism biaya sewa, transaksi dan pengembalian, serta statistik.

## BAB VI KESIMPULAN

Sistem Rental Kendaraan Berbasis Object-Oriented Programming berhasil dibuat menggunakan Python. Program menerapkan class, object, inheritance, encapsulation, polymorphism, composition, constructor, dan method. Fitur utama berjalan sesuai kebutuhan, yaitu pengelolaan kendaraan, pelanggan, transaksi, pengembalian, penyimpanan data, statistik, dan laporan.
