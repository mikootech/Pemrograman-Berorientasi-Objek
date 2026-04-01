# ============================================================
# Modul parkir_utils.py
# Berisi fungsi-fungsi perhitungan untuk sistem parkir roda dua
# ============================================================

# Tarif parkir per jam
TARIF_PER_JAM = 2000
TARIF_MINIMUM  = 2000  # Biaya minimum meskipun kurang dari 1 jam

def hitung_biaya(durasi_jam):
    """Menghitung biaya parkir berdasarkan durasi (jam)"""
    if durasi_jam <= 1:
        return TARIF_MINIMUM
    else:
        return durasi_jam * TARIF_PER_JAM

def format_rupiah(nominal):
    """Memformat angka menjadi format rupiah"""
    return f"Rp {nominal:,}".replace(",", ".")

def tampilkan_struk(plat, durasi, biaya):
    """Menampilkan struk parkir"""
    print("=" * 35)
    print("       STRUK PARKIR RODA DUA")
    print("=" * 35)
    print(f"  Plat Nomor  : {plat}")
    print(f"  Durasi      : {durasi} jam")
    print(f"  Total Biaya : {format_rupiah(biaya)}")
    print("=" * 35)
    print("    Terima kasih telah parkir!")
    print("=" * 35)