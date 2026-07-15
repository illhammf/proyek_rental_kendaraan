"""Model kendaraan untuk Sistem Rental Kendaraan.

File ini sengaja diberi komentar agar mudah dipelajari.
Konsep OOP yang terlihat:
1. Class: Kendaraan, Mobil, Motor.
2. Inheritance: Mobil dan Motor mewarisi Kendaraan.
3. Encapsulation: beberapa atribut memakai awalan _ dan __ serta diakses lewat property.
4. Polymorphism: method hitung_biaya_sewa() dan tampil_info() dioverride pada class turunan.
"""

from __future__ import annotations


class Kendaraan:
    """Class induk untuk semua jenis kendaraan.

    Kendaraan tidak dibuat terlalu abstrak agar mahasiswa tetap mudah memahami alur program.
    Class ini menyimpan data umum yang dimiliki mobil maupun motor.
    """

    def __init__(
        self,
        kode: str,
        merk: str,
        model: str,
        tahun: int,
        plat_nomor: str,
        tarif_harian: int,
        status: str = "tersedia",
    ) -> None:
        self._kode = kode
        self._merk = merk
        self._model = model
        self._tahun = tahun
        self.__plat_nomor = plat_nomor
        self.__tarif_harian = 0
        self.__status = "tersedia"
        self.tarif_harian = tarif_harian
        self.status = status

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def merk(self) -> str:
        return self._merk

    @merk.setter
    def merk(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Merk kendaraan tidak boleh kosong.")
        self._merk = nilai.strip()

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Model kendaraan tidak boleh kosong.")
        self._model = nilai.strip()

    @property
    def tahun(self) -> int:
        return self._tahun

    @tahun.setter
    def tahun(self, nilai: int) -> None:
        if nilai < 1990:
            raise ValueError("Tahun kendaraan terlalu lama untuk data rental.")
        self._tahun = nilai

    @property
    def plat_nomor(self) -> str:
        return self.__plat_nomor

    @plat_nomor.setter
    def plat_nomor(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Plat nomor tidak boleh kosong.")
        self.__plat_nomor = nilai.strip().upper()

    @property
    def tarif_harian(self) -> int:
        return self.__tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai < 0:
            raise ValueError("Tarif harian tidak boleh negatif.")
        self.__tarif_harian = int(nilai)

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, nilai: str) -> None:
        nilai = nilai.lower().strip()
        if nilai not in {"tersedia", "disewa", "servis"}:
            raise ValueError("Status kendaraan harus tersedia, disewa, atau servis.")
        self.__status = nilai

    def ubah_status(self, status_baru: str) -> None:
        """Mengubah status kendaraan."""
        self.status = status_baru

    def apakah_tersedia(self) -> bool:
        """Mengembalikan True jika kendaraan siap disewa."""
        return self.status == "tersedia"

    def hitung_biaya_sewa(self, lama_hari: int, **opsi: object) -> int:
        """Menghitung biaya sewa standar.

        Method ini akan dioverride oleh Mobil dan Motor.
        """
        if lama_hari <= 0:
            raise ValueError("Lama sewa minimal 1 hari.")
        return self.tarif_harian * lama_hari

    def tampil_info(self) -> str:
        """Menampilkan informasi kendaraan dalam format teks."""
        return (
            f"{self.kode} | {self.merk} {self.model} | {self.tahun} | "
            f"{self.plat_nomor} | Rp{self.tarif_harian:,}/hari | {self.status}"
        )

    def to_dict(self) -> dict:
        """Mengubah objek menjadi dictionary agar bisa disimpan ke JSON."""
        return {
            "jenis": "Kendaraan",
            "kode": self.kode,
            "merk": self.merk,
            "model": self.model,
            "tahun": self.tahun,
            "plat_nomor": self.plat_nomor,
            "tarif_harian": self.tarif_harian,
            "status": self.status,
        }


class Mobil(Kendaraan):
    """Class turunan untuk kendaraan berjenis mobil."""

    def __init__(
        self,
        kode: str,
        merk: str,
        model: str,
        tahun: int,
        plat_nomor: str,
        tarif_harian: int,
        jumlah_kursi: int,
        tipe_transmisi: str,
        biaya_supir_per_hari: int = 150000,
        status: str = "tersedia",
    ) -> None:
        super().__init__(kode, merk, model, tahun, plat_nomor, tarif_harian, status)
        self.__jumlah_kursi = jumlah_kursi
        self.__tipe_transmisi = tipe_transmisi
        self.__biaya_supir_per_hari = biaya_supir_per_hari

    @property
    def jumlah_kursi(self) -> int:
        return self.__jumlah_kursi

    @property
    def tipe_transmisi(self) -> str:
        return self.__tipe_transmisi

    @property
    def biaya_supir_per_hari(self) -> int:
        return self.__biaya_supir_per_hari

    def hitung_biaya_sewa(self, lama_hari: int, pakai_supir: bool = False, **opsi: object) -> int:
        """Override method dari Kendaraan.

        Mobil bisa memiliki tambahan biaya supir.
        """
        total = super().hitung_biaya_sewa(lama_hari)
        if pakai_supir:
            total += self.biaya_supir_per_hari * lama_hari
        return total

    def tampil_info(self) -> str:
        return (
            f"[MOBIL] {super().tampil_info()} | Kursi: {self.jumlah_kursi} | "
            f"Transmisi: {self.tipe_transmisi}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "jenis": "Mobil",
                "jumlah_kursi": self.jumlah_kursi,
                "tipe_transmisi": self.tipe_transmisi,
                "biaya_supir_per_hari": self.biaya_supir_per_hari,
            }
        )
        return data


class Motor(Kendaraan):
    """Class turunan untuk kendaraan berjenis motor."""

    def __init__(
        self,
        kode: str,
        merk: str,
        model: str,
        tahun: int,
        plat_nomor: str,
        tarif_harian: int,
        jenis_motor: str,
        kapasitas_cc: int,
        biaya_helm: int = 10000,
        status: str = "tersedia",
    ) -> None:
        super().__init__(kode, merk, model, tahun, plat_nomor, tarif_harian, status)
        self.__jenis_motor = jenis_motor
        self.__kapasitas_cc = kapasitas_cc
        self.__biaya_helm = biaya_helm

    @property
    def jenis_motor(self) -> str:
        return self.__jenis_motor

    @property
    def kapasitas_cc(self) -> int:
        return self.__kapasitas_cc

    @property
    def biaya_helm(self) -> int:
        return self.__biaya_helm

    def hitung_biaya_sewa(self, lama_hari: int, tambah_helm: bool = False, **opsi: object) -> int:
        """Override method dari Kendaraan.

        Motor bisa memiliki tambahan biaya helm cadangan.
        """
        total = super().hitung_biaya_sewa(lama_hari)
        if tambah_helm:
            total += self.biaya_helm * lama_hari
        return total

    def tampil_info(self) -> str:
        return (
            f"[MOTOR] {super().tampil_info()} | Jenis: {self.jenis_motor} | "
            f"CC: {self.kapasitas_cc}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "jenis": "Motor",
                "jenis_motor": self.jenis_motor,
                "kapasitas_cc": self.kapasitas_cc,
                "biaya_helm": self.biaya_helm,
            }
        )
        return data


def kendaraan_from_dict(data: dict) -> Kendaraan:
    """Factory function untuk membuat objek kendaraan dari data JSON."""
    jenis = data.get("jenis")
    if jenis == "Mobil":
        return Mobil(
            data["kode"], data["merk"], data["model"], data["tahun"], data["plat_nomor"],
            data["tarif_harian"], data.get("jumlah_kursi", 4), data.get("tipe_transmisi", "Manual"),
            data.get("biaya_supir_per_hari", 150000), data.get("status", "tersedia")
        )
    if jenis == "Motor":
        return Motor(
            data["kode"], data["merk"], data["model"], data["tahun"], data["plat_nomor"],
            data["tarif_harian"], data.get("jenis_motor", "Matic"), data.get("kapasitas_cc", 125),
            data.get("biaya_helm", 10000), data.get("status", "tersedia")
        )
    return Kendaraan(
        data["kode"], data["merk"], data["model"], data["tahun"], data["plat_nomor"],
        data["tarif_harian"], data.get("status", "tersedia")
    )
