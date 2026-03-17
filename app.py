import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual (PENTING: Memperbaiki Tampilan & Sidebar)
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

# 4. LINK DATABASE (MOHON CEK ID INI SANGAT TELITI, PAK)
# Saya menggunakan ID yang kemarin Bapak gunakan dan berhasil
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
GID = "747045750"
URL_CSV = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"

# --- LOGIKA MENU ---

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.markdown("<h4 style='text-align: center;'>English Dept. Politeknik MBP</h4>", unsafe_allow_html=True)
    st.divider()
    
    st.subheader("📝 New Student?")
    st.link_button("Click Here to Enroll", "https://forms.gle/vP9n3D8Z5u8y5X6X9")

    st.write("")
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Enter your NIM to check status")

    if nim_input:
        try:
            # Mengambil data dengan penanganan error yang lebih detail
            df = pd.read_csv(URL_CSV)
            
            # Membersihkan data NIM (menghilangkan spasi)
            df['NIM'] = df['NIM'].astype(str).str.strip()
            target_nim = str(nim_input).strip()
            
            student_data = df[df['NIM'] == target_nim]
            
            if not student_data.empty:
                status = student_data.iloc[0]['STATUS']
                nama = student_data.iloc[0]['NAMA']
                if str(status).upper() == "APPROVED":
                    st.success(f"Welcome, {nama}! Your status is APPROVED.")
                    st.balloons() # Efek perayaan kecil
                    st.info("Pilih menu 'Materi (Classroom)' di samping kiri untuk mulai belajar.")
                else:
                    st.warning(f"Hello {nama}, your status is: {status}. Please contact Mr. Anggiat.")
            else:
                st.error("NIM tidak ditemukan. Pastikan sudah mendaftar.")
        except Exception as e:
            st.error("Gagal terhubung ke Google Sheets.")
            st.info("Saran: Buka Google Sheets database Bapak, lalu pastikan menu 'Share' sudah 'Anyone with the link'.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.write("Silakan klik mata kuliah Anda:")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🚀 Public Speaking", "https://classroom.google.com/") 
        st.link_button("📖 Translation I & II", "https://classroom.google.com/")
    with col2:
        st.link_button("✍️ Communicative Grammar", "https://classroom.google.com/")

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Hubungi Pak Anggiat di kampus jika ada kendala sistem.")