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
day_hour_df = pd.read_csv("https://raw.githubusercontent.com/aldafdyhs/Submissions/main/all_data_bike_sharing.csv")

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

    # Filter data untuk jam 7
    day_hour_df_7 = day_hour_df[day_hour_df['hr'] == 7]

    # Mengelompokkan berdasarkan weekday dan menghitung rata-rata persentase
    result = day_hour_df_7.groupby(by="weekday_y").agg({"casual_y": "mean"})

    # Menampilkan hasil operasi groupby dan agg
    st.write("Rata-Rata Persentase Pelanggan Casual Berdasarkan Weekday pada Jam 7:")
    st.write(result)

    # Membuat diagram pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(result['casual_y'], labels=result.index, autopct='%1.1f%%', startangle=140)
    plt.title('Rata-Rata Persentase Pelanggan Casual Berdasarkan Weekday pada Jam 7', fontsize=15)
    plt.axis('equal')  # Memastikan pie chart berbentuk lingkaran
    st.pyplot(plt)  # Menampilkan plot menggunakan st.pyplot()

# Tab "cuaca"
elif selected_tab == "Cuaca":
    st.subheader("Cuaca")

    # Cuaca yang bagaimana dengan penyewaan rental sepeda tersedikit?
    result = day_hour_df.groupby(by="season_x").agg({"cnt_x": "sum"})
    st.write("Jumlah Pelanggan Berdasarkan Musim:")
    st.write(result)

    # Membuat kanvas
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 6))

    # Daftar warna untuk setiap bar (sesuai dengan jumlah musim)
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Membuat diagram batang dengan seaborn
    sns.barplot(x="season_x", y="cnt_x", data=result.reset_index(), palette=colors, ax=ax)

    # Mengatur label dan judul
    ax.set_ylabel("Jumlah Pelanggan", fontsize=12)
    ax.set_xlabel("Musim", fontsize=12)
    ax.set_title("Jumlah Pelanggan Berdasarkan Musim", loc="center", fontsize=15)

    # Menampilkan diagram
    st.pyplot(fig)  # Menampilkan plot menggunakan st.pyplot()


st.caption("Copyright by AldaFuadiyah")
