import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

def main():
    st.title("Modelleme Bölümü")
    
    # İlk dosya yükleme widget'ı
    uploaded_file1 = st.file_uploader("Lütfen veri setini seçin", type=["csv", "xlsx"], key="file_uploader1")
    
    if uploaded_file1 is not None:
        # İlk veri setini okuma
        file_extension1 = uploaded_file1.name.split(".")[-1]
        if file_extension1 == "csv":
            df1 = pd.read_csv(uploaded_file1)
        elif file_extension1 in ["xls", "xlsx"]:
            df1 = pd.read_excel(uploaded_file1)
        
        # İlk veri setindeki küme dağılımı
        cluster_counts1 = df1['cluster_label'].value_counts()
        cluster_percentage1 = cluster_counts1 / cluster_counts1.sum() * 100
        
        # Karşılaştırma
        st.subheader(" Kümelerin Dağılımı:")
        st.bar_chart(cluster_percentage1)
        
    # İkinci ve üçüncü dosya yükleme widget'ı
    uploaded_files = st.file_uploader("Lütfen iki veri setini de seçin", type=["csv", "xlsx"], accept_multiple_files=True, key="file_uploader2")
    
    if uploaded_files and len(uploaded_files) == 2:
        dfs = []
        for uploaded_file in uploaded_files:
            # Veri setini okuma
            file_extension = uploaded_file.name.split(".")[-1]
            if file_extension == "csv":
                dfs.append(pd.read_csv(uploaded_file))
            elif file_extension in ["xls", "xlsx"]:
                dfs.append(pd.read_excel(uploaded_file))
        
        df1 = dfs[0]
        df2 = dfs[1]
        
        st.subheader('Veri 1 Veri Önizleme')
        st.write(df1.head(100))

        st.subheader('Veri 2 Veri Önizleme')
        st.write(df2.head(100))
       
        st.subheader("Kümeleme Dağılım Grafiği:")
        x = df2['tsne1']
        y = df2['tsne2']
        c = df1['cluster_label']  # df1'in cluster_label sütunu kullanılacak

        # 2D scatter plot çizimi
        fig, ax = plt.subplots(figsize=(10, 8))

        # Her küme için farklı renkler kullanarak scatter plot çiz
        clusters = c.unique()
        for cluster in clusters:
            cluster_data = df2[c == cluster]  # Küme etiketlerini kullanarak veriyi filtrele
            ax.scatter(cluster_data['tsne1'], cluster_data['tsne2'], label=f'Cluster {cluster}')

        ax.set_xlabel('tsne1')
        ax.set_ylabel('tsne2')
        ax.set_title('Küme Etiketleri ile Kümelerin Görselleştirilmesi')
        ax.legend()

        st.write("Küme Etiketleri ile Kümelerin Görselleştirilmesi:")
        st.pyplot(fig)
          
        # Siluet skoru
        silhouette_avg = silhouette_score(df2[['tsne1', 'tsne2']], df1['cluster_label'])

        # Calinski-Harabasz skoru
        ch_score = calinski_harabasz_score(df2[['tsne1', 'tsne2']], df1['cluster_label'])

        # Davies-Bouldin skoru
        db_score = davies_bouldin_score(df2[['tsne1', 'tsne2']], df1['cluster_label'])

        # Sonuçları tablo halinde göster
        results = {
            "Metric": ["Silhouette Score", "Calinski-Harabasz Score", "Davies-Bouldin Score"],
            "Score": [f"{silhouette_avg:.4f}", f"{ch_score:.4f}", f"{db_score:.4f}"]
        }

        results_df = pd.DataFrame(results)

        st.subheader("Kümeleme Performans Metrikleri:")
        st.table(results_df)

    # Dördüncü resim yükleme widget'ı
    uploaded_file3= st.file_uploader("Lütfen resmi seçin", type=["jpg", "jpeg", "png"], key="file_uploader3")
    
    if uploaded_file3 is not None:
        st.subheader("Öneri Sistemi")
        st.image(uploaded_file3, use_column_width=True)



    # Dördüncü resim yükleme widget'ı
    uploaded_file4 = st.file_uploader("Lütfen resmi seçin", type=["jpg", "jpeg", "png"], key="file_uploader4")
    
    if uploaded_file4 is not None:
        st.subheader("Öneri Sistemi")
        st.image(uploaded_file4, use_column_width=True)


if __name__ == "__main__":
    main()
