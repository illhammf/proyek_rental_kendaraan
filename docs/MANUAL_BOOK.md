# Manual Book Sistem Rental Kendaraan OOP

## 1. Persiapan
Pastikan Python sudah terpasang pada komputer. Proyek ini dapat dijalankan di VS Code tanpa instalasi library tambahan.

## 2. Menjalankan Program
1. Buka VS Code.
2. Pilih menu File > Open Folder.
3. Pilih folder `Sistem_Rental_Kendaraan_OOP`.
4. Buka terminal.
5. Jalankan perintah `python main.py`.

## 3. Menu Program
Program memiliki menu berbasis terminal.

### 1. Lihat kendaraan
Menampilkan seluruh kendaraan yang tersimpan, baik mobil maupun motor.

### 2. Tambah kendaraan
Menambahkan kendaraan baru. Pengguna dapat memilih jenis mobil atau motor.

### 3. Lihat pelanggan
Menampilkan data pelanggan rental.

### 4. Tambah pelanggan
Menambahkan identitas pelanggan baru.

### 5. Sewa kendaraan
Membuat transaksi penyewaan kendaraan. Sistem hanya mengizinkan kendaraan dengan status tersedia.

### 6. Pengembalian kendaraan
Menyelesaikan transaksi aktif dan mengubah status kendaraan menjadi tersedia.

### 7. Lihat transaksi
Menampilkan seluruh transaksi rental.

### 8. Statistik
Menampilkan ringkasan jumlah kendaraan, kendaraan tersedia, kendaraan disewa, total transaksi, dan pendapatan dari transaksi selesai.

### 9. Buat laporan
Menghasilkan laporan kendaraan, transaksi TXT, dan transaksi CSV pada folder `reports`.

### 10. Simpan data
Menyimpan data kendaraan, pelanggan, dan transaksi ke folder `data` dalam format JSON.

### 0. Keluar
Menyimpan data lalu menutup program.

## 4. Catatan Penggunaan
- Gunakan kode kendaraan unik, misalnya M001 untuk mobil dan R001 untuk motor.
- Gunakan ID pelanggan unik, misalnya P001.
- Lama sewa minimal 1 hari.
- Kendaraan yang sedang disewa tidak dapat disewa lagi sebelum dikembalikan.
