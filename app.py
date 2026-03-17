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

# 4. LINK DATABASE (SUDAH DIPERBAIKI SESUAI LINK BAPAK)
# Perhatikan huruf kecil di ID ini, Pak
URL_DATABASE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg/export?format=csv"

# --- LOGIKA MENU ---

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.markdown("<h4 style='text-align: center;'>English Dept. Politeknik MBP</h4>", unsafe_allow_html=True)
    st.divider()
    
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Enter your NIM to check status")

    if nim_input:
        try:
            # Membaca data
            df = pd.read_csv(URL_DATABASE)
            
            # Membersihkan nama kolom
            df.columns = [c.strip().upper() for c in df.columns]
            
            # Cari NIM
            target_nim = str(nim_input).strip()
            # Membersihkan data NIM di tabel dari spasi
            df['NIM'] = df['NIM'].astype(str).str.strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                status = str(student_data.iloc[0]['STATUS']).strip().upper()
                nama = student_data.iloc[0]['NAMA']
                if status == "APPROVED":
                    st.success(f"Welcome, {nama}! Your status is APPROVED.")
                    st.balloons()
                else:
                    st.warning(f"Hello {nama}, your status is: {status}.")
            else:
                st.error("NIM tidak ditemukan di database.")
        except Exception as e:
            st.error("Gagal membaca data.")
            st.info("Pastikan kolom di Excel Bapak berjudul: NAMA, NIM, dan STATUS.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.write("Silakan masuk ke portal materi:")
    st.link_button("🚀 Buka Google Classroom", "https://classroom.google.com/") 

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Hubungi Pak Anggiat jika ada kendala.")