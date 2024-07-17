import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D grafik için gerekli
import  warnings
import altair as alt



warnings.filterwarnings('ignore')

st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Customer Segmentation")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Sayfa başlığı ve açıklama
st.subheader("Feature Engineering Uygulaması")

# Dosya yükleme widget'ı tanımlama
file_uploader_key = st.file_uploader("Dosyayı Yükleyin", type=["csv", "txt", "xlsx", "xls"], key="uploader")

# Dosya yüklendiğinde işlemleri gerçekleştirme
if file_uploader_key is not None:
    # Dosya adını ve boyutunu kontrol etme
    filename = file_uploader_key.name
    file_size = len(file_uploader_key.getvalue())

    if file_size == 0:
        st.error("Yüklenen dosya boş. Lütfen geçerli bir dosya yükleyin.")
    else:
        # Debug bilgilerini yazdırma (isteğe bağlı)
        st.write(f"Yüklenen dosya adı: {filename}")
        st.write(f"Dosya boyutu: {file_size} byte")

        # Dosya türüne göre veri okuma işlemleri
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_uploader_key, encoding="ISO-8859-1")
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_uploader_key)
            
            # Veri çerçevesinin başlıklarını gösterme
            st.subheader("Veri Çerçevesi Önizleme")
            st.write(df.head())
            
              # 2.1.2) Eksik değerlerin durumu
            st.subheader('Eksik Değerlerin Durumu')
            st.write(df.isnull().sum())  # Eksik değerlerin sayısını göster

            # 2.1.3) Yinelenen değerlerin durumu
            st.subheader('Yinelenen Değerlerin Durumu')
            st.write(df.duplicated().sum())  # Yinelenen değerlerin sayısını göster


        # RFM metriklerini görselleştirme başlığı
            st.subheader("RFM Metriklerini Görselleştirme")

# Days Since Last Purchase (Son Satın Alma Tarihinden İtibaren Geçen Günler) için segment oluşturma
            df['RecencySegment'] = pd.cut(df['Days_Since_Last_Purchase'], bins=[0, 10, 20, 30, float('inf')],
                               labels=['0-10', '11-20', '21-30', '31+'])

# Total Transactions (Toplam İşlemler) için segment oluşturma
            df['FrequencySegment'] = pd.cut(df['Total_Transactions'], bins=[0, 2, 4, 6, float('inf')],
                                 labels=['1-2', '3-4', '5-6', '7+'])

# Total Spend (Toplam Harcama) için segment oluşturma
            df['MonetarySegment'] = pd.cut(df['Total_Spend'], bins=[0, 200, 400, 600, float('inf')],
                                labels=['0-200', '201-400', '401-600', '601+'])

# Total Products Purchased (Satın Alınan Toplam Ürün) ve Average Transaction Value (Ortalama İşlem Değeri) için segment oluşturma
            df['ProductsPurchasedSegment'] = pd.cut(df['Total_Products_Purchased'], bins=[0, 20, 40, 60, float('inf')],
                                         labels=['0-20', '21-40', '41-60', '61+'])
            df['AvgTransactionValueSegment'] = pd.cut(df['Average_Transaction_Value'], bins=[0, 150, 200, 250, float('inf')],
                                          labels=['0-150', '151-200', '201-250', '251+'])

# Müşteri segmentlerinin sayılarını hesaplama
            recency_counts = df['RecencySegment'].value_counts().sort_index()
            frequency_counts = df['FrequencySegment'].value_counts().sort_index()
            monetary_counts = df['MonetarySegment'].value_counts().sort_index()
            products_purchased_counts = df['ProductsPurchasedSegment'].value_counts().sort_index()
            avg_transaction_value_counts = df['AvgTransactionValueSegment'].value_counts().sort_index()

# Çubuk grafiklerini oluşturma için subplotlar
            fig, axes = plt.subplots(2, 3, figsize=(24, 12))

