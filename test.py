from abc import ABC, abstractmethod

# --- Praktikum 01: Definisi Kelas Abstrak ---
class KendaraanAbstrak(ABC):
    def __init__(self, merk):
        self.merk = merk
        print(f"Inisialisasi KendaraanAbstrak dengan merk: {self.merk}")

    # Metode konkret (bisa diwarisi langsung)
    def info_merk(self):
        print(f"Merk kendaraan ini adalah {self.merk}.")

    @abstractmethod
    def start_mesin(self):
        """Metode ini wajib di-override oleh anak kelas"""
        pass

    @abstractmethod
    def stop_mesin(self):
        """Metode ini wajib di-override oleh anak kelas"""
        pass

# Subclass Konkret (Implementasi dari KendaraanAbstrak)
class Mobil(KendaraanAbstrak):
    def start_mesin(self):
        print(f"Mesin mobil {self.merk} dinyalakan.")

    def stop_mesin(self):
        print(f"Mesin mobil {self.merk} dimatikan.")

# --- Praktikum 02: Mencoba Instansiasi ---
class MediaAbstrak(ABC):
    def __init__(self, judul):
        self.judul = judul

    @abstractmethod
    def play(self):
        pass

if __name__ == "__main__":
    # Ini berhasil karena Mobil adalah kelas konkret
    print("--- Demo Praktikum 01 ---")
    mobil_contoh = Mobil("Toyota")
    mobil_contoh.start_mesin()
    mobil_contoh.info_merk()

    print("\n--- Demo Praktikum 02 (Uji Error) ---")
    try:
        # Baris ini akan memicu TypeError
        media = MediaAbstrak("Konten Abstrak")
    except TypeError as e:
        print(f"GAGAL membuat objek! Error: {e}")