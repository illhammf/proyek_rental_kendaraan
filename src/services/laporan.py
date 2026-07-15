"""Service laporan untuk rental kendaraan."""

from __future__ import annotations
from pathlib import Path


class Laporan:
    """Class ini bertugas menghasilkan laporan dalam format TXT dan CSV sederhana."""

    def __init__(self, folder_laporan: str = "reports") -> None:
        self.folder_laporan = Path(folder_laporan)
        self.folder_laporan.mkdir(parents=True, exist_ok=True)

    def buat_laporan_kendaraan(self, kendaraan: list) -> Path:
        path = self.folder_laporan / "laporan_kendaraan.txt"
        with path.open("w", encoding="utf-8") as file:
            file.write("LAPORAN DATA KENDARAAN\n")
            file.write("=" * 70 + "\n")
            for item in kendaraan:
                file.write(item.tampil_info() + "\n")
        return path

    def buat_laporan_transaksi(self, transaksi: list) -> Path:
        path = self.folder_laporan / "laporan_transaksi.txt"
        with path.open("w", encoding="utf-8") as file:
            file.write("LAPORAN TRANSAKSI RENTAL\n")
            file.write("=" * 70 + "\n")
            for item in transaksi:
                file.write(item.ringkasan() + "\n")
        return path

    def buat_laporan_csv(self, transaksi: list) -> Path:
        path = self.folder_laporan / "laporan_transaksi.csv"
        with path.open("w", encoding="utf-8") as file:
            file.write("kode,pelanggan,kendaraan,lama_hari,total,status\n")
            for item in transaksi:
                file.write(
                    f"{item.kode_transaksi},{item.pelanggan.nama},{item.kendaraan.kode},"
                    f"{item.lama_hari},{item.total_biaya},{item.status}\n"
                )
        return path

    def statistik_ringkas(self, kendaraan: list, transaksi: list) -> dict:
        jumlah_tersedia = sum(1 for item in kendaraan if item.status == "tersedia")
        jumlah_disewa = sum(1 for item in kendaraan if item.status == "disewa")
        pendapatan = sum(item.total_biaya for item in transaksi if item.status == "selesai")
        return {
            "total_kendaraan": len(kendaraan),
            "kendaraan_tersedia": jumlah_tersedia,
            "kendaraan_disewa": jumlah_disewa,
            "total_transaksi": len(transaksi),
            "pendapatan_selesai": pendapatan,
        }
