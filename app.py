import streamlit as st
import pandas as pd

# --- 1. CSS: PENGATURAN TAMPILAN (UKURAN & TULISAN) ---
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
    
    /* GAYA DASAR KOTAK: PANJANG, TULISAN HITAM, TEBAL */
    div.stLinkButton > a {
        height: 90px !important; 
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 24px !important; 
        font-weight: 900 !important; 
        color: #000000 !important; 
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.5) !important;
        margin-bottom: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SISTEM DATABASE (TIDAK BERUBAH) ---
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/export?format=csv&gid=747045750"

classroom_links = {
    "Pancasila Education": "https://classroom.google.com/c/ODUxODU1NDQxNjAw?cjc=skdvjw4",
    "Communicative Grammar II": "https://classroom.google.com/c/ODUxODU2MDg1NDA2?cjc=v5wvneku",
    "Translation II": "https://classroom.google.com/c/ODUxODUzOTMwNTA3?cjc=vtihdzh"
}

# Daftar warna spesifik (Merah Pastel, Hijau, Biru, Kuning, Ungu, Oranye, Pink)
specific_colors = ["#FFADAD", "#CAFFBF", "#9BF6FF", "#FDFFB6", "#BDB2FF", "#FFD6A5", "#FFC6FF"]

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Enroll Mata Kuliah Baru", "Bantuan"])
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
            # LOGIN TETAP PAKAI SISTEM ILOC
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
                            # Mengambil warna berbeda berdasarkan urutan (i)
                            bg_color = specific_colors[i % len(specific_colors)]
                            link_tujuan = classroom_links.get(mk_name, "https://classroom.google.com")
                            
                            # CSS KHUSUS UNTUK SETIAP TOMBOL AGAR WARNANYA BERBEDA
                            st.markdown(f"""
                                <style>
                                    div.stLinkButton:nth-of-type({i+1}) > a {{
                                        background-color: {bg_color} !important;
                                    }}
                                </style>
                            """, unsafe_allow_html=True)
                            
                            st.link_button(f"📖 {mk_name}", link_tujuan, use_container_width=True)
                    else:
                        st.info("Belum ada mata kuliah terdaftar.")
                else:
                    st.warning(f"Halo {nama_mhs}, status Anda: {status_mhs}")
            else:
                st.error("NIM tidak ditemukan.")
        except:
            st.error("Gagal memproses data.")

elif menu == "Enroll Mata Kuliah Baru":
    st.title("📝 Enroll Mata Kuliah")
    st.link_button("🚀 Enroll / Sign Up Sekarang", "https://forms.gle/BapakPunyaLink", use_container_width=True)
