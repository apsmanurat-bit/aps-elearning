import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual (Background & Sidebar)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
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

# 4. LINK DATABASE (FORMAT EXPORT TERKUAT)
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
# Mengarahkan ke GID 747045750 (Form Responses 1)
URL_DATABASE = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=747045750"

# --- LOGIKA MENU ---

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    
    # --- MENU ENROLLMENT (KITA KEMBALIKAN DI SINI) ---
    st.subheader("📝 New Student?")
    st.write("Belum terdaftar di database? Silakan isi form pendaftaran di bawah ini:")
    st.link_button("Click Here to Enroll / Sign Up", "https://forms.gle/vP9n3D8Z5u8y5X6X9")
    
    st.divider()

    # --- MENU CEK NIM ---
    st.subheader("🔐 Access Your Class")
    st.write("Masukkan NIM Bapak/Ibu untuk cek status akses:")
    nim_input = st.text_input("Enter NIM (Example: 1234567)")

    if nim_input:
        try:
            # Membaca data
            df = pd.read_csv(URL_DATABASE)
            
            # Membersihkan nama kolom (ke huruf besar)
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
                    st.info("Silakan buka menu 'Materi (Classroom)' di samping kiri.")
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda saat ini: {status_mhs}. Hubungi Pak Anggiat.")
            else:
                st.error("NIM tidak ditemukan. Pastikan Anda sudah mengisi form di atas.")
        except Exception as e:
            st.error("Koneksi database terhambat. Pastikan internet stabil.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.write("Portal materi di Google Classroom:")
    st.link_button("🚀 Masuk ke Google Classroom", "https://classroom.google.com/") 

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Ada kendala? Silakan hubungi Pak Anggiat langsung di kampus.")