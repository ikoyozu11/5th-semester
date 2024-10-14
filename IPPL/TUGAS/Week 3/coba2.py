class Akun:
    def __init__(self, nomor_akun, status_kode, jumlah_penjualan):
        self.nomor_akun = nomor_akun
        self.status_kode = status_kode
        self.jumlah_penjualan = jumlah_penjualan

def cari_akun(daftar_akun, input_nomor_akun):
    for akun in daftar_akun:
        if akun.nomor_akun == input_nomor_akun:
            return akun 
    return None 

def proses_servis(daftar_akun, input_nomor_akun):
    akun = cari_akun(daftar_akun, input_nomor_akun)
    
    if akun and akun.status_kode == "valid":
        print("Invoice Dihasilkan:")
        print(f"Nomor Akun: {akun.nomor_akun}")
        print(f"Jumlah Penjualan: ${akun.jumlah_penjualan:.2f}")
    else:
        print("Error: Akun tidak ditemukan atau status kode tidak valid.")

daftar_akun = [
    Akun("ACC12345", "valid", 150.75),
    Akun("ACC54321", "invalid", 200.50),
    Akun("ACC67890", "valid", 300.25)
]

input_nomor_akun = input("Masukkan nomor akun: ")

proses_servis(daftar_akun, input_nomor_akun)