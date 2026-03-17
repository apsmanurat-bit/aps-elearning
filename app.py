import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

# 2. Gaya Visual (Emas - Biru Tua)
st.markdown("""
    <style>
    .stApp { background-color: #003366 !important; }
    h1, h2, h3, h4, p, span, label { color: #ffffff !important; }
    .stLinkButton a {
        background-color: #FFD700 !important; 
        border-radius: 10px !important;
        margin-bottom: 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .stLinkButton a p { color: #000000 !important; font-weight: bold !important; font-size: 18px !important; }
    .stTextInput input { background-color: #ffffff !important; color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 AngietClass E-Learning")
st.markdown("<h4 style='text-align: center;'>English Dept. Politeknik MBP</h4>", unsafe_allow_html=True)
st.divider()

# 4. Link Database
SHEET_ID = "163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg"
URL_CSV = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=747045750"

# 5. Tombol Pendaftaran
st.subheader("📝 New Student?")
link_form = "https://docs.google.com/forms/d/e/1FAIpQLSfBTCp9tKuRoCODRtofnjlf4wd-0BmnHEt9SnQSiiMFH75v2Q/viewform?usp=sf_link"
st.link_button("Click Here to Enroll", link_form, use_container_width=True)

st.divider()

# 6. Fitur Pengecekan Akses
st.subheader("🔓 Access Your Class")
check_nim = st.text_input("Enter your NIM to check approval status")

# Daftar Link Undangan (Pastikan Nama di Sini Mirip dengan di Form Bapak)
links = {
    "MORAL PHILOSOPHY": "https://classroom.google.com/c/ODUxODU3NzA1MjQz?cjc=gxaxonqf",
    "RESEARCH METHODOLOGY": "https://classroom.google.com/c/ODUxODU4NzU3NDYy?cjc=ywl7b5c2",
    "TRANSLATION II": "https://classroom.google.com/c/ODUxODUzOTMwNTA3?cjc=vtihdzhq",
    "COMMUNICATIVE GRAMMAR II": "https://classroom.google.com/c/ODUxODU2MDg1NDA2?cjc=v5wvneku",
    "PUBLIC SPEAKING": "https://classroom.google.com/c/ODUxODU1Mzk1NDAx?cjc=lhzfnqqd",
    "PENDIDIKAN PANCASILA": "https://classroom.google.com/c/ODUxODU1NDQxNjAw?cjc=skdvjw4v",
    "COMMUNICATIVE GRAMMAR I": "https://classroom.google.com/c/ODQ4MjMwNzg1NjM5?cjc=4rt3q34b"
}

if check_nim:
    try:
        df = pd.read_csv(URL_CSV)
        df.columns = [str(c).strip().upper() for c in df.columns]
        
        col_nim = next((c for c in df.columns if 'NIM' in c), None)
        col_status = next((c for c in df.columns if 'STATUS' in c), None)
        # Mencari kolom mata kuliah (biasanya berisi kata 'MATA' atau 'PILIH' atau 'WHICH')
        col_mk = next((c for c in df.columns if any(x in c for x in ['MATA', 'COURSE', 'PILIH', 'WHICH'])), None)

        if col_nim and col_status:
            user_data = df[df[col_nim].astype(str).str.strip() == str(check_nim).strip()]
            
            if not user_data.empty:
                # Ambil baris terbaru (paling bawah) jika mahasiswa daftar dua kali
                latest_entry = user_data.iloc[-1]
                status_val = str(latest_entry[col_status]).strip().upper()
                
                if status_val == "APPROVED":
                    st.success("✅ Access Granted! Your Classes:")
                    
                    if col_mk:
                        # Mengambil pilihan mata kuliah (misal: "Public Speaking, Translation II")
                        pilihan_user = str(latest_entry[col_mk]).upper()
                        
                        # Loop mengecek setiap mata kuliah di daftar links
                        for nama_mk, link_url in links.items():
                            if nama_mk in pilihan_user:
                                st.link_button(f"Enter {nama_mk} Room", link_url, use_container_width=True)
                    else:
                        st.warning("Kolom pilihan mata kuliah tidak ditemukan di Sheets.")
                else:
                    st.warning("⚠️ Status: PENDING. Tunggu persetujuan Pak Anggiat.")
            else:
                st.error("❌ NIM tidak ditemukan.")
        else:
            st.error("Kolom NIM atau STATUS tidak ditemukan di Sheets.")
            
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

st.divider()
st.caption("© 2026 AngietClass E-Learning - Developed by Mr. Angiet")