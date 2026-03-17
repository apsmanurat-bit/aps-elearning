import streamlit as st
import pandas as pd

# --- BAGIAN 1: KONFIGURASI & CSS (Hanya merubah warna tulisan & kotak) ---
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
    
    /* Warna tulisan di kotak dibuat hitam pekat agar kontras */
    .course-card {
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        font-weight: bold;
        font-size: 18px;
        color: #000000 !important; 
        box-shadow: 3px 3px 10px rgba(0,0,0,0.4);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# --- BAGIAN 2: LOGIKA DATABASE (Tetap sama seperti yang sudah berhasil) ---
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/export?format=csv&gid=747045750"

# Daftar warna kotak yang cerah (Pastel)
colors = ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF", "#A0C4FF", "#BDB2FF"]

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            df = pd.read_csv(URL_SHARE)
            target_nim = str(nim_input).strip()
            # Tetap menggunakan indeks kolom (Column 2 untuk NIM)
            df.iloc[:, 2] = df.iloc[:, 2].astype(str).str.strip()
            student_data = df[df.iloc[:, 2] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0, 1] # Kolom B
                mk_mhs = str(student_data.iloc[0, 5]).strip() # Kolom F
                status_mhs = str(student_data.iloc[0, 6]).strip().upper() # Kolom G
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status: APPROVED ✅")
                    st.balloons()
                    
                    st.divider()
                    st.subheader("📚 Daftar Mata Kuliah Anda:")
                    
                    if mk_mhs and mk_mhs != 'nan':
                        list_mk = mk_mhs.split(',')
                        for i, mk in enumerate(list_mk):
                            # Memberikan warna berbeda untuk tiap kotak
                            bg_color = colors[i % len(colors)]
                            st.markdown(f'''
                                <div class="course-card" style="background-color: {bg_color};">
                                    📖 {mk.strip()}
                                </div>
                            ''', unsafe_allow_html=True)
                    else:
                        st.info("Belum ada mata kuliah terdaftar.")
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda: {status_mhs}")
            else:
                st.error("NIM tidak ditemukan.")
        except:
            st.error("Gagal memproses data. Cek koneksi.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi")
    st.link_button("🚀 Masuk Classroom", "https://classroom.google.com/")