# Days Since Last Purchase (Recency) için çubuk grafiği
            sns.barplot(x=recency_counts.index, y=recency_counts.values, palette='deep', ax=axes[0, 0])
            axes[0, 0].set_title('Son Satın Almadan Bu Yana Geçen Günler')
            axes[0, 0].set_xlabel('Recency Segment')
            axes[0, 0].set_ylabel('Customer Count')

# Total Transactions (Frequency) için çubuk grafiği
            sns.barplot(x=frequency_counts.index, y=frequency_counts.values, palette='deep', ax=axes[0, 1])
            axes[0, 1].set_title('Toplam İşlemler')
            axes[0, 1].set_xlabel('Frequency Segment (Total Transactions)')
            axes[0, 1].set_ylabel('Customer Count')

# Total Products Purchased için çubuk grafiği
            sns.barplot(x=products_purchased_counts.index, y=products_purchased_counts.values, palette='deep', ax=axes[0, 2])
            axes[0, 2].set_title('Satın Alınan Toplam Ürün')
            axes[0, 2].set_xlabel('Frequency Segment (Total Products Purchased)')
            axes[0, 2].set_ylabel('Customer Count')

# Total Spend (Monetary) için çubuk grafiği
            sns.barplot(x=monetary_counts.index, y=monetary_counts.values, palette='deep', ax=axes[1, 0])
            axes[1, 0].set_title('Toplam Harcama')
            axes[1, 0].set_xlabel('Monetary Segment (Total Spend)')
            axes[1, 0].set_ylabel('Customer Count')

# Average Transaction Value için çubuk grafiği
            sns.barplot(x=avg_transaction_value_counts.index, y=avg_transaction_value_counts.values, palette='deep', ax=axes[1, 1])
            axes[1, 1].set_title('Ortalama İşlem Değeri')
            axes[1, 1].set_xlabel('Monetary Segment (Average Transaction Value)')
            axes[1, 1].set_ylabel('Customer Count')

# Boş subplot'u kaldırma
            fig.delaxes(axes[1, 2])

# Subplotlar arasındaki boşluk ayarlama
            plt.tight_layout()

# Streamlit üzerinde gösterme
            st.pyplot(fig)

          # Unique_Products_Purchased (Benzersiz Ürünlerin Sayısı) için segmentler oluşturma
            df['ProductDiversity'] = pd.cut(df['Unique_Products_Purchased'], bins=[0, 3, 6, float('inf')],
                                 labels=['1-3', '4-6', '7+'])

# Müşteri segmentlerinin sayılarını hesaplama
            product_diversity_counts = df['ProductDiversity'].value_counts().sort_index()

# Streamlit uygulamasında Müşteri Ürün Çeşitliliği için çubuk grafik çizimi
            st.subheader('Müşteri Ürün Çeşitliliği')
            st.bar_chart(product_diversity_counts)


            st.subheader('Favori Alışveriş Saati')
           
            # Müşteri alışveriş saatlerini analiz etme

    # Saat dilimlerine göre alışveriş yoğunluğunun analizi
            hour_counts = df['Favorite_Shopping_Hour'].value_counts()
            # Haftanın gün isimlerini tanımlama
           # Haftanın gün isimlerini tanımlama
            weekdays = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']

# Gün isimlerine göre alışveriş yoğunluğunun analizi
            day_counts = df['Favorite_Shopping_Day_Numeric'].value_counts().sort_index()

# Grafik için gün isimleriyle indeksleri değiştirme
            day_counts.index = [weekdays[i] for i in day_counts.index]


            df['PurchaseFrequencySegment'] = pd.cut(df['Average_Days_Between_Purchases'],
                                        bins=[0, 15, float('inf')],
                                        labels=['Kısa Aralık', 'Uzun Aralık'])

# Segmentlerdeki müşteri sayılarını görselleştirme
            segment_counts = df['PurchaseFrequencySegment'].value_counts()

# Çubuk grafik ile görselleştirme için subplotlar oluşturma
            fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 8))  # 1 satır, 2 sütunlu subplot

# İlk subplot için çubuk grafik (En Çok Tercih Edilen Alışveriş Saatleri)
            sns.barplot(x=hour_counts.index, y=hour_counts.values, palette='deep', ax=ax1)
            ax1.set_title('En Çok Tercih Edilen Alışveriş Saatleri')
            ax1.set_xlabel('Saat')
            ax1.set_ylabel('Müşteri Sayısı')
            ax1.tick_params(axis='x', rotation=45)

# İkinci subplot için çubuk grafik (En Çok Tercih Edilen Alışveriş Günleri)
            sns.barplot(x=day_counts.index, y=day_counts.values, palette='deep', ax=ax2)
            ax2.set_title('En Çok Tercih Edilen Alışveriş Günleri')
            ax2.set_xlabel('Gün')
            ax2.set_ylabel('Müşteri Sayısı')
            ax2.tick_params(axis='x', rotation=45)

            
            sns.barplot(x=segment_counts.index, y=segment_counts.values, palette='deep')
            ax3.set_title('Müşteri Segmentleri')
            ax3.set_xlabel('Satın Alma Aralığı')
            ax3.set_ylabel('Müşteri Sayısı')
            ax3.tick_params(axis='x', rotation=45)


            # Subplotları düzenleme ve gösterme
            plt.tight_layout(pad=5.0)  # Subplotlar arası boşluk ayarlama
            st.pyplot(fig)

            st.subheader('Müşterilerin Coğrafi Dağılımı')
            # UK_Customer sütununu kullanarak Birleşik Krallık müşterilerini sayın
            uk_customer_counts = df['UK_Customer'].value_counts()

            # Pasta grafiği oluştur
            plt.figure(figsize=(24, 6))
            plt.pie(uk_customer_counts, labels=['Birleşik Krallık', 'Diğer Ülkeler'], autopct='%1.1f%%', colors=['#9268F2', '#BF68F2'])
            plt.title('Müşteri Dağılımı')
            plt.axis('equal')  # Daireyi daire olarak ayarla
            st.pyplot(plt)


            st.subheader('Müşterilerin İptal Sıklığı ve İptal Oranı')
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 8))                   # 1 satır, 2 sütunlu subplot

            # İlk subplot için çubuk grafik (En Çok Tercih Edilen Alışveriş Saatleri)
            sns.histplot(df['Cancel_Frequency'], bins=20, kde=True, color='skyblue', ax=ax1)
            ax1.set_title('Müşteri İptal Sıklığı Dağılımı')
            ax1.set_xlabel('İptal Sayısı')
            ax1.set_ylabel('Müşteri Sayısı')
            ax1.tick_params(axis='x', rotation=45)

            # İkinci subplot için çubuk grafik (En Çok Tercih Edilen Alışveriş Günleri)
            sns.histplot(df['Cancel_Rate'], bins=20, kde=True, color='skyblue', ax=ax2)
            ax2.set_title('Müşteri İptal Oranı')
            ax2.set_xlabel('İptal Oranı')
            ax2.set_ylabel('Müşteri Sayısı')
            ax2.tick_params(axis='x', rotation=45)

            
            plt.tight_layout(pad=5.0)  # Subplotlar arası boşluk ayarlama
            st.pyplot(fig)
          
          
          
            # Area chart oluşturma
            st.subheader('Aylık Harcama Analizi')

           # Renkleri özelleştirerek area chart oluşturma
            colors = ['#FF5733', '#3380FF', '#33FF57']  # Renkleri istediğiniz gibi ayarlayabilirsiniz

            st.area_chart(df[[ 'Monthly_Spending_Mean', 'Monthly_Spending_Std', 'Spending_Trend']], 
               use_container_width=True, 
               color=colors)

        except Exception as e:
            st.error(f"Dosya okuma sırasında hata oluştu: {e}")
