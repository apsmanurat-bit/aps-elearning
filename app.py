import streamlit as st
import pandas as pd

# 1. Judul Halaman
st.set_page_config(page_title="AngietClass", layout="wide")
st.title("🎓 AngietClass E-Learning")
st.write("English Dept. Politeknik MBP")

# 2. Link Database (Sudah diperbaiki huruf besar-kecilnya)
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
URL_DATABASE = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=747045750"

# 3. Input NIM
nim_input = st.text_input("Masukkan NIM Anda")

if nim_input:
    try:
        # Proses membaca data
        df = pd.read_csv(URL_DATABASE)
        df.columns = [c.strip().upper() for c in df.columns]
        target_nim = str(nim_input).strip()
        df['NIM'] = df['NIM'].astype(str).str.strip()
        
        student_data = df[df['NIM'] == target_nim]
        
        if not student_data.empty:
            nama_mhs = student_data.iloc[0]['NAMA']
            status_mhs = str(student_data.iloc[0]['STATUS']).strip().upper()
            
            if status_mhs == "APPROVED":
                st.success(f"Welcome, {nama_mhs}! Status: APPROVED ✅")
                st.balloons()
            else:
                st.warning(f"Halo {nama_mhs}, status Anda: {status_mhs}")
        else:
            st.error("NIM tidak ditemukan. Pastikan Anda sudah terdaftar.")
    except Exception:
        st.error("Gagal terhubung ke database. Cek koneksi internet.")
