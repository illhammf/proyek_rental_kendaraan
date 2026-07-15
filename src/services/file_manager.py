"""Service untuk menyimpan dan membaca data JSON."""

from __future__ import annotations
import json
from pathlib import Path


class FileManager:
    """Class pembantu agar proses simpan dan baca file tidak ditulis berulang."""

    def __init__(self, folder_data: str = "data") -> None:
        self.folder_data = Path(folder_data)
        self.folder_data.mkdir(parents=True, exist_ok=True)

    def path(self, nama_file: str) -> Path:
        return self.folder_data / nama_file

    def simpan_json(self, nama_file: str, data: list | dict) -> None:
        with self.path(nama_file).open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def baca_json(self, nama_file: str, default: list | dict | None = None) -> list | dict:
        target = self.path(nama_file)
        if not target.exists():
            return [] if default is None else default
        with target.open("r", encoding="utf-8") as file:
            return json.load(file)
