import streamlit as st
import pandas as pd
import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import altair as alt



warnings.filterwarnings('ignore')

st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Customer Segmentation")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# 1) DATA SET BÖLÜMÜ
st.header("Data Set")

file_uploader_key_1 = st.file_uploader(":file_folder: Dosya 1'i Yükleyin", type=(["csv", "txt", "xlsx", "xls"]), key="uploader1")

if file_uploader_key_1 is not None:
    filename = file_uploader_key_1.name
    st.write(filename)
    df = pd.read_csv(file_uploader_key_1, encoding="ISO-8859-1")

    st.sidebar.header("Filtrenizi seçin: ")

    # Tüm sütunları filtre seçenekleri olarak eklemek
    selected_columns = st.sidebar.multiselect("Sütunlarınızı seçin", df.columns.tolist(), default=[])

    if not selected_columns:
        st.write("Lütfen verilerinizi filtrelemek için sütunları seçin")
    else:
        df2 = df[selected_columns]  # Seçilen sütunları içeren yeni bir veri seti oluştur
        st.write(df2)  # Seçilen sütunları içeren veri setini göster
else:
    st.write("Lütfen bir dosya yükleyin")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2) DATA PREPROCESSING BOLUMU
st.header("Data Preprocessing")

# 2.1) Data Cleaning Bölümü
st.subheader("Data Cleaning")
# Dosya yükleme widget'ını tanımlayın
file_uploader_key_2 = st.file_uploader(":file_folder: Dosya 2'yi Yükleyin", type=(["csv", "txt", "xlsx", "xls"]), key="uploader2")

