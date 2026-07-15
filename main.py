"""Program utama Sistem Rental Kendaraan berbasis OOP.

Cara menjalankan di VS Code:
1. Buka folder proyek ini.
2. Jalankan terminal.
3. Ketik: python main.py
"""

from src.models.kendaraan import Mobil, Motor
from src.models.pelanggan import Pelanggan
from src.services.rental import Rental


def garis() -> None:
    print("-" * 70)


def input_int(pesan: str, default: int = 0) -> int:
    """Fungsi kecil untuk membaca angka dari user dengan aman."""
    try:
        return int(input(pesan))
    except ValueError:
        return default


def tampilkan_list(judul: str, data: list[str]) -> None:
    print(f"\n{judul}")
    garis()
    if not data:
        print("Data masih kosong.")
    for item in data:
        print(item)


def menu_tambah_kendaraan(rental: Rental) -> None:
    print("\nTambah Kendaraan")
    jenis = input("Jenis kendaraan [mobil/motor]: ").strip().lower()
    kode = input("Kode kendaraan: ").strip().upper()
    merk = input("Merk: ").strip()
    model = input("Model: ").strip()
    tahun = input_int("Tahun: ")
    plat = input("Plat nomor: ").strip()
    tarif = input_int("Tarif harian: ")

    if jenis == "mobil":
        kursi = input_int("Jumlah kursi: ")
        transmisi = input("Tipe transmisi: ").strip()
        kendaraan = Mobil(kode, merk, model, tahun, plat, tarif, kursi, transmisi)
    elif jenis == "motor":
        jenis_motor = input("Jenis motor: ").strip()
        cc = input_int("Kapasitas CC: ")
        kendaraan = Motor(kode, merk, model, tahun, plat, tarif, jenis_motor, cc)
    else:
        print("Jenis kendaraan tidak valid.")
        return

    if rental.tambah_kendaraan(kendaraan):
        print("Kendaraan berhasil ditambahkan.")
    else:
        print("Kode kendaraan sudah terdaftar.")


def menu_tambah_pelanggan(rental: Rental) -> None:
    print("\nTambah Pelanggan")
    id_pelanggan = input("ID pelanggan: ").strip().upper()
    nama = input("Nama: ").strip()
    no_ktp = input("No KTP: ").strip()
    no_hp = input("No HP: ").strip()
    alamat = input("Alamat: ").strip()
    pelanggan = Pelanggan(id_pelanggan, nama, no_ktp, no_hp, alamat)
    if rental.tambah_pelanggan(pelanggan):
        print("Pelanggan berhasil ditambahkan.")
    else:
        print("ID pelanggan sudah terdaftar.")


def menu_sewa(rental: Rental) -> None:
    print("\nSewa Kendaraan")
    tampilkan_list("Kendaraan Tersedia", [item.tampil_info() for item in rental.filter_kendaraan_tersedia()])
    id_pelanggan = input("ID pelanggan: ").strip().upper()
    kode_kendaraan = input("Kode kendaraan: ").strip().upper()
    lama = input_int("Lama sewa hari: ", 1)
    opsi = {}
    kendaraan = rental.cari_kendaraan(kode_kendaraan)
    if kendaraan and kendaraan.__class__.__name__ == "Mobil":
        opsi["pakai_supir"] = input("Pakai supir? [y/t]: ").strip().lower() == "y"
    if kendaraan and kendaraan.__class__.__name__ == "Motor":
        opsi["tambah_helm"] = input("Tambah helm cadangan? [y/t]: ").strip().lower() == "y"
    try:
        transaksi = rental.sewa_kendaraan(id_pelanggan, kode_kendaraan, lama, opsi)
        print("Transaksi berhasil dibuat:")
        print(transaksi.ringkasan())
    except ValueError as error:
        print(f"Gagal membuat transaksi: {error}")


def menu_pengembalian(rental: Rental) -> None:
    print("\nPengembalian Kendaraan")
    tampilkan_list("Daftar Transaksi", rental.tampilkan_semua_transaksi())
    kode = input("Kode transaksi yang selesai: ").strip().upper()
    if rental.kembalikan_kendaraan(kode):
        print("Transaksi selesai. Kendaraan kembali tersedia.")
    else:
        print("Transaksi tidak ditemukan atau tidak aktif.")


def menu_statistik(rental: Rental) -> None:
    print("\nStatistik Rental")
    garis()
    for kunci, nilai in rental.statistik().items():
        print(f"{kunci}: {nilai}")


def main() -> None:
    rental = Rental("Sistem Rental Kendaraan OOP")
    rental.muat_data()
    rental.buat_data_contoh()

    while True:
        print("\nSISTEM RENTAL KENDARAAN BERBASIS OOP")
        garis()
        print("1. Lihat kendaraan")
        print("2. Tambah kendaraan")
        print("3. Lihat pelanggan")
        print("4. Tambah pelanggan")
        print("5. Sewa kendaraan")
        print("6. Pengembalian kendaraan")
        print("7. Lihat transaksi")
        print("8. Statistik")
        print("9. Buat laporan")
        print("10. Simpan data")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_list("Daftar Kendaraan", rental.tampilkan_semua_kendaraan())
        elif pilihan == "2":
            menu_tambah_kendaraan(rental)
        elif pilihan == "3":
            tampilkan_list("Daftar Pelanggan", rental.tampilkan_semua_pelanggan())
        elif pilihan == "4":
            menu_tambah_pelanggan(rental)
        elif pilihan == "5":
            menu_sewa(rental)
        elif pilihan == "6":
            menu_pengembalian(rental)
        elif pilihan == "7":
            tampilkan_list("Daftar Transaksi", rental.tampilkan_semua_transaksi())
        elif pilihan == "8":
            menu_statistik(rental)
        elif pilihan == "9":
            for path in rental.buat_semua_laporan():
                print(f"Laporan dibuat: {path}")
        elif pilihan == "10":
            rental.simpan_data()
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            rental.simpan_data()
            print("Data disimpan. Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()
