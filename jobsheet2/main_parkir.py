import jobsheet.jobsheet2.parkir_utils as parkir_utils

class KendaraanParkir:
    def __init__(self, plat_nomor, jenis_kendaraan, jam_masuk):
        self.plat_nomor       = plat_nomor
        self.jenis_kendaraan  = jenis_kendaraan
        self.jam_masuk        = jam_masuk
        self.jam_keluar       = None
        self.status           = "Parkir"

    def tampilkan_info(self):
        print(f"  Plat Nomor      : {self.plat_nomor}")
        print(f"  Jenis Kendaraan : {self.jenis_kendaraan}")
        print(f"  Jam Masuk       : {self.jam_masuk:02d}:00")
        print(f"  Status          : {self.status}")

    def keluar(self, jam_keluar):
        if self.status == "Parkir":
            self.jam_keluar = jam_keluar
            self.status     = "Sudah Keluar"
            durasi          = self.jam_keluar - self.jam_masuk
            biaya           = parkir_utils.hitung_biaya(durasi)
            parkir_utils.tampilkan_struk(self.plat_nomor, durasi, biaya)
        else:
            print(f"Kendaraan {self.plat_nomor} sudah keluar sebelumnya.")

    def ubah_status(self, status_baru):
        self.status = status_baru
        print(f"Status kendaraan {self.plat_nomor} diubah menjadi: {self.status}")


def main():
    print("=" * 35)
    print("    SISTEM PARKIR RODA DUA")
    print("=" * 35)

    kendaraan1 = KendaraanParkir("B 1234 ABC", "Motor", 9)
    kendaraan2 = KendaraanParkir("D 5678 XYZ", "Sepeda Motor", 10)
    kendaraan3 = KendaraanParkir("H 9999 ZZZ", "Motor", 11)

    print("\n DAFTAR KENDARAAN PARKIR:")
    print("-" * 35)
    kendaraan1.tampilkan_info()
    print("-" * 35)
    kendaraan2.tampilkan_info()
    print("-" * 35)
    kendaraan3.tampilkan_info()
    print("-" * 35)

    print("\n PROSES KENDARAAN KELUAR:\n")

    kendaraan1.keluar(12)   # jam 9 - 12 = 3 jam
    print()
    kendaraan2.keluar(11)   # jam 10 - 11 = 1 jam (tarif minimum)
    print()
    kendaraan3.keluar(15)   # jam 11 - 15 = 4 jam

    print("\n STATUS KENDARAAN SETELAH KELUAR:")
    print("-" * 35)
    kendaraan1.tampilkan_info()
    print("-" * 35)
    kendaraan2.tampilkan_info()
    print("-" * 35)
    kendaraan3.tampilkan_info()
    print("-" * 35)

main()