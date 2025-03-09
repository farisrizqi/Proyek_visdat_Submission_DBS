import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset langsung dari sumber
@st.cache_data
def load_data():
    day_df = pd.read_csv("https://raw.githubusercontent.com/farisrizqi/Proyek_visdat_Submission_DBS/refs/heads/main/data/day.csv")
    hour_df = pd.read_csv("https://raw.githubusercontent.com/farisrizqi/Proyek_visdat_Submission_DBS/refs/heads/main/data/hour.csv")
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar dengan informasi proyek
st.sidebar.markdown("<h1 style='text-align: center;'>Bike Rental<br>Analysis And Visualization</h1>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/farisrizqi/Proyek_visdat_Submission_DBS/blob/main/dashboard/logo_proyek.jpeg?raw=true") 

# Judul Dashboard
st.markdown("<h1 style='text-align: center;'>Bike Rental<br>Analysis And Visualization</h1>", unsafe_allow_html=True)

# Pilih halaman
st.sidebar.header("Menu Halaman Utama :")
page = st.sidebar.radio("Pilih :", ("Page 1 : Preview Dataset & Visualisasi musim serta cuaca", "Page 2 : Analisis, Visualisasi, dan Kesimpulan"))

if page == "Page 1 : Preview Dataset & Visualisasi musim serta cuaca":

    st.sidebar.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
    st.sidebar.header("Fitur Filters :")
    option = st.sidebar.selectbox("Pilih Table Dataset", ["Data Harian", "Data Per Jam"])

    # Streamlit sidebar for date range selection
    st.sidebar.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
    st.sidebar.header("Filter by Date")

    # Filter berdasarkan pilihan tabel
    if option == "Data Harian":
        start_date = st.sidebar.date_input("Start Date", pd.to_datetime(day_df['dteday']).min())
        end_date = st.sidebar.date_input("End Date", pd.to_datetime(day_df['dteday']).max())
        filtered_df = day_df[(pd.to_datetime(day_df['dteday']) >= pd.to_datetime(start_date)) &
                            (pd.to_datetime(day_df['dteday']) <= pd.to_datetime(end_date))]
    else:
        start_date = st.sidebar.date_input("Start Date", pd.to_datetime(hour_df['dteday']).min())
        end_date = st.sidebar.date_input("End Date", pd.to_datetime(hour_df['dteday']).max())
        filtered_df = hour_df[(pd.to_datetime(hour_df['dteday']) >= pd.to_datetime(start_date)) &
                            (pd.to_datetime(hour_df['dteday']) <= pd.to_datetime(end_date))]


    st.sidebar.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
    st.sidebar.header("Filter by Season & Weather")

    # Filtering berdasarkan musim dan cuaca
    season_filter = st.sidebar.multiselect("Pilih Musim", options=[1, 2, 3, 4], default=[1, 2, 3, 4])
    weather_filter = st.sidebar.multiselect("Pilih Cuaca", options=[1, 2, 3], default=[1, 2, 3])

    filtered_df = day_df[day_df['season'].isin(season_filter) & day_df['weathersit'].isin(weather_filter)]
    
    # Membuat dua kolom
    col1, col2 = st.sidebar.columns(2)
    # Menampilkan musim di kolom pertama
    with col1:
        st.write("**Musim**")
        st.write("1. Spring")
        st.write("2. Summer")
        st.write("3. Fall")
        st.write("4. Winter")

    # Menampilkan cuaca di kolom kedua
    with col2:
        st.write("**Cuaca**")
        st.write("1. Clear")
        st.write("2. Cloudy")
        st.write("3. Rain")
    
    
    st.write("## Preview Dataset")
    st.dataframe(filtered_df, use_container_width=True)

    # Mapping musim dan cuaca untuk label
    season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    weather_labels = {1: "Clear", 2: "Cloudy", 3: "Rain"}

    # Visualisasi berdasarkan musim
    st.write("### Penggunaan Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.barplot(x=filtered_df["season"], y=filtered_df["cnt"], ax=ax, palette="coolwarm", order=sorted(filtered_df["season"].unique()))
    ax.set_xlabel("Musim")
    ax.set_ylabel("Total Peminjaman")
    ax.set_xticklabels([season_labels[s] for s in sorted(filtered_df["season"].unique())], rotation=45)
    st.pyplot(fig)

    # Visualisasi berdasarkan cuaca
    st.write("### Penggunaan Sepeda Berdasarkan Cuaca")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.barplot(x=filtered_df["weathersit"], y=filtered_df["cnt"], ax=ax, palette="viridis", order=sorted(filtered_df["weathersit"].unique()))
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Total Peminjaman")
    ax.set_xticklabels([weather_labels[w] for w in sorted(filtered_df["weathersit"].unique())], rotation=45)
    st.pyplot(fig)
    
    st.markdown("<div style='margin-bottom: 50px;'></div>", unsafe_allow_html=True)

elif page == "Page 2 : Analisis, Visualisasi, dan Kesimpulan":
    # Streamlit UI
    st.write("## Analisis Peminjaman Sepeda")
    st.markdown("<div style='margin-bottom: 3px;'></div>", unsafe_allow_html=True)

    # Visualisasi Total Pengguna Berdasarkan Day & Hour
    st.write("#### 1. Penggunaan sepeda tiap musim berdasarkan Day & Hour")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Total Pengguna Berdasarkan Day
    sns.barplot(ax=axes[0], x="season", y="cnt", data=day_df, palette="coolwarm", ci=None)
    axes[0].set_xlabel("Season")
    axes[0].set_ylabel("Total Pengguna")
    axes[0].set_title("Total Pengguna Berdasarkan Day")
    axes[0].set_xticks([0, 1, 2, 3])
    axes[0].set_xticklabels(["Spring", "Summer", "Fall", "Winter"])

    # Total Pengguna Berdasarkan Hour
    sns.barplot(ax=axes[1], x="season", y="cnt", data=hour_df, palette="viridis", ci=None)
    axes[1].set_xlabel("Season")
    axes[1].set_ylabel("Total Pengguna")
    axes[1].set_title("Total Pengguna Berdasarkan Hour")
    axes[1].set_xticks([0, 1, 2, 3])
    axes[1].set_xticklabels(["Spring", "Summer", "Fall", "Winter"])

    plt.tight_layout()
    st.pyplot(fig)

    st.write("Pola Musim menunjukkan pengaruh besar terhadap penggunaan sepeda, "
            "dengan musim semi dan panas memiliki lebih banyak peminjaman daripada musim gugur dan dingin. "
            "Musim bisa menjadi pertimbangan toko maupun peminjam pada saat meminjam sepeda.")

    st.markdown("<div style='margin-bottom: 3px;'></div>", unsafe_allow_html=True)

    # Load data
    day_df = pd.read_csv("https://raw.githubusercontent.com/farisrizqi/Proyek_visdat_Submission_DBS/refs/heads/main/data/day.csv")  # Pastikan file tersedia
    hour_df = pd.read_csv("https://raw.githubusercontent.com/farisrizqi/Proyek_visdat_Submission_DBS/refs/heads/main/data/hour.csv")

    # Pengubahan format tanggal
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])

    # Agregasi data
    df_day = day_df.groupby('dteday')[['casual', 'registered']].sum().reset_index()
    df_hour = hour_df.groupby('hr')[['casual', 'registered']].sum().reset_index()

    st.write("#### 2. Pertumbuhan Peminjaman Pengguna Casual dan Registered")

    # Membuat plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Grafik line chart peminjaman berdasarkan hari
    axes[0].plot(df_day['dteday'], df_day['casual'], label='Peminjaman Casual', color='red', marker='.', linestyle='-', linewidth=1, markersize=4)
    axes[0].plot(df_day['dteday'], df_day['registered'], label='Peminjaman Registered', color='blue', marker='.', linestyle='-', linewidth=1, markersize=4)
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Jumlah Peminjaman')
    axes[0].set_title('Peminjaman Berdasarkan Hari')
    axes[0].legend()
    axes[0].grid(True)
    axes[0].tick_params(axis='x', rotation=45)

    # Grafik line chart peminjaman berdasarkan jam
    axes[1].plot(df_hour['hr'], df_hour['casual'], label='Peminjaman Casual', color='red', marker='.', linestyle='-', linewidth=1, markersize=4)
    axes[1].plot(df_hour['hr'], df_hour['registered'], label='Peminjaman Registered', color='blue', marker='.', linestyle='-', linewidth=1, markersize=4)
    axes[1].set_xlabel('Hour')
    axes[1].set_ylabel('Jumlah Peminjaman')
    axes[1].set_title('Peminjaman Berdasarkan Jam')
    axes[1].legend()
    axes[1].grid(True)
    axes[1].tick_params(axis='x', rotation=45)

    # Tampilkan grafik di Streamlit
    st.pyplot(fig)

    st.write("Pola Pengguna Casual vs Registered menunjukkan bahwa pengguna registered secara keseluruhan "
            "lebih tinggi dan stabil dibandingkan dengan pengguna casual, yang memiliki jumlah peminjaman dengan grafik yang relatif"
            "lebih rendah. Pengguna terdaftar (registered) memiliki peminjaman tertinggi berdasarkan jam, "
            "yaitu pada pukul 17.00. Hal ini bisa memperlihatkan gambaran ramai peminjam casual maupun registered berdasarkan Day dan Hour.")


    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
    st.write("## Conclusion")

    # Conclusion for question 1
    st.write("##### 1. Bagaimana pola penggunaan sepeda di setiap musim?")
    st.write("##### 2. Bagaimana tren pertumbuhan jumlah peminjaman oleh pengguna kasual dan terdaftar?")
    st.write("Kesimpulan : ")

    st.markdown(
        """
        <style>
            .center-align {
                text-align: justify;
            }
        </style>
        <div class="center-align">
            Berdasarkan analisis, pola penggunaan sepeda menunjukkan bahwa musim semi dan panas memiliki jumlah peminjaman
            yang lebih tinggi dibandingkan musim gugur dan dingin. Pengguna terdaftar (registered) menunjukkan tren yang lebih
            stabil dan tinggi dalam peminjaman dibandingkan dengan pengguna kasual (casual) yang memiliki grafik peminjaman
            relatif lebih rendah. Hal ini menunjukkan bahwa musim dan jenis pengguna sangat mempengaruhi tingkat peminjaman sepeda. 
            Dengan demikian, pemilik toko atau penyedia layanan sepeda dapat mempertimbangkan faktor musim dan jenis pengguna 
            untuk merencanakan peminjaman dan operasional mereka.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    
st.sidebar.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
st.sidebar.header("About the Developer")
st.sidebar.write("**Nama :** Faris Nur Rizqiawan")
st.sidebar.write("**Email :** farisnur07@gmail.com")
st.sidebar.write("**ID Dicoding :** farisrizqiawan")
#fix project
