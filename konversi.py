import streamlit as st

def tampilkan_konversi(konverter):
    st.title("Aplikasi Konversi Mata Uang")
    
    jumlah = st.number_input("Jumlah:", min_value=0.0)
    mata_uang_asal = st.selectbox("Pilih Mata Uang Asal:", ["USD", "EUR", "IDR", "JPY"])
    mata_uang_tujuan = st.selectbox("Pilih Mata Uang Tujuan:", ["USD", "EUR", "IDR", "JPY"])

    if st.button("Konversi"):
        try:
            jumlah_terkonversi = konverter.konversi(jumlah, mata_uang_asal, mata_uang_tujuan)
            catatan_konversi = f"{jumlah} {mata_uang_asal} = {jumlah_terkonversi:.2f} {mata_uang_tujuan}"
            if 'riwayat' not in st.session_state:
                st.session_state.riwayat = []
            st.session_state.riwayat.append(catatan_konversi)
            st.success(catatan_konversi)
        except ValueError as e:
            st.warning(str(e))
