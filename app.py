import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman & Menu Sidebar
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# Gaya Visual (Kembali ke desain awal yang Bapak suka)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    h1, h2, h3, h4, p, span, label { color: #ffffff !important; text-shadow: 1px 1px 2px #000000; }
    .stTextInput input { background-color: #ffffff !important; color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: rgba(0, 0, 30, 0.9); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 2. LINK DATABASE (FORMAT PALING STABIL)
# Saya menggunakan link CSV langsung tanpa variabel SHEET_ID agar tidak ada typo
URL_DATABASE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg/export?format=csv"

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            # Menggunakan pandas dengan pengaturan tambahan agar lebih kuat
            df = pd.read_csv(URL_DATABASE, on_bad_lines='skip')
            
            # Membersihkan data (hapus spasi dan buat huruf besar)
            df.columns = [c.strip().upper() for c in df.columns]
            target_nim = str(nim_input).strip()
            df['NIM'] = df['NIM'].astype(str).str.strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0]['NAMA']
                status_mhs = str(student_data.iloc[0]['STATUS']).strip().upper()
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status Anda: APPROVED ✅")
                    st.balloons()
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda: {status_mhs}.")
            else:
                st.error("NIM tidak ditemukan. Pastikan Anda sudah terdaftar di Google Sheets.")
        except Exception as e:
            st.error(f"Gagal terhubung. Pastikan Google Sheets sudah 'Anyone with the link' dan internet stabil.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.link_button("🚀 Buka Google Classroom", "https://classroom.google.com/") 

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Silakan hubungi Bapak Anggiat Simamora di kantor English Dept.")
