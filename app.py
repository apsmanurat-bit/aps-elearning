import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual (Gambar Latar Profesional - SIAP PAKAI)
st.markdown("""
<style>
    /* Menambahkan Gambar Latar dengan Efek Gelap agar Teks Jelas */
    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Warna Teks Putih dengan Bayangan */
    h1, h2, h3, h4, p, span, label { 
        color: #ffffff !important; 
        text-shadow: 1px 1px 3px #000000;
    }

    /* Kotak Input agar tulisan mahasiswa tetap hitam dan jelas */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* Gaya Tombol Emas (Enroll) */
    .stLinkButton a {
        background-color: #FFD700 !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        border: none !important;
        height: 50px !important;
    }
    
    .stLinkButton a p {
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Judul Utama
st.title("🎓 AngietClass E-Learning")
st.markdown("<h4 style='text-align: center;'>English Dept. Politeknik MBP</h4>", unsafe_allow_html=True)
st.divider()

# 4. Link Database (Google Sheets)
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDcFP43Dlx12BWcakg"
URL_CSV = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=747045750"

# 5. Bagian Pendaftaran (New Student)
st.subheader("📝 New Student?")
st.link_button("Click Here to Enroll", "https://forms.gle/vP9n3D8Z5u8y5X6X9") # Ganti dengan link Google Form Bapak jika perlu

st.write("")
st.write("")

# 6. Bagian Akses Kelas (Cek NIM)
st.subheader("🔐 Access Your Class")
nim_input = st.text_input("Enter your NIM to check approval status")

if nim_input:
    try:
        # Membaca data dari Google Sheets
        df = pd.read_csv(URL_CSV)
        
        # Pastikan kolom NIM dibaca sebagai string agar tidak error
        df['NIM'] = df['NIM'].astype(str)
        
        # Cek apakah NIM ada di database
        student_data = df[df['NIM'] == nim_input.strip()]
        
        if not student_data.empty:
            status = student_data.iloc[0]['STATUS']
            nama = student_data.iloc[0]['NAMA']
            
            if status.upper() == "APPROVED":
                st.success(f"Welcome, {nama}! Your status is APPROVED.")
                st.info("Please select your course from the sidebar (Coming Soon).")
            else:
                st.warning(f"Hello {nama}, your status is still: {status}. Please contact Mr. Anggiat.")
        else:
            st.error("NIM not found. Please enroll first or check your NIM again.")
            
    except Exception as e:
        st.error("Connection error. Please try again later.")

# 7. Penutup Footer
st.divider()
st.caption("© 2026 Mr. Angiet Grammar Lite - English Dept. Politeknik MBP")