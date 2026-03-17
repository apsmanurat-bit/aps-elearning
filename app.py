import streamlit as st
import pandas as pd

# --- BAGIAN 1: CSS (KOTAK DIPERPANJANG FULL WIDTH) ---
# Bagian ini hanya mengatur "Baju" atau tampilan, bukan mesin aplikasi.
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
    
    /* KOTAK DIPERPANJANG HORIZONTAL (FULL WIDTH) */
    div.stLinkButton > a {
        width: 100% !important; 
        height: 80px !important; 
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 22px !important; 
        font-weight: bold !important;
        color: #000000 !important;
        border-radius: 15px !important;
        border: none !important;
        text-decoration: none !important;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.5) !important;
        margin-bottom: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- BAGIAN 2: LOGIKA DATABASE (SISTEM INTI - TIDAK SAYA UBAH) ---
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/export?format=csv&gid=747045750"

classroom_links = {
    "Pancasila Education": "https://classroom.google.com/c/ODUxODU1NDQxNjAw?cjc=skdvjw4",
    "Communicative Grammar II": "https://classroom.google.com/c/ODUxODU2MDg1NDA2?cjc=v5wvneku",
    "Translation II": "https://classroom.google.com/c/ODUxODUzOTMwNTA3?cjc=vtihdzh"
}

colors = ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF", "#A0C4FF", "#BDB2FF"]

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Bantuan"])
    st.divider()
    st.caption("English Dept. Politeknik MBP")

if menu == "Akses Kelas & Absensi":
    st.title("🎓 AngietClass E-Learning")
    st.divider()
    nim_input = st.text_input("Masukkan NIM Anda")

    if nim_input:
        try:
            df = pd.read_csv(URL_SHARE)
            target_nim = str(nim_input).strip()
            # MENGGUNAKAN SISTEM ILOC YANG SUDAH BERHASIL
            df.iloc[:, 2] = df.iloc[:, 2].astype(str).str.strip()
            student_data = df[df.iloc[:, 2] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0, 1]
                mk_mhs = str(student_data.iloc[0, 5]).strip()
                status_mhs = str(student_data.iloc[0, 6]).strip().upper()
                
                if status_mhs == "APPROVED":
                    st.success(f"Welcome, {nama_mhs}! Status: APPROVED ✅")
                    
                    st.divider()
                    st.subheader("📚 Klik Mata Kuliah untuk Masuk Classroom:")
                    
                    if mk_mhs and mk_mhs != 'nan':
                        list_mk = mk_mhs.split(',')
                        for i, mk in enumerate(list_mk):
                            mk_name = mk.strip()
                            bg_color = colors[i % len(colors)]
                            link_tujuan = classroom_links.get(mk_name, "https://classroom.google.com")
                            
                            st.markdown(f'<style>div.stLinkButton:nth-of-type({i+1}) > a {{ background-color: {bg_color} !important; }}</style>', unsafe_allow_html=True)
                            st.link_button(f"📖 {mk_name}", link_tujuan)
                    else:
                        st.info("Mata kuliah belum terdaftar.")
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda: {status_mhs}")
            else:
                st.error("NIM tidak ditemukan.")
        except:
            st.error("Gagal memproses data.")
