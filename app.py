import streamlit as st
from konversi import tampilkan_konversi
from riwayat import tampilkan_riwayat
from berita import tampilkan_berita
from info import tampilkan_info

class KonverterMataUang:
    def __init__(self):
        self.nilai_tukar = {
            "USD": {"EUR": 0.85, "IDR": 14500, "JPY": 110},
            "EUR": {"USD": 1.18, "IDR": 17000, "JPY": 130},
            "IDR": {"USD": 0.000069, "EUR": 0.000059, "JPY": 0.0077},
            "JPY": {"USD": 0.0091, "EUR": 0.0077, "IDR": 130},
        }

    def konversi(self, jumlah, mata_uang_asal, mata_uang_tujuan):
        if mata_uang_asal == mata_uang_tujuan:
            raise ValueError("Mata uang asal dan tujuan tidak boleh sama.")
        rate = self.nilai_tukar[mata_uang_asal][mata_uang_tujuan]
        return jumlah * rate

# Inisialisasi kelas KonverterMataUang
konverter = KonverterMataUang()

# Menu navigasi
menu = st.sidebar.selectbox("Pilih Halaman", ["Konversi", "Riwayat", "Berita", "Informasi"])

# Halaman Konversi
if menu == "Konversi":
    tampilkan_konversi(konverter)

# Halaman Riwayat
elif menu == "Riwayat":
    tampilkan_riwayat()

# Halaman Berita
elif menu == "Berita":
    tampilkan_berita()

# Halaman Informasi
elif menu == "Informasi":
    tampilkan_info()
