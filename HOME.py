import streamlit as st
import pandas as pd

def home():
    st.title("Halaman Utama")
    st.write("Selamat datang di Aplikasi Kami!")
    st.write("Berikut adalah daftar nama yang terlibat:")
    st.write("1. Deva Nova Moza Auriel (2360101)")
    st.write("2. Bella Naomi Ginting (2360088)")
    st.write("3. Fadilah Aulia (2360120)")
    st.write("4. Hanisa Aulia Rachmawati (2360137)")
    st.write("5. Barra Yudhistira (2360086)")
    # Tambahkan konten lainnya untuk halaman utama

def density_info():
    st.title("Informasi Kerapatan")
    st.write("Kerapatan dapat didefinisikan sebagai bobot per volume. Untuk benda yang berbentuk butiran (yang bisa dicurahkan), dapat dibedakan antara kerapatan curah dan kerapatan absolut. Dari kedua kerapatan ini dapat diturunkan menjadi nilai kerapatan relatif. Nilai kerapatan dapat digunakan dalam perhitungan nilai koreksi. Kerapatan juga dapat menentukan kepekatan larutan atau kekompakan bentuk padat.")
    st.write("Kerapatan curah adalah bobot bahan padat berbentuk butiran dibagi volume curah yaitu volume bahan dalam bentuk tercurah (seperti beras pada takaran).")
    st.write("Kerapatan absolut adalah bobot bahan dibagi volume nyata bahan. Untuk benda yang bersifat curah, volume nyata adalah volume curah dikurangi volume udara di antara butiran-butiran bahan. Volume celah-celah butiran ini bisa diketahui dengan cara menambahkan cairan (yang akan mengisi celah-celah butiran) yang tidak bereaksi (diserap, diresap, atau membentuk ikatan) dengan bahan.")
    st.write("Kerapatan Relatif adalah perbandingan kerapatan bahan dengan kerapatan air pada temperatur dan tekanan yang sama.")

def viscosity():
    st.title("Viskositas Air")
    st.write("Viskositas air adalah sifat fisik yang mengukur ketebalan atau kekentalan air. Nilai viskositas air bergantung pada suhu air, di mana semakin tinggi suhu, viskositasnya akan semakin rendah. Berikut adalah tabel data viskositas air dari suhu 1°C hingga 20°C:")

    # Membuat dataframe untuk tabel viskositas air
    data = {
        "Temperatur (°C)": list(range(1, 21)),
        "Viskositas (mPa.s)": [1.792, 1.722, 1.656, 1.592, 1.531, 1.472, 1.415, 1.360, 1.307, 1.256, 1.207, 1.159, 1.113, 1.069, 1.026, 0.984, 0.944, 0.905, 0.867, 0.831]
    }
    df = pd.DataFrame(data)
    st.write(df)

def main():
    st.title("Menu")
    menu = ["HOME", "Informasi Kerapatan", "Viskositas Air"]
    cols = st.columns(len(menu))
    for i, col in enumerate(cols):
        col.subheader(menu[i])

    choice = st.radio("Pilih Halaman", menu)

    if choice == "HOME":
        home()
    elif choice == "Informasi Kerapatan":
        density_info()
    elif choice == "Viskositas Air":
        viscosity()

if __name__ == "__main__":
    main()

import streamlit as st

def calculate_absolute_density(sample_weight, water_weight, sample_volume, water_volume):
    # Menghitung kerapatan absolut dalam mg/cm³
    absolute_density = ((sample_weight - water_weight) / (sample_volume - water_volume)) 
    return absolute_density

def calculate_bulk_density(sample_weight,berat_wadah, sample_volume):
    # Menghitung kerapatan curah
    bulk_density = ((sample_weight - berat_wadah) / sample_volume)
    return bulk_density

def calculate_relative_density(absolute_density, nilai_viskositas_air):
    # Menghitung kerapatan relatif
    relative_density = absolute_density / nilai_viskositas_air
    return relative_density

def main():
    st.title('Aplikasi Kalkulator Kerapatan')
    st.subheader('Kerapatan Absolut')
    st.write('Masukkan Data Untuk Menghitung Kerapatan Absolut:')
    sample_weight_abs = st.number_input ('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, step=0.1, format="%.4f")
    water_weight_abs = st.number_input  ('Bobot Gelas Ukur Isi Air (mg):', min_value=0.0, step=0.1, format="%.4f")
    sample_volume_abs = st.number_input ('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, step=0.1, format="%.4f")
    water_volume_abs = st.number_input ('Volume Gelas Ukur Isi Air (mL):', min_value=0.0, step=0.1, format="%.4f")

    st.subheader('Kerapatan Curah')
    st.write('Masukkan Data Untuk Menghitung Kerapatan Curah:')
    sample_weight_bulk = st.number_input ('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, format="%.4f", key='bulk_sample_weight')
    berat_wadah_bulk = st.number_input ('Bobot Gelas Ukur (mg):', min_value=0.0, format="%.4f", key='bulk_berat_wadah')
    sample_volume_bulk = st.number_input ('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, format="%.4f", key='bulk_sample_volume')

    st.subheader('Nilai Viskositas air')
    st.write('Masukkan Data Nilai Viskositas air:')
    nilai_viskositas_air_bulk =  st.number_input ('Nilai Viskositas air (mPa.s):', min_value=0.0, format="%.4f", key='bulk_nilai_viskositas_air')

    if st.button('Hitung Kerapatan Absolut'):
        try:
            absolute_density = calculate_absolute_density(sample_weight_abs, water_weight_abs, sample_volume_abs, water_volume_abs)
            st.subheader('Hasil Perhitungan Kerapatan Absolut:')
            st.write('Kerapatan Absolut:', absolute_density, 'mg/mL')
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

    if st.button('Hitung Kerapatan Curah'):
        try:
            bulk_density = calculate_bulk_density(sample_weight_bulk, berat_wadah_bulk, sample_volume_bulk)
            st.subheader('Hasil Perhitungan Kerapatan Curah:')
            st.write('Kerapatan Curah:', bulk_density, 'mg/mL')
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

    if st.button('Hitung Kerapatan Relatif'):
        try:
            absolute_density = calculate_absolute_density(sample_weight_abs, water_weight_abs, sample_volume_abs, water_volume_abs)
            relative_density = calculate_relative_density(absolute_density, nilai_viskositas_air_bulk)
            st.subheader('Hasil Perhitungan Kerapatan Relatif:')
            st.write('Kerapatan Relatif:', relative_density)
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

if __name__ == '__main__':
    main()
