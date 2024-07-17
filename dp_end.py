import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import  warnings
import altair as alt
from sklearn.neighbors import LocalOutlierFactor


warnings.filterwarnings('ignore')

st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Customer Segmentation")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Sayfa başlığı ve açıklama
st.subheader("Outliter Analyst - Correlation Analyst - Feature Scaling - Dimensionality Reduction ")

# Dosya yükleme widget'ı tanımlama
file_uploader_key1 = st.file_uploader("Dosyayı Yükleyin", type=["csv", "txt", "xlsx", "xls"], key="uploader1")

# Dosya yüklendiğinde işlemleri gerçekleştirme
if file_uploader_key1 is not None:
    # Dosya adını ve boyutunu kontrol etme
    filename = file_uploader_key1.name
    file_size = len(file_uploader_key1.getvalue())

    if file_size == 0:
        st.error("Yüklenen dosya boş. Lütfen geçerli bir dosya yükleyin.")
    else:
        # Debug bilgilerini yazdırma (isteğe bağlı)
        st.write(f"Yüklenen dosya adı: {filename}")
        st.write(f"Dosya boyutu: {file_size} byte")

        # Dosya türüne göre veri okuma işlemleri
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_uploader_key1, encoding="ISO-8859-1")
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_uploader_key1)
            
            # Veri çerçevesinin başlıklarını gösterme
            st.subheader("Veri Çerçevesi Önizleme")
            st.write(df.head())

            # Local Outlier Factor (LOF) modelini oluşturun
            lof_model = LocalOutlierFactor(contamination='auto')

# Modeli eğitin ve aykırı değerleri tespit edin

            outlier_preds = lof_model.fit_predict(df)

# Aykırı değerlerin indekslerini alın
            outlier_indices = np.where(outlier_preds == -1)[0]

# Aykırı değerleri ayrı bir veri çerçevesine atayın
            outliers_data = df.iloc[outlier_indices]

# Streamlit arayüzü oluşturma
            st.subheader('Temizlenmiş Veri Seti Aykırı Değer Analizi')



# Aykırı değer sayısını ve yüzdesini gösterme
            num_outliers = len(outlier_indices)
            total_records = len(df)
            outlier_percentage = (num_outliers / total_records) * 100

            st.write(f"Aykırı Değer Sayısı: {num_outliers}")
            st.write(f"Aykırı Değer Yüzdesi: {outlier_percentage:.2f}%")

            # Aykırı değer sayısı ve yüzdesini data_table içinde gösterme
            st.subheader('Aykırı Değer İstatistikleri')
            data_stats = {
              'Aykırı Değer Sayısı': [num_outliers],
              'Aykırı Değer Yüzdesi (%)': [outlier_percentage]
            }
            stats_df = pd.DataFrame(data_stats)
            st.dataframe(stats_df)

            
             
            st.subheader("Korelasyon Analizi")
            correlation_matrix = df.corr()

           # Alt üçgen maskesi oluştur
            mask = np.zeros_like(correlation_matrix )
            mask[np.triu_indices_from(mask, k=1)] = True

            custom_colors = ['#19a871', '#1bd691', '#c9dbd4', '#b6efd9', '#d5f2e6'] # RGB renk kodları
            
# Özel renk haritası oluşturma
            cmap_custom = sns.color_palette(custom_colors, as_cmap=True)

           # Korelasyon matrisini görselleştirme (yalnızca alt üçgeni göstererek)
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap=cmap_custom, fmt='.2f', linewidths=1, mask=mask)
            plt.title('Korelasyon Matrisi (Alt Üçgen)')
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Dosya okuma sırasında hata oluştu: {e}")


# Dosya yükleme widget'ı tanımlama
file_uploader_key2 = st.file_uploader("Dosyayı Yükleyin", type=["csv", "txt", "xlsx", "xls"], key="uploader2")

# Dosya yüklendiğinde işlemleri gerçekleştirme
if file_uploader_key2 is not None:
    # Dosya adını ve boyutunu kontrol etme
    filename = file_uploader_key2.name
    file_size = len(file_uploader_key2.getvalue())

    if file_size == 0:
        st.error("Yüklenen dosya boş. Lütfen geçerli bir dosya yükleyin.")
    else:
        # Debug bilgilerini yazdırma (isteğe bağlı)
        st.write(f"Yüklenen dosya adı: {filename}")
        st.write(f"Dosya boyutu: {file_size} byte")

        # Dosya türüne göre veri okuma işlemleri
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_uploader_key2, encoding="ISO-8859-1")
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_uploader_key2)
                 # Veri çerçevesinin başlıklarını gösterme
            st.subheader("Veri Çerçevesi Önizleme")
            st.write(df.head())

        
        except Exception as e:
            st.error(f"Dosya okuma sırasında hata oluştu: {e}")

            # Dosya yükleme widget'ı tanımlama
file_uploader_key3= st.file_uploader("Dosyayı Yükleyin", type=["csv", "txt", "xlsx", "xls"], key="uploader3")

            # Dosya yüklendiğinde işlemleri gerçekleştirme
if file_uploader_key3 is not None:
    # Dosya adını ve boyutunu kontrol etme
    filename = file_uploader_key3.name
    file_size = len(file_uploader_key3.getvalue())

    if file_size == 0:
        st.error("Yüklenen dosya boş. Lütfen geçerli bir dosya yükleyin.")
    else:
        # Debug bilgilerini yazdırma (isteğe bağlı)
        st.write(f"Yüklenen dosya adı: {filename}")
        st.write(f"Dosya boyutu: {file_size} byte")

        # Dosya türüne göre veri okuma işlemleri
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_uploader_key3, encoding="ISO-8859-1")
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_uploader_key3)
            
             # Veri çerçevesinin başlıklarını gösterme
            st.subheader("Veri Çerçevesi Önizleme")
            st.write(df.head())

        except Exception as e:
            st.error(f"Dosya okuma sırasında hata oluştu: {e}")


