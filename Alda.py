import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='whitegrid')

# Set tema Streamlit
st.set_page_config(
    page_title="Bike-sharing",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Membaca data CSV dari GitHub
alldata_df = pd.read_csv("https://raw.githubusercontent.com/aldafdyhs/Submissions/main/all_data_bike_sharing.csv")

# Header Streamlit dengan judul keren
st.title('Bike-sharing Dashboard')

# Menambahkan deskripsi untuk memberikan konteks
st.markdown(
    "Selamat datang di Dashboard Bike-sharing! Dashboard ini akan memberikan informasi terkait persentase jumlah pelanggan "
    "dan Tingkat penyewaan terhadap cuaca."
)

# Membuat tab untuk subheader
selected_tab = st.sidebar.radio("Pilih Menu", ["Pukul 7", "Cuaca"])

if selected_tab == "Pukul 7":
    st.subheader("Pukul 7")

    #Berapa persentase jumlah pelanggan casual tertinggi berdasarkan weekday untuk setiap jam 7?
    #Filter data untuk jam 7
    hour_df_7 = hour_df[hour_df['hr'] == 7]
    #Mengelompokkan berdasarkan weekday dan menghitung rata-rata persentase
    result = hour_df_7.groupby(by="weekday").agg({"casual": "mean"})
    print(result)


    #membuat pie chart untuk jumlah pelanggan per hari jam 7
    #Filter data untuk jam 7
    hour_df_7 = hour_df[hour_df['hr'] == 7]
    #Mengelompokkan berdasarkan weekday dan menghitung rata-rata persentase
    result = hour_df_7.groupby(by="weekday").agg({"casual": "mean"})
    #Membuat diagram pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(result['casual'], labels=result.index, autopct='%1.1f%%', startangle=140)
    plt.title('Rata-Rata Persentase Pelanggan Casual Berdasarkan Weekday pada Jam 7', fontsize=15)
    plt.axis('equal')  # Memastikan pie chart berbentuk lingkaran
    plt.show()

# Tab "cuaca"
elif selected_tab == "Cuaca":
    st.subheader("Cuaca")

    #Cuaca yang bagaimana dengan penyewaan rental sepeda tersedikit?
    day_df.groupby(by="season").agg({"cnt": "sum"})

    # Membuat kanvas
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 6))

    # Daftar warna untuk setiap bar (sesuai dengan jumlah musim)
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Membuat diagram batang dengan seaborn
    sns.barplot(x="season", y="cnt", data=day_df, palette=colors, ax=ax)

    # Mengatur label dan judul
    ax.set_ylabel("Jumlah Pelanggan", fontsize=12)
    ax.set_xlabel("Musim", fontsize=12)
    ax.set_title("Jumlah Pelanggan Berdasarkan Musim", loc="center", fontsize=15)

    # Menyembunyikan legend
    ax.legend().remove()

    # Menampilkan diagram
    plt.show()


st.caption("Copyright by AldaFuadiyah")
