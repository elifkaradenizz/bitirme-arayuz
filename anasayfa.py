import streamlit as st
import subprocess



st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Customer Segmentation")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


def main():
    st.title("Ana Sayfa")


   # Modelling butonu
    if st.button("Veri Temizleme"):
        # `modelling.py` dosyasını subprocess ile çalıştırarak yeni bir tarayıcı penceresinde aç
        subprocess.Popen(["streamlit", "run", "data_cleaning.py"])


   # Modelling butonu
    if st.button("Özellik Mühendisliği"):
        # `modelling.py` dosyasını subprocess ile çalıştırarak yeni bir tarayıcı penceresinde aç
        subprocess.Popen(["streamlit", "run", "feature_engineering.py"])


   # Modelling butonu
    if st.button("Veri Ön İşleme Diğer Adımlar"):
        # `modelling.py` dosyasını subprocess ile çalıştırarak yeni bir tarayıcı penceresinde aç
        subprocess.Popen(["streamlit", "run", "dp_end.py"])


    # Modelling butonu
    if st.button("Modelleme Sayfası"):
        # `modelling.py` dosyasını subprocess ile çalıştırarak yeni bir tarayıcı penceresinde aç
        subprocess.Popen(["streamlit", "run", "modelling.py"])

            # Modelling butonu
    if st.button("Performans Karşılaştırma Sayfası"):
        # `modelling.py` dosyasını subprocess ile çalıştırarak yeni bir tarayıcı penceresinde aç
        subprocess.Popen(["streamlit", "run", "performance.py"])

        

if __name__ == "__main__":
    main()

