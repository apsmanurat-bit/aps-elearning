import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman & Gaya Visual
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
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlxl2BWCakg/export?format=csv&gid=747045750"

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            df = pd.read_csv(URL_SHARE)
            # Membersihkan nama semua kolom agar tidak sensitif spasi
            df.columns = [str(c).strip() for c in df.columns]
            
            target_nim = str(nim_input).strip()
            df['NIM'] = df['NIM'].astype(str).str.strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0]['NAMA']
                status_raw = str(student_data.iloc[0]['Status']).strip()
                
                if status_raw.upper() == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status Anda: APPROVED ✅")
                    st.balloons()
                    
                    st.divider()
                    st.subheader("📚 Daftar Mata Kuliah Anda:")
                    
                    # Mencari kolom Mata Kuliah secara otomatis (fleksibel)
                    col_mk = [c for c in df.columns if 'Mata Kuliah' in c][0]
                    mata_kuliah = str(student_data.iloc[0][col_mk]).strip()
                    
                    if mata_kuliah and mata_kuliah != 'nan':
                        list_mk = mata_kuliah.split(',')
                        for mk in list_mk:
                            st.markdown(f"""<div class="course-card">📖 {mk.strip()}</div>""", unsafe_allow_html=True)
                    else:
                        st.info("Belum ada mata kuliah yang terdaftar.")
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda saat ini adalah: {status_raw}")
            else:
                st.error("NIM tidak ditemukan. Mohon pastikan NIM benar.")
                
        except Exception as e:
            st.error("Terjadi kendala saat membaca data. Pastikan kolom 'NAMA', 'NIM', 'Status', dan 'Mata Kuliah' sudah ada di Google Sheets.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.write("Silakan klik tombol di bawah untuk masuk ke ruang kelas digital:")
    st.link_button("🚀 Buka Google Classroom", "https://classroom.google.com/") 

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Jika NIM Anda tidak terdaftar, silakan hubungi Bapak Anggiat Simamora di kantor Prodi.")
