import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual (Gambar Latar & Sidebar)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1, h2, h3, h4, p, span, label { 
        color: #ffffff !important; 
        text-shadow: 1px 1px 3px #000000;
    }
    .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 30, 0.9);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar untuk Navigasi (Gateway ke Google Classroom)
with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Materi (Classroom)", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

# 4. Link Database (Sama seperti yang sukses kemarin)
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
URL_CSV = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=747045750"

# --- LOGIKA MENU ---

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.markdown("<h4 style='text-align: center;'>English Dept. Politeknik MBP</h4>", unsafe_allow_html=True)
    st.divider()
    
    st.subheader("📝 New Student?")
    st.link_button("Click Here to Enroll", "https://forms.gle/vP9n3D8Z5u8y5X6X9")

    st.write("")
    st.subheader("🔐 Access Your Class")
    nim_input = st.text_input("Enter your NIM to check approval status")

    if nim_input:
        try:
            # Bagian ini yang krusial untuk koneksi ke Sheet
            df = pd.read_csv(URL_CSV)
            df['NIM'] = df['NIM'].astype(str).str.strip()
            student_data = df[df['NIM'] == nim_input.strip()]
            
            if not student_data.empty:
                status = student_data.iloc[0]['STATUS']
                nama = student_data.iloc[0]['NAMA']
                if status.upper() == "APPROVED":
                    st.success(f"Welcome, {nama}! Your status is APPROVED.")
                    st.info("Pilih menu 'Materi (Classroom)' di samping kiri untuk mulai belajar.")
                else:
                    st.warning(f"Hello {nama}, your status is: {status}. Please contact Mr. Anggiat.")
            else:
                st.error("NIM not found. Please enroll first.")
        except Exception as e:
            # Jika masih error, sistem akan memberitahu detailnya sedikit
            st.error(f"Maaf, sistem tidak bisa membaca database. Pastikan koneksi internet stabil.")

elif menu == "Materi (Classroom)":
    st.title("📚 Materi Perkuliahan")
    st.write("Silakan klik tombol di bawah untuk masuk ke Google Classroom sesuai mata kuliah Bapak:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🚀 Public Speaking Class", "https://classroom.google.com/") 
        st.link_button("📖 Translation I & II Class", "https://classroom.google.com/")
    with col2:
        st.link_button("✍️ Communicative Grammar", "https://classroom.google.com/")
        st.link_button("📂 Download Syllabus (RPS)", "https://google.com")

elif menu == "Bantuan":
    st.title("❓ Bantuan")
    st.write("Hubungi Pak Anggiat jika NIM Bapak/Ibu tidak terdaftar.")