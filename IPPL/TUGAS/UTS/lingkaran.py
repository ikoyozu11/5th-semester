import tkinter as tk  # Mengimpor modul tkinter untuk GUI
from tkinter import messagebox  # Mengimpor messagebox dari tkinter untuk menampilkan pesan kesalahan

# Konstanta untuk nilai Phi (π) yang digunakan dalam perhitungan luas lingkaran dan tabung
PHI = 3.14159

# Fungsi untuk validasi input dari pengguna
def validasi():
    """
    Fungsi ini memvalidasi input dari pengguna yang dimasukkan di kolom tinggi dan jari-jari.
    Jika input bukan angka, akan menampilkan pesan kesalahan.
    Jika input valid, fungsi ini akan memanggil fungsi-fungsi perhitungan luas.
    """
    try:
        # Mengambil nilai dari entry untuk tinggi dan jari-jari, serta mengonversi ke tipe float
        t = float(inp_t.get())
        r = float(inp_r.get())

        # Memanggil fungsi perhitungan luas dengan parameter jari-jari dan tinggi
        luas_lingkaran(r)
        luas_persegi(t, r)
        luas_tabung(t, r)
    except ValueError:
        # Menampilkan pesan kesalahan jika input tidak valid (misalnya, bukan angka)
        messagebox.showerror("Error", "Masukkan nilai numerik yang valid untuk tinggi dan jari-jari.")

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(r):
    luas = PHI * r ** 2  # Rumus luas lingkaran: π * r^2
    lbl_lingkaran.config(text=f"Luas Lingkaran: {luas:.2f}")  # Menampilkan hasil dengan 2 desimal

# Fungsi untuk menghitung luas persegi panjang (bagian samping tabung)
def luas_persegi(t, r):
    luas = 2 * PHI * r * t  # Rumus luas persegi panjang: 2 * π * r * t
    lbl_persegi.config(text=f"Luas Persegi Panjang: {luas:.2f}")  # Menampilkan hasil dengan 2 desimal

# Fungsi untuk menghitung luas permukaan tabung
def luas_tabung(t, r):
    luas = (2 * PHI * r ** 2) + (2 * PHI * r * t)  # Rumus luas permukaan tabung
    lbl_tabung.config(text=f"Luas Permukaan Tabung: {luas:.2f}")  # Menampilkan hasil dengan 2 desimal

# Inisialisasi antarmuka pengguna (GUI) menggunakan tkinter
root = tk.Tk()  # Membuat jendela utama aplikasi
root.title("Kalkulator Luas Permukaan Tabung")  # Judul aplikasi
root.geometry("400x400")  # Ukuran jendela
root.configure(bg="#f2f2f2")  # Warna latar belakang yang lembut

# Gaya Font
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 12)
result_font = ("Arial", 12, "bold")

# Judul Aplikasi
title = tk.Label(root, text="Kalkulator Luas Permukaan Tabung", font=title_font, bg="#f2f2f2", fg="#333333")
title.pack(pady=(20, 10))  # Padding untuk jarak atas dan bawah

# Label dan Entry untuk tinggi
lbl_t = tk.Label(root, text="Masukkan Tinggi:", font=label_font, bg="#f2f2f2", fg="#333333")
lbl_t.pack()
inp_t = tk.Entry(root, font=label_font)
inp_t.pack(pady=(0, 10))

# Label dan Entry untuk jari-jari
lbl_r = tk.Label(root, text="Masukkan Jari-jari:", font=label_font, bg="#f2f2f2", fg="#333333")
lbl_r.pack()
inp_r = tk.Entry(root, font=label_font)
inp_r.pack(pady=(0, 10))

# Tombol untuk menghitung luas
btn_hitung = tk.Button(root, text="Hitung", command=validasi, font=label_font, bg="#4CAF50", fg="white", width=10)
btn_hitung.pack(pady=(10, 20))  # Padding untuk tombol

# Label untuk menampilkan hasil perhitungan luas lingkaran
lbl_lingkaran = tk.Label(root, text="Luas Lingkaran: ", font=result_font, bg="#f2f2f2", fg="#007ACC")
lbl_lingkaran.pack(pady=(5, 5))

# Label untuk menampilkan hasil perhitungan luas persegi panjang (bagian samping tabung)
lbl_persegi = tk.Label(root, text="Luas Persegi Panjang: ", font=result_font, bg="#f2f2f2", fg="#007ACC")
lbl_persegi.pack(pady=(5, 5))

# Label untuk menampilkan hasil perhitungan luas permukaan tabung
lbl_tabung = tk.Label(root, text="Luas Permukaan Tabung: ", font=result_font, bg="#f2f2f2", fg="#007ACC")
lbl_tabung.pack(pady=(5, 20))

# Menjalankan aplikasi GUI (loop utama)
root.mainloop()  # Loop yang membuat jendela tetap terbuka hingga ditutup oleh pengguna