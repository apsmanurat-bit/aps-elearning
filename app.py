import streamlit as st
import pandas as pd

# 1. Setting Tampilan
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
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 2. Link Database
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg/export?format=csv"

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            df = pd.read_csv(URL_SHARE)
            
            # Membersihkan nama kolom dari spasi yang tidak sengaja terketik
            df.columns = [str(c).strip() for c in df.columns]
            
            # Mencocokkan NIM
            target_nim = str(nim_input).strip()
            df['NIM'] = df['NIM'].astype(str).str.strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                # Mengambil NAMA dan Status (Sesuai format kolom Bapak)
                nama_mhs = student_data.iloc[0]['NAMA']
                status_mhs = str(student_data.iloc[0]['Status']).strip().upper()
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status Anda: APPROVED ✅")
                    st.balloons()
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda saat ini adalah: {status_mhs}")
            else:
                st.error("NIM tidak ditemukan. Mohon pastikan NIM benar.")
                
        except Exception as e:
            st.error("Judul kolom di Excel belum sesuai. Pastikan ada kolom bernama 'NAMA', 'NIM', dan 'Status'.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi")
    st.link_button("🚀 Masuk Classroom", "https://classroom.google.com/")
