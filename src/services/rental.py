"""Class utama untuk mengelola seluruh proses rental kendaraan."""

from __future__ import annotations
from datetime import date
from src.models.kendaraan import Kendaraan, Mobil, Motor, kendaraan_from_dict
from src.models.pelanggan import Pelanggan
from src.models.transaksi import Transaksi
from src.services.file_manager import FileManager
from src.services.laporan import Laporan


class Rental:
    """Class inti aplikasi.

    Composition terlihat karena Rental memiliki FileManager, Laporan, daftar Kendaraan,
    daftar Pelanggan, dan daftar Transaksi.
    """

    def __init__(self, nama_rental: str = "Rental Jaya") -> None:
        self.nama_rental = nama_rental
        self.file_manager = FileManager()
        self.laporan = Laporan()
        self.daftar_kendaraan: list[Kendaraan] = []
        self.daftar_pelanggan: list[Pelanggan] = []
        self.daftar_transaksi: list[Transaksi] = []

    def tambah_kendaraan(self, kendaraan: Kendaraan) -> bool:
        if self.cari_kendaraan(kendaraan.kode):
            return False
        self.daftar_kendaraan.append(kendaraan)
        return True

    def tambah_pelanggan(self, pelanggan: Pelanggan) -> bool:
        if self.cari_pelanggan(pelanggan.id_pelanggan):
            return False
        self.daftar_pelanggan.append(pelanggan)
        return True

    def cari_kendaraan(self, kode: str) -> Kendaraan | None:
        for kendaraan in self.daftar_kendaraan:
            if kendaraan.kode.lower() == kode.lower():
                return kendaraan
        return None

    def cari_pelanggan(self, id_pelanggan: str) -> Pelanggan | None:
        for pelanggan in self.daftar_pelanggan:
            if pelanggan.id_pelanggan.lower() == id_pelanggan.lower():
                return pelanggan
        return None

    def cari_transaksi(self, kode_transaksi: str) -> Transaksi | None:
        for transaksi in self.daftar_transaksi:
            if transaksi.kode_transaksi.lower() == kode_transaksi.lower():
                return transaksi
        return None

    def filter_kendaraan_tersedia(self) -> list[Kendaraan]:
        return [kendaraan for kendaraan in self.daftar_kendaraan if kendaraan.apakah_tersedia()]

    def filter_kendaraan_disewa(self) -> list[Kendaraan]:
        return [kendaraan for kendaraan in self.daftar_kendaraan if kendaraan.status == "disewa"]

    def buat_kode_transaksi(self) -> str:
        nomor = len(self.daftar_transaksi) + 1
        return f"TRX{nomor:04d}"

    def sewa_kendaraan(
        self,
        id_pelanggan: str,
        kode_kendaraan: str,
        lama_hari: int,
        opsi_tambahan: dict | None = None,
    ) -> Transaksi:
        pelanggan = self.cari_pelanggan(id_pelanggan)
        kendaraan = self.cari_kendaraan(kode_kendaraan)
        if pelanggan is None:
            raise ValueError("Pelanggan tidak ditemukan.")
        if kendaraan is None:
            raise ValueError("Kendaraan tidak ditemukan.")
        if not kendaraan.apakah_tersedia():
            raise ValueError("Kendaraan tidak tersedia untuk disewa.")
        transaksi = Transaksi(
            self.buat_kode_transaksi(), pelanggan, kendaraan, str(date.today()), lama_hari, opsi_tambahan or {}
        )
        kendaraan.ubah_status("disewa")
        self.daftar_transaksi.append(transaksi)
        return transaksi

    def kembalikan_kendaraan(self, kode_transaksi: str) -> bool:
        transaksi = self.cari_transaksi(kode_transaksi)
        if transaksi is None or transaksi.status != "aktif":
            return False
        transaksi.selesaikan()
        return True

    def batalkan_transaksi(self, kode_transaksi: str) -> bool:
        transaksi = self.cari_transaksi(kode_transaksi)
        if transaksi is None or transaksi.status != "aktif":
            return False
        transaksi.batalkan()
        return True

    def hapus_kendaraan(self, kode: str) -> bool:
        kendaraan = self.cari_kendaraan(kode)
        if kendaraan is None or kendaraan.status == "disewa":
            return False
        self.daftar_kendaraan.remove(kendaraan)
        return True

    def hapus_pelanggan(self, id_pelanggan: str) -> bool:
        pelanggan = self.cari_pelanggan(id_pelanggan)
        if pelanggan is None:
            return False
        self.daftar_pelanggan.remove(pelanggan)
        return True

    def tampilkan_semua_kendaraan(self) -> list[str]:
        return [kendaraan.tampil_info() for kendaraan in self.daftar_kendaraan]

    def tampilkan_semua_pelanggan(self) -> list[str]:
        return [pelanggan.tampil_info() for pelanggan in self.daftar_pelanggan]

    def tampilkan_semua_transaksi(self) -> list[str]:
        return [transaksi.ringkasan() for transaksi in self.daftar_transaksi]

    def simpan_data(self) -> None:
        self.file_manager.simpan_json("kendaraan.json", [item.to_dict() for item in self.daftar_kendaraan])
        self.file_manager.simpan_json("pelanggan.json", [item.to_dict() for item in self.daftar_pelanggan])
        self.file_manager.simpan_json("transaksi.json", [item.to_dict() for item in self.daftar_transaksi])

    def muat_data(self) -> None:
        self.daftar_kendaraan = [kendaraan_from_dict(data) for data in self.file_manager.baca_json("kendaraan.json", [])]
        self.daftar_pelanggan = [Pelanggan.from_dict(data) for data in self.file_manager.baca_json("pelanggan.json", [])]
        self.daftar_transaksi = []
        for data in self.file_manager.baca_json("transaksi.json", []):
            pelanggan = self.cari_pelanggan(data["id_pelanggan"])
            kendaraan = self.cari_kendaraan(data["kode_kendaraan"])
            if pelanggan and kendaraan:
                self.daftar_transaksi.append(Transaksi.from_dict(data, pelanggan, kendaraan))

    def buat_data_contoh(self) -> None:
        """Data contoh agar demo pertama langsung bisa dijalankan."""
        if self.daftar_kendaraan or self.daftar_pelanggan:
            return
        self.tambah_kendaraan(Mobil("M001", "Toyota", "Avanza", 2022, "B 1234 TKA", 350000, 7, "Manual"))
        self.tambah_kendaraan(Mobil("M002", "Honda", "Brio", 2021, "B 4421 BRI", 300000, 5, "Automatic"))
        self.tambah_kendaraan(Motor("R001", "Honda", "Vario", 2023, "B 7788 VRO", 90000, "Matic", 125))
        self.tambah_kendaraan(Motor("R002", "Yamaha", "NMAX", 2022, "B 9911 NMX", 150000, "Matic", 155))
        self.tambah_pelanggan(Pelanggan("P001", "Andi Saputra", "3671010101010001", "081234567890", "Tangerang"))
        self.tambah_pelanggan(Pelanggan("P002", "Siti Aminah", "3671010101010002", "082233445566", "Jakarta"))

    def buat_semua_laporan(self) -> list[str]:
        hasil = [
            self.laporan.buat_laporan_kendaraan(self.daftar_kendaraan),
            self.laporan.buat_laporan_transaksi(self.daftar_transaksi),
            self.laporan.buat_laporan_csv(self.daftar_transaksi),
        ]
        return [str(path) for path in hasil]

    def statistik(self) -> dict:
        return self.laporan.statistik_ringkas(self.daftar_kendaraan, self.daftar_transaksi)
