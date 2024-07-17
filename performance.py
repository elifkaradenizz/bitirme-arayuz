import streamlit as st

def main():
    st.title("Resim Yükleme Bölümü")
    
    # İlk resim yükleme widget'ı
    uploaded_file1 = st.file_uploader("Lütfen birinci resmi seçin", type=["jpg", "jpeg", "png"], key="file_uploader1")
    
    if uploaded_file1 is not None:
        st.subheader("Birinci Resim")
        st.image(uploaded_file1, use_column_width=True)
        st.subheader(" Eksik Değerleri Doldurma Yönteminin Performans Oranına Etkisi")
    # İkinci resim yükleme widget'ı
    uploaded_file2 = st.file_uploader("Lütfen ikinci resmi seçin", type=["jpg", "jpeg", "png"], key="file_uploader2")
    
    if uploaded_file2 is not None:
        st.subheader("İkinci Resim")
        st.image(uploaded_file2, use_column_width=True)
        st.subheader(" Aykırı Değer Yöntemlerinin Performans Oranına Etkisi")
        
    # Üçüncü resim yükleme widget'ı
    uploaded_file3 = st.file_uploader("Lütfen üçüncü resmi seçin", type=["jpg", "jpeg", "png"], key="file_uploader3")
    
    if uploaded_file3 is not None:
        st.subheader("Üçüncü Resim")
        st.image(uploaded_file3, use_column_width=True)
        st.subheader(" Boyutsal Azaltma (Veri Görselleştirme) Yöntemlerinin Performans Etkisi")
    
    # Dördüncü resim yükleme widget'ı
    uploaded_file4 = st.file_uploader("Lütfen dördüncü resmi seçin", type=["jpg", "jpeg", "png"], key="file_uploader4")
    
    if uploaded_file4 is not None:
        st.subheader("Dördüncü Resim")
        st.image(uploaded_file4, use_column_width=True)
        st.subheader(" Farklı Kümeleme Algoritmalarının Başarı Oranına Etkisi")

if __name__ == "__main__":
    main()
