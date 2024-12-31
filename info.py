import streamlit as st

def tampilkan_info():
    st.title("Informasi Aplikasi Konversi Mata Uang")
    
    st.write("""
        Aplikasi ini memungkinkan Anda untuk mengonversi antara berbagai mata uang.
        Saat ini, aplikasi mendukung konversi antara empat mata uang:
        - USD (Dolar AS)
        - EUR (Euro)
        - IDR (Rupiah Indonesia)
        - JPY (Yen Jepang)

        ### Cara Menggunakan
        1. Masukkan jumlah uang yang ingin Anda konversi.
        2. Pilih mata uang asal dari dropdown.
        3. Pilih mata uang tujuan dari dropdown.
        4. Klik tombol "Konversi" untuk melihat hasil konversi.
        5. Riwayat konversi Anda dapat dilihat di halaman Riwayat.

        ### Catatan
        - Nilai tukar yang digunakan dalam aplikasi ini adalah nilai tukar manual dan dapat diubah sesuai kebutuhan.
        - Riwayat konversi akan hilang jika sesi di-refresh atau ditutup.

        Terima kasih telah menggunakan aplikasi ini!
    """)
