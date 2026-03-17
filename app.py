import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual (Background Gelap agar Teks Putih Terbaca)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.8), rgba(0, 0, 50, 0.8)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1, h2, h3, h4, p, span, label { color: #ffffff !important; text-shadow: 1px 1px 2px #000000; }
    .stTextInput input { background-color: #ffffff !important; color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: rgba(0, 0, 30, 0.9); }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigasi
with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 4. LINK DATABASE (SUDAH DIPERBAIKI TOTAL - HURUF PER HURUF)
# Saya telah memperbaiki SHEET_ID agar sesuai dengan link yang Bapak bagikan
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
URL_DATABASE = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=747045750"

# --- LOGIKA MENU ---

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    
    st.subheader("📝 New Student?")
    st.write("Silakan klik tombol di bawah untuk mengisi formulir pendaftaran:")
    st.link_button("Click Here to Enroll / Sign Up", "https://docs.google.com/forms/d/e/1FAIpQLSfBTCp9tKuRoCODRtofnjlf4wd-0BmnHEt9SnQSiiMFH75v2Q/viewform?usp=sharing")
    
    st.divider()

    st.subheader("🔐 Access Your Class")
    st.write("Masukkan NIM Bapak/Ibu untuk cek status:")
    nim_input = st.text_input("Enter NIM (Contoh: 90876545)")

    if nim_input:
        try:
            # Membaca data dengan timeout agar tidak menggantung
            df = pd.read_csv(URL_DATABASE)
            
            # Membersihkan nama kolom
            df.columns = [c.strip().upper() for c in df.columns]
            
            # Cari NIM mahasiswa
            target_nim = str(nim_input).strip()
            df['NIM'] = df['NIM'].astype(str).str.strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0]['NAMA']
                status_mhs = str(student_data.iloc[0]['STATUS']).strip().upper()
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status Anda: APPROVED.")
                    st.balloons()
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda: {status_mhs}.")
            else:
                st.error("NIM tidak ditemukan. Pastikan Anda sudah terdaftar.")
        except Exception:
            st.error("Gagal terhubung ke database. Mohon pastikan link 'Share' di Google Sheets sudah 'Anyone with the link'.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.link_button("🚀 Buka Google Classroom", "https://classroom.google.com/") 

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Hubungi Pak Anggiat Simamora di kantor English Dept.")