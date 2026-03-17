import streamlit as st
import pandas as pd

# --- 1. CSS: HANYA UNTUK TAMPILAN (LOGIKA TIDAK DISENTUH) ---
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

st.markdown("""
<style>
    /* MERUBAH WARNA HEADER BAWAAN STREAMLIT AGAR KEREN (Sesuai Gambar) */
    header[data-testid="stHeader"] {
        background: linear-gradient(to right, #1e3c72, #6a11cb, #ff4b2b) !important;
    }
    header[data-testid="stHeader"] * {
        color: white !important;
    }

    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    h1, h2, h3, h4, p, span, label { color: #ffffff !important; text-shadow: 1px 1px 2px #000000; }
    .stTextInput input { background-color: #ffffff !important; color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: rgba(0, 0, 30, 0.9); }
    
    /* GAYA KOTAK MATA KULIAH (Tetap Proporsional & Berwarna-warni) */
    .course-card {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 120px;
        border-radius: 20px;
        margin-bottom: 25px;
        text-decoration: none;
        color: #000000 !important;
        font-size: 35px !important;
        font-weight: 900;
        box-shadow: 8px 8px 20px rgba(0,0,0,0.5);
        border: 3px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease-in-out;
        text-align: center;
    }
    .course-card:hover {
        transform: translateY(-5px) scale(1.01);
        filter: brightness(1.1);
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SISTEM DATABASE (BAGIAN INI SANGAT DIJAGA - TIDAK DIUBAH) ---
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/export?format=csv&gid=747045750"

classroom_links = {
    "Pancasila Education": "https://classroom.google.com/c/ODUxODU1NDQxNjAw?cjc=skdvjw4",
    "Communicative Grammar II": "https://classroom.google.com/c/ODUxODU2MDg1NDA2?cjc=v5wvneku",
    "Translation II": "https://classroom.google.com/c/ODUxODUzOTMwNTA3?cjc=vtihdzh"
}

color_palette = ["#FF5E5E", "#46EB7E", "#58CCFF", "#F1C40F", "#FF9F43"]

with st.sidebar:
    st.title("👨‍🏫 Menu Utama")
    menu = st.radio("Pilih Halaman:", ["Akses Kelas & Absensi", "Enroll Mata Kuliah Baru"])
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
            # MESIN UTAMA (ILOC) TETAP ASLI
            df.iloc[:, 2] = df.iloc[:, 2].astype(str).str.strip()
            student_data = df[df.iloc[:, 2] == target_nim]
            
            if not student_data.empty:
                nama_mhs = student_data.iloc[0, 1]
                mk_mhs = str(student_data.iloc[0, 5]).strip()
                
                st.success(f"Welcome, {nama_mhs}!")
                st.divider()
                st.subheader("📚 Klik Mata Kuliah Anda:")
                
                if mk_mhs and mk_mhs != 'nan':
                    list_mk = mk_mhs.split(',')
                    for i, mk in enumerate(list_mk):
                        mk_name = mk.strip()
                        current_color = color_palette[i % len(color_palette)]
                        link = classroom_links.get(mk_name, "https://classroom.google.com")
                        
                        st.markdown(f"""
                            <a href="{link}" target="_blank" class="course-card" style="background-color: {current_color};">
                                📖 {mk_name}
                            </a>
                        """, unsafe_allow_html=True)
                else:
                    st.info("Belum ada mata kuliah terdaftar.")
        except:
            st.error("Gagal memproses data.")

elif menu == "Enroll Mata Kuliah Baru":
    st.title("📝 Enroll Mata Kuliah")
    st.markdown("""
        <a href="https://forms.gle/BapakPunyaLink" target="_blank" class="course-card" style="background-color: #FF9F43;">
            🚀 Enroll / Sign Up Sekarang
        </a>
    """, unsafe_allow_html=True)
