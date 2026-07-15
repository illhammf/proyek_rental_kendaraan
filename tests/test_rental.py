"""Pengujian sederhana tanpa library tambahan.

Jalankan:
python tests/test_rental.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.models.kendaraan import Mobil, Motor
from src.models.pelanggan import Pelanggan
from src.services.rental import Rental


def test_tambah_kendaraan():
    rental = Rental("Test Rental")
    mobil = Mobil("M100", "Toyota", "Innova", 2022, "B 100 ABC", 500000, 7, "Automatic")
    assert rental.tambah_kendaraan(mobil) is True
    assert rental.tambah_kendaraan(mobil) is False


def test_tambah_pelanggan():
    rental = Rental("Test Rental")
    pelanggan = Pelanggan("P100", "Budi", "1234567890", "081234567890", "Depok")
    assert rental.tambah_pelanggan(pelanggan) is True
    assert rental.cari_pelanggan("P100").nama == "Budi"


def test_polymorphism_biaya():
    mobil = Mobil("M101", "Honda", "Brio", 2021, "B 101 ABC", 300000, 5, "Manual")
    motor = Motor("R101", "Yamaha", "NMAX", 2022, "B 102 ABC", 150000, "Matic", 155)
    assert mobil.hitung_biaya_sewa(2, pakai_supir=True) == 900000
    assert motor.hitung_biaya_sewa(2, tambah_helm=True) == 320000


def test_transaksi_dan_pengembalian():
    rental = Rental("Test Rental")
    rental.tambah_kendaraan(Motor("R200", "Honda", "Vario", 2023, "B 200 ABC", 90000, "Matic", 125))
    rental.tambah_pelanggan(Pelanggan("P200", "Sari", "1234567891", "081111111111", "Bekasi"))
    transaksi = rental.sewa_kendaraan("P200", "R200", 3)
    assert transaksi.total_biaya == 270000
    assert rental.cari_kendaraan("R200").status == "disewa"
    assert rental.kembalikan_kendaraan(transaksi.kode_transaksi) is True
    assert rental.cari_kendaraan("R200").status == "tersedia"


def test_statistik():
    rental = Rental("Test Rental")
    rental.buat_data_contoh()
    data = rental.statistik()
    assert data["total_kendaraan"] == 4
    assert data["kendaraan_tersedia"] == 4


if __name__ == "__main__":
    test_tambah_kendaraan()
    test_tambah_pelanggan()
    test_polymorphism_biaya()
    test_transaksi_dan_pengembalian()
    test_statistik()
    print("Semua 5 skenario pengujian berhasil.")
