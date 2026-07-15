# Pemetaan Konsep OOP

## Class
Proyek menggunakan lebih dari 6 class, yaitu Kendaraan, Mobil, Motor, Pelanggan, Transaksi, Rental, FileManager, dan Laporan.

## Object
Objek dibuat dari setiap class. Contohnya objek Mobil, Motor, Pelanggan, Transaksi, Rental, FileManager, dan Laporan.

## Inheritance
Mobil dan Motor merupakan class turunan dari Kendaraan.

## Encapsulation
Atribut penting memakai `_` dan `__`, misalnya `__plat_nomor`, `__tarif_harian`, `__status`, `__nama`, dan `__total_biaya`. Atribut tersebut diakses melalui property getter dan setter.

## Polymorphism
Method `hitung_biaya_sewa()` dan `tampil_info()` dioverride oleh class Mobil dan Motor. Mobil menghitung tambahan supir. Motor menghitung tambahan helm.

## Composition
Class Rental memiliki objek FileManager dan Laporan. Class Transaksi memiliki objek Pelanggan dan Kendaraan.

## Constructor
Setiap class utama menggunakan method `__init__()`.

## Method
Proyek memiliki lebih dari 20 method, antara lain tambah_kendaraan, tambah_pelanggan, cari_kendaraan, cari_pelanggan, sewa_kendaraan, kembalikan_kendaraan, batalkan_transaksi, simpan_data, muat_data, buat_semua_laporan, hitung_biaya_sewa, tampil_info, to_dict, from_dict, dan statistik.
