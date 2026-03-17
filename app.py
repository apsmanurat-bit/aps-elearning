import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1, h2, h3, h4, p, span, label { color: #ffffff !important; }
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

# 4. LINK DATABASE (DISESUAIKAN DENGAN GAMBAR BAPAK)
# Mengarahkan langsung ke sheet "Form Responses 1"
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
URL_DATABASE = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Form%20Responses%201"

# --- LOGIKA MENU ---

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Enter your NIM to check status")

    if nim_input:
        try:
            # Membaca data
            df = pd.read_csv(URL_DATABASE)
            
            # Membersihkan nama kolom (menghilangkan spasi dan ke huruf besar)
            df.columns = [c.strip().upper() for c in df.columns]
            
            # Cari NIM mahasiswa
            target_nim = str(nim_input).strip()
            # Memastikan kolom NIM dibaca sebagai teks
            df['NIM'] = df['NIM'].astype(str).str.strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                # Mengambil data dari kolom NAMA dan STATUS sesuai gambar Bapak
                nama_mhs = student_data.iloc[0]['NAMA']
                status_mhs = str(student_data.iloc[0]['STATUS']).strip().upper()
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Your status is APPROVED.")
                    st.balloons()
                else:
                    st.warning(f"Hello {nama_mhs}, your status is: {status_mhs}.")
            else:
                st.error("NIM tidak ditemukan. Pastikan Anda sudah mengisi form pendaftaran.")
        except Exception as e:
            st.error("Gagal terhubung ke database. Silakan lapor ke Pak Anggiat.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.write("Silakan akses Google Classroom Anda:")
    st.link_button("🚀 Buka Google Classroom", "https://classroom.google.com/") 

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Hubungi Pak Anggiat di ruang dosen jika ada kendala sistem.")