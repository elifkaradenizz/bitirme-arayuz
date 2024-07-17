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
# -------------------------------------------