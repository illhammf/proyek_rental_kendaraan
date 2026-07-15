"""Model transaksi penyewaan kendaraan."""

from __future__ import annotations
from datetime import date, datetime, timedelta
from .kendaraan import Kendaraan
from .pelanggan import Pelanggan


class Transaksi:
    """Class Transaksi menghubungkan pelanggan dengan kendaraan yang disewa.

    Ini adalah contoh composition. Objek Transaksi memiliki objek Pelanggan dan objek Kendaraan.
    """

    def __init__(
        self,
        kode_transaksi: str,
        pelanggan: Pelanggan,
        kendaraan: Kendaraan,
        tanggal_pinjam: str,
        lama_hari: int,
        opsi_tambahan: dict | None = None,
        status: str = "aktif",
    ) -> None:
        self.__kode_transaksi = kode_transaksi
        self.__pelanggan = pelanggan
        self.__kendaraan = kendaraan
        self.__tanggal_pinjam = tanggal_pinjam
        self.__lama_hari = lama_hari
        self.__opsi_tambahan = opsi_tambahan or {}
        self.__status = status
        self.__total_biaya = self.hitung_total_biaya()

    @property
    def kode_transaksi(self) -> str:
        return self.__kode_transaksi

    @property
    def pelanggan(self) -> Pelanggan:
        return self.__pelanggan

    @property
    def kendaraan(self) -> Kendaraan:
        return self.__kendaraan

    @property
    def tanggal_pinjam(self) -> str:
        return self.__tanggal_pinjam

    @property
    def lama_hari(self) -> int:
        return self.__lama_hari

    @property
    def opsi_tambahan(self) -> dict:
        return self.__opsi_tambahan

    @property
    def status(self) -> str:
        return self.__status

    @property
    def total_biaya(self) -> int:
        return self.__total_biaya

    def hitung_total_biaya(self) -> int:
        """Menghitung total biaya memakai polymorphism pada objek kendaraan."""
        return self.kendaraan.hitung_biaya_sewa(self.lama_hari, **self.opsi_tambahan)

    def tanggal_kembali(self) -> str:
        """Menghitung tanggal pengembalian berdasarkan lama sewa."""
        awal = datetime.strptime(self.tanggal_pinjam, "%Y-%m-%d").date()
        return str(awal + timedelta(days=self.lama_hari))

    def selesaikan(self) -> None:
        """Menandai transaksi selesai."""
        self.__status = "selesai"
        self.kendaraan.ubah_status("tersedia")

    def batalkan(self) -> None:
        """Membatalkan transaksi aktif."""
        self.__status = "batal"
        self.kendaraan.ubah_status("tersedia")

    def ringkasan(self) -> str:
        return (
            f"{self.kode_transaksi} | {self.pelanggan.nama} menyewa {self.kendaraan.merk} "
            f"{self.kendaraan.model} selama {self.lama_hari} hari | "
            f"Kembali: {self.tanggal_kembali()} | Total: Rp{self.total_biaya:,} | {self.status}"
        )

    def to_dict(self) -> dict:
        return {
            "kode_transaksi": self.kode_transaksi,
            "id_pelanggan": self.pelanggan.id_pelanggan,
            "kode_kendaraan": self.kendaraan.kode,
            "tanggal_pinjam": self.tanggal_pinjam,
            "lama_hari": self.lama_hari,
            "opsi_tambahan": self.opsi_tambahan,
            "status": self.status,
            "total_biaya": self.total_biaya,
        }

    @classmethod
    def from_dict(cls, data: dict, pelanggan: Pelanggan, kendaraan: Kendaraan) -> "Transaksi":
        return cls(
            data["kode_transaksi"], pelanggan, kendaraan, data["tanggal_pinjam"],
            data["lama_hari"], data.get("opsi_tambahan", {}), data.get("status", "aktif")
        )
