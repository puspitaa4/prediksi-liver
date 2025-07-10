import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model_knn.pkl")  # Pastikan file ini sudah ada di folder yang sama

st.title("Prediksi Penyakit Liver")

# Form input pengguna
with st.form("form_prediksi"):
    st.subheader("Masukkan nilai parameter medis:")

    Age = st.number_input("Umur", min_value=1, max_value=100, value=45)
    Gender = st.selectbox("Jenis Kelamin", ["Female", "Male"])
    TB = st.number_input("Total Bilirubin", min_value=0.0, value=1.0)
    DB = st.number_input("Direct Bilirubin", min_value=0.0, value=0.5)
    Alkphos = st.number_input("Alkaline Phosphotase", min_value=0.0, value=200.0)
    Sgpt = st.number_input("SGPT (Alamine Aminotransferase)", min_value=0.0, value=30.0)
    Sgot = st.number_input("SGOT (Aspartate Aminotransferase)", min_value=0.0, value=40.0)
    TP = st.number_input("Total Protein", min_value=0.0, value=6.5)
    ALB = st.number_input("Albumin", min_value=0.0, value=3.0)
    A_G_Ratio = st.number_input("A/G Ratio", min_value=0.0, value=1.0)

    submitted = st.form_submit_button("Prediksi")

if submitted:
    # Konversi gender
    gender_num = 1 if Gender == "Male" else 0

    # Susun input jadi array
    input_data = np.array([[Age, gender_num, TB, DB, Alkphos, Sgpt, Sgot, TP, ALB, A_G_Ratio]])

    # Prediksi menggunakan model
    pred = model.predict(input_data)[0]

    # Ubah hasil prediksi jadi label
    if pred == 1 or pred == "Liver Disease":
        hasil = "Pasien Terindikasi Mengalami Penyakit Liver"
    elif pred == 2 or pred == "Healthy":
        hasil = "Pasien Tidak Terindikasi Penyakit Liver"
    else:
        hasil = f"Prediksi Tidak Diketahui ({pred})"

    # Tampilkan hasil
    st.success(f"Hasil Prediksi: **{hasil}**")