# Dosya yüklendiğinde işlemleri gerçekleştirin
if file_uploader_key_2 is not None:
    # Dosya adını ve boyutunu kontrol edin
    filename = file_uploader_key_2.name
    file_size = len(file_uploader_key_2.getvalue())

    if file_size == 0:
        st.error("Yüklenen dosya boş. Lütfen geçerli bir dosya yükleyin.")
    else:
        # Print debug information (optional)
        st.write(f"Yüklenen dosya adı: {filename}")
        st.write(f"Dosya boyutu: {file_size} byte")

        # Dosya türüne göre veri okuma işlemleri
    try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_uploader_key_2, encoding="ISO-8859-1")
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_uploader_key_2)


            # 2.1.1) Veri ön işleme sonuçlarını gösterme
            st.title('Veri Ön İşleme Sonuçları')

            # Temizlenmiş veri önizleme
            st.subheader('Temizlenmiş Veri Önizleme')
            st.write(df.head(100))  # İlk 100 satırı göster

            # 2.1.2) Eksik değerlerin durumu
            st.subheader('Eksik Değerlerin Durumu')
            st.write(df.isnull().sum())  # Eksik değerlerin sayısını göster

            # 2.1.3) Yinelenen değerlerin durumu
            st.subheader('Yinelenen Değerlerin Durumu')
            st.write(df.duplicated().sum())  # Yinelenen değerlerin sayısını göster

           # 2.1.4.1) İptal edilen işlemlerin oranını çıkarma
            st.subheader('İptal Edilen İşlemlerin Dağılımı')
            cancelled_counts = df['Transaction_Status'].value_counts()
            st.write(cancelled_counts)

          # 2.1.4.2) İptal edilen işlemlerin pasta grafiği dağılımını görselleştirme
            st.subheader('İptal Edilen İşlemlerin Grafik Dağılımı')
            # Verileri DataFrame'e dönüştürme
            df_cancelled = pd.DataFrame(cancelled_counts.items(), columns=['Durum', 'Sayı'])
            # Pasta grafiği oluşturma
            fig, ax = plt.subplots()
            ax.pie(df_cancelled['Sayı'], labels=df_cancelled['Durum'], autopct='%1.1f%%', textprops={'fontsize': 7}, startangle=20)
            # Grafik verilerini base64 formatında HTML içeriği olarak dönüştürme
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            plt.close(fig)
            data = base64.b64encode(buffer.getvalue()).decode()
            # HTML içeriğini oluşturma
            html_img = f'<img src="data:image/png;base64,{data}" style="max-width: 1000px;">'
            # Streamlit'e HTML içeriği gönderme
            st.markdown(html_img, unsafe_allow_html=True)

            # 2.1.5.1) Anormal Stok Kodlarını İnceleme
            st.subheader('Anormal Stok Kodlarını İnceleme')
             # Anormal stok kodları listesi
            abnormal_stockcodes = ['POST', 'D', 'M', 'BANK CHARGES', 'PADS', 'DOT', 'CRUK', 'C2']
            # DataFrame'e 'IsAbnormal' sütunu ekleme
            df['IsAbnormal'] = df['StockCode'].isin(abnormal_stockcodes)
            # Anormal ve normal StockCode'ların sayısını bulma
            count_abnormal = df['IsAbnormal'].sum()
            count_normal = len(df) - count_abnormal
            # StockCode'ların oranlarını hesaplama
            total_codes = len(df)
            percentage_abnormal = (count_abnormal / total_codes) * 100
            percentage_normal = (count_normal / total_codes) * 100
            # Streamlit uygulamasında sonuçları tablo halinde gösterme
            st.subheader('Stok Kodu İstatistikleri')
            # Bilgileri tablo halinde gösterme
            data_table = {
                'İstatistik': ['Toplam Stok Kodu Sayısı', 'Anormal Stok Kodu Sayısı', 'Normal Stok Kodu Sayısı', 'Anormal Stok Kodu Oranı', 'Normal Stok Kodu Oranı'],
                 'Değer': [total_codes, count_abnormal, count_normal, f'{percentage_abnormal:.2f}%', f'{percentage_normal:.2f}%']
            }
            # DataFrame oluşturma
            statistics_df = pd.DataFrame(data_table)
            # Tabloyu Streamlit'te gösterme
            st.table(statistics_df)
        
            # 2.1.5.2) En Çok Kullanılan 10 StockCode çubuk grafik çizimi
            st.subheader('En Çok Kullanılan 10 StockCode')
             # StockCode'ların sayısını sayalım
            stockcode_counts = df['StockCode'].value_counts()
             # En çok tekrar eden ilk 10 StockCode'ı alalım
            top_10_stockcodes = stockcode_counts.head(10)
             # En çok tekrar eden StockCode'ların dağılımını çubuk grafikle gösterelim
            st.bar_chart(top_10_stockcodes)
             
            st.subheader('Anormal Ürün İsimlerini İnceleme')
            # 2.1.6.1) Anormal Ürün İsimlerini İnceleme
            def is_anormal_product_name(name):
             # Sadece büyük harflerden oluşan isimleri kontrol et
              if name.isupper():  # Eğer sadece büyük harflerden oluşuyorsa
                return False  # Anormal ürün ismi değil
              else:
                 return True  # Anormal ürün ismi
            # Anormal ürün isimlerini içeren DataFrame'i oluşturalım
            anormal_products_df = df[df['Description'].apply(is_anormal_product_name)]
            # Toplam ürün sayısı
            total_products_count = len(df)
            # Anormal ürün isimleri sayısı
            anormal_products_count = len(anormal_products_df)
            # Anormal ürün isimleri oranını hesapla
            if total_products_count > 0:
                 anormal_products_ratio = (anormal_products_count / total_products_count) * 100
            else:
                 anormal_products_ratio = 0.0
            # Tablo şeklinde sonuçları gösterme
            data_table = {
              'İstatistik': ['Toplam Ürün Sayısı', 'Anormal Ürün İsimleri Sayısı', 'Anormal Ürün İsimleri Oranı'],
               'Değer': [total_products_count, anormal_products_count, f'{anormal_products_ratio:.2f}%']
            }
            # DataFrame oluşturma
            statistics_df = pd.DataFrame(data_table)
            # Tabloyu Streamlit'te gösterme
            st.table(statistics_df)
           
           # 2.1.6.2) En Çok Kullanılan 10 Ürün İsmi çubuk grafik çizimi
           # Streamlit uygulamasında çubuk grafik çizimi
            st.subheader('En Çok Kullanılan 10 Ürün İsmi')
           # Description'ların sayısını sayalım
            description_counts = df['Description'].value_counts()
           # En çok tekrar eden ilk 10 StockCode'ı alalım
            top_10_description = description_counts.head(10)
           # En çok tekrar eden StockCode'ların dağılımını çubuk grafikle gösterelim
            st.bar_chart(top_10_description)

            # 2.1.7) Ücreti '0' Olanların Kontrolü
            # UnitPrice değeri 0 olan ürünleri filtreleme
            filtered_df = df[df['UnitPrice'] == 0]
            # Ücreti 0 olan ürünlerin sayısı
            count_zero_price = len(filtered_df)
            # Toplam ürün sayısı
            total_products_count = len(df)
            # Ücreti 0 olan ürünlerin oranını hesaplama
            if total_products_count > 0:
               percentage_zero_price = (count_zero_price / total_products_count) * 100
            else:
               percentage_zero_price = 0.0
            # Streamlit uygulamasında sonuçları tablo halinde gösterme
            st.subheader('Ücreti 0 Olan Ürün İstatistikleri')
            # Bilgileri tablo halinde gösterme
            data_table = {
               'İstatistik': ['Ücreti 0 Olan Ürün Sayısı', 'Toplam Ürün Sayısı', 'Ücreti 0 Olan Ürün Oranı'],
                'Değer': [count_zero_price, total_products_count, f'{percentage_zero_price:.2f}%']
             }
            # DataFrame oluşturma
            statistics_df = pd.DataFrame(data_table)
            # Tabloyu Streamlit'te gösterme
            st.table(statistics_df)


    except Exception as e:
         st.error(f"Dosya okuma sırasında hata oluştu: {e}")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Modeling kodlarını buraya ekle
