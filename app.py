import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN & CSS (HEADER NAVIGASI AKTIF) ---
st.set_page_config(page_title="AngietClass E-Learning", layout="wide")

st.markdown("""
<style>
    /* HEADER GRADIENT (BIRU-UNGU-MERAH) SESUAI GAMBAR */
    header[data-testid="stHeader"] {
        background: linear-gradient(to right, #1e3c72, #6a11cb, #ff4b2b) !important;
        height: 60px;
    }
    
    /* NAVIGASI MENU DI HEADER (BISA DIKLIK) */
    .nav-container {
        position: fixed;
        top: 15px;
        left: 20px;
        z-index: 999999;
        display: flex;
        gap: 30px;
    }
    .nav-link {
        color: white !important;
        text-decoration: none !important;
        font-weight: 800;
        font-size: 15px;
        letter-spacing: 1px;
        transition: 0.3s;
    }
    .nav-link:hover {
        color: #FFD700 !important; /* Kuning Emas */
    }

    .stApp {
        background: linear-gradient(rgba(0, 0, 50, 0.75), rgba(0, 0, 50, 0.75)), 
                    url("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* GAYA KOTAK MATA KULIAH (BESAR, PROPORSIONAL & BERSENI) */
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
        font-size: 32px !important;
        font-weight: 900;
        box-shadow: 8px 8px 20px rgba(0,0,0,0.5);
        border: 3px solid rgba(255,255,255,0.3);
        text-align: center;
        transition: 0.3s;
    }
    .course-card:hover { transform: scale(1.02); filter: brightness(1.1); }
    
    [data-testid="stSidebar"] { display: none; }
</style>

<div class="nav-container">
    <a href="/" class="nav-link">🎓 HOME / SIGN IN</a>
    <a href="https://docs.google.com/forms/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/viewform" target="_blank" class="nav-link">📝 ENROLL / SIGN UP</a>
    <a href="mailto:admin@politeknikmbp.ac.id" class="nav-link">📧 CONTACT</a>
</div>
""", unsafe_allow_html=True)

# --- 2. SISTEM DATABASE (TIDAK BERUBAH - ILOC AMAN) ---
URL_SHARE = "https://docs.google.com/spreadsheets/d/163wKC1PxZU-Zs6Ef6ixPKpIUWLDCfP43Dlxl2BWCakg/export?format=csv&gid=747045750"

classroom_links = {
    "Pancasila Education": "https://classroom.google.com/c/ODUxODU1NDQxNjAw?cjc=skdvjw4",
    "Communicative Grammar II": "https://classroom.google.com/c/ODUxODU2MDg1NDA2?cjc=v5wvneku",
    "Translation II": "https://classroom.google.com/c/ODUxODUzOTMwNTA3?cjc=vtihdzh"
}

color_palette = ["#FF5E5E", "#46EB7E", "#58CCFF", "#F1C40F", "#FF9F43"]

# --- 3. LOGIKA HALAMAN LOGIN ---
st.title("🎓 AngietClass E-Learning")
st.write("Silakan Sign In dengan NIM Anda.")
st.divider()

nim_input = st.text_input("🔑 Masukkan NIM Anda")

if nim_input:
    try:
        df = pd.read_csv(URL_SHARE)
        target_nim = str(nim_input).strip()
        # MESIN ILOC ASLI - TETAP DIJAGA SESUAI KESEPAKATAN
        df.iloc[:, 2] = df.iloc[:, 2].astype(str).str.strip()
        student_data = df[df.iloc[:, 2] == target_nim]
        
        if not student_data.empty:
            nama_mhs = student_data.iloc[0, 1]
            mk_mhs = str(student_data.iloc[0, 5]).strip()
            
            st.success(f"Welcome, {nama_mhs}!")
            st.divider()
            st.subheader("📚 Mata Kuliah Anda:")
            
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
            st.error("NIM tidak ditemukan. Gunakan menu ENROLL di atas jika belum terdaftar.")
    except:
        st.error("Gagal memproses data.")
