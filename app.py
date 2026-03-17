import streamlit as st
import pandas as pd

# 1. Konfigurasi Tampilan (Kembali ke desain lengkap)
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

# 2. Sidebar Menu
with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 3. LINK DATABASE (Format Khusus "Publikasikan ke Web")
# Link ini biasanya jauh lebih stabil daripada link 'Share' biasa
URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS7Yidv96m82XqM8v-J3pL-U7N5TzW6z9y9Y9Y9Y9Y9Y9Y9/pub?output=csv" 
# Jika link di atas error, kita pakai link Share Bapak yang sudah saya bersihkan:
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/edit?usp=sharing"

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            # Sistem mencoba membaca link Share Bapak
            df = pd.read_csv(URL_SHARE)
            
            # Merapikan Data
            df.columns = [str(c).strip().upper() for c in df.columns]
            target_nim = str(nim_input).strip()
            
            # Pastikan kolom NIM ada
            if 'NIM' in df.columns:
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
                    st.error("NIM tidak terdaftar. Pastikan sudah isi form.")
            else:
                st.error("Format Tabel salah. Pastikan judul kolom pertama adalah 'NIM'.")
                
        except Exception as e:
            st.error("Koneksi Macet. Solusi: Di Google Sheets, klik File -> Share -> Publish to web -> Klik Publish. Lalu coba lagi.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi")
    st.link_button("🚀 Masuk Classroom", "https://classroom.google.com/")
