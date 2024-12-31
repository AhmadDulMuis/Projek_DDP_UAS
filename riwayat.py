import streamlit as st

def tampilkan_riwayat():
    st.title("Riwayat Konversi")
    
    if 'riwayat' in st.session_state and st.session_state.riwayat:
        for catatan in st.session_state.riwayat:
            st.write(catatan)
    else:
        st.write("Belum ada riwayat konversi.")
