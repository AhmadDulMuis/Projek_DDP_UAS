import streamlit as st

def tampilkan_berita():
    st.title("Berita Terkait Mata Uang")
    
    st.write("""
        ### Berita Terbaru:
        
        - **Dolar AS Menguat Terhadap Euro**: Dolar AS mengalami penguatan terhadap Euro setelah laporan ekonomi positif dari AS.
        - **Fluktuasi Nilai Tukar Rupiah**: Rupiah Indonesia mengalami fluktuasi akibat ketidakpastian politik dan ekonomi global.
        - **Yen Jepang Tertekan**: Yen Jepang tertekan oleh kebijakan moneter yang longgar dari Bank of Japan.
        - **Analisis Pasar**: Para analis memperkirakan bahwa nilai tukar mata uang akan terus berfluktuasi seiring dengan perkembangan ekonomi global.
        
        ### Sumber Berita:
        - [Reuters](https://www.reuters.com)
        - [Bloomberg](https://www.bloomberg.com)
        - [CNBC](https://www.cnbc.com)
    """)
