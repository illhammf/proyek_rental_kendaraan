# Sistem Rental Kendaraan Berbasis Object-Oriented Programming

Proyek ini dibuat untuk tugas Bahasa Pemrograman menggunakan Python dan konsep Object-Oriented Programming.

## Tema
Sistem Rental Kendaraan Berbasis Object-Oriented Programming.

## Fitur Utama
1. Mengelola data mobil dan motor.
2. Mengelola data pelanggan.
3. Membuat transaksi penyewaan kendaraan.
4. Menghitung total biaya sewa secara otomatis.
5. Melakukan pengembalian kendaraan.
6. Menampilkan statistik rental.
7. Menyimpan data ke file JSON.
8. Membuat laporan TXT dan CSV.

## Cara Menjalankan
Buka folder proyek di VS Code, lalu jalankan:

```bash
python main.py
```

Jika menggunakan Windows dan perintah `python` tidak terbaca, gunakan:

```bash
py main.py
```

## Cara Testing

```bash
python tests/test_rental.py
```

## Struktur Folder

```text
Sistem_Rental_Kendaraan_OOP/
├── main.py
├── src/
│   ├── models/
│   │   ├── kendaraan.py
│   │   ├── pelanggan.py
│   │   └── transaksi.py
│   └── services/
│       ├── file_manager.py
│       ├── laporan.py
│       └── rental.py
├── data/
├── reports/
├── docs/
├── slides/
├── poster/
└── tests/
```

## Class Utama
- Kendaraan
- Mobil
- Motor
- Pelanggan
- Transaksi
- Rental
- FileManager
- Laporan

## Akun Login
Program ini tidak memakai login agar demo lebih cepat. Fokus utama proyek adalah penerapan OOP, bukan autentikasi.
