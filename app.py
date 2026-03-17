import streamlit as st
import pandas as pd

# 1. Tampilan Utama
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
    .course-card { background-color: rgba(255, 255, 255, 0.15); padding: 15px; border-radius: 10px; border-left: 5px solid #00ff00; margin-bottom: 10px; color: white; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 2. Database Link
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlxl2BWCakg/export?format=csv&gid=747045750"

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            df = pd.read_csv(URL_SHARE)
            # Membersihkan nama kolom: Hilangkan spasi dan ubah ke HURUF BESAR SEMUA
            df.columns = [str(c).strip().upper() for c in df.columns]
            
            # Cari kolom yang mengandung kata kunci secara otomatis
            col_nim = [c for c in df.columns if 'NIM' in c][0]
            col_nama = [c for c in df.columns if 'NAMA' in c or 'MAHASISWA' in c][0]
            col_status = [c for c in df.columns if 'STATUS' in c][0]
            col_mk = [c for c in df.columns if 'MATA KULIAH' in c or 'MK' in c][0]
            
            target_nim = str(nim_input).strip()
            df[col_nim] = df[col_nim].astype(str).str.strip()
            
            student_data = df[df[col_nim] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0][col_nama]
                status_mhs = str(student_data.iloc[0][col_status]).strip().upper()
                mk_mhs = str(student_data.iloc[0][col_mk]).strip()
                
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
                        st.info("Mata kuliah belum diinput di database.")
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda saat ini: {status_mhs}")
            else:
                st.error("NIM tidak ditemukan.")
                
        except Exception as e:
            st.error("Gagal memproses data. Mohon pastikan file Google Sheets tidak sedang diedit.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi")
    st.link_button("🚀 Masuk Classroom", "https://classroom.google.com/")
