import streamlit as st
import pandas as pd

# 1. Konfigurasi Tampilan
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

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
    .course-card { background-color: rgba(255, 255, 255, 0.15); padding: 15px; border-radius: 10px; border-left: 5px solid #00ff00; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 2. Link Database
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/export?format=csv&gid=747045750"

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            # Membaca file CSV dari Google Sheets
            df = pd.read_csv(URL_SHARE)
            
            # Kita gunakan nomor kolom agar tidak pusing nama judul:
            # Kolom 1 (index 1) = NAMA
            # Kolom 2 (index 2) = NIM
            # Kolom 5 (index 5) = Mata Kuliah
            # Kolom 6 (index 6) = Status
            
            target_nim = str(nim_input).strip()
            # Membersihkan kolom NIM (kolom ke-3 di Excel Bapak)
            df.iloc[:, 2] = df.iloc[:, 2].astype(str).str.strip()
            
            # Mencari data mahasiswa
            student_data = df[df.iloc[:, 2] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0, 1]  # Kolom B (NAMA)
                mk_mhs = str(student_data.iloc[0, 5]).strip()  # Kolom F (Mata Kuliah)
                status_mhs = str(student_data.iloc[0, 6]).strip().upper()  # Kolom G (Status)
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status: APPROVED ✅")
                    st.balloons()
                    
                    st.divider()
                    st.subheader("📚 Daftar Mata Kuliah Anda:")
                    if mk_mhs and mk_mhs != 'nan':
                        list_mk = mk_mhs.split(',')
                        for mk in list_mk:
                            st.markdown(f'<div class="course-card">📖 {mk.strip()}</div>', unsafe_allow_html=True)
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda saat ini: {status_mhs}")
            else:
                st.error("NIM tidak ditemukan di database.")
                
        except Exception as e:
            st.error(f"Koneksi terganggu. Mohon tunggu 1 menit dan coba lagi.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi")
    st.link_button("🚀 Masuk Classroom", "https://classroom.google.com/")
