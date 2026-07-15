"""Model pelanggan rental kendaraan."""

from __future__ import annotations


class Pelanggan:
    """Class Pelanggan menyimpan identitas penyewa kendaraan."""

    def __init__(self, id_pelanggan: str, nama: str, no_ktp: str, no_hp: str, alamat: str) -> None:
        self.__id_pelanggan = id_pelanggan
        self.__nama = nama
        self.__no_ktp = no_ktp
        self.__no_hp = no_hp
        self.__alamat = alamat

    @property
    def id_pelanggan(self) -> str:
        return self.__id_pelanggan

    @property
    def nama(self) -> str:
        return self.__nama

    @nama.setter
    def nama(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Nama pelanggan tidak boleh kosong.")
        self.__nama = nilai.strip()

    @property
    def no_ktp(self) -> str:
        return self.__no_ktp

    @property
    def no_hp(self) -> str:
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, nilai: str) -> None:
        if len(nilai.strip()) < 10:
            raise ValueError("Nomor HP minimal 10 karakter.")
        self.__no_hp = nilai.strip()

    @property
    def alamat(self) -> str:
        return self.__alamat

    @alamat.setter
    def alamat(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Alamat tidak boleh kosong.")
        self.__alamat = nilai.strip()

    def update_kontak(self, no_hp: str, alamat: str) -> None:
        """Mengubah nomor HP dan alamat pelanggan."""
        self.no_hp = no_hp
        self.alamat = alamat

    def tampil_info(self) -> str:
        return f"{self.id_pelanggan} | {self.nama} | KTP: {self.no_ktp} | HP: {self.no_hp} | {self.alamat}"

    def to_dict(self) -> dict:
        return {
            "id_pelanggan": self.id_pelanggan,
            "nama": self.nama,
            "no_ktp": self.no_ktp,
            "no_hp": self.no_hp,
            "alamat": self.alamat,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Pelanggan":
        return cls(data["id_pelanggan"], data["nama"], data["no_ktp"], data["no_hp"], data["alamat"])
