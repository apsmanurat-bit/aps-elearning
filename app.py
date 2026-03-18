import streamlit as st

# 1. PENGATURAN HALAMAN (Agar Tampilan Luas & Berseni)
st.set_page_config(page_title="ANGIET CLASS | APS E-LEARNING", layout="wide")

# 2. MENAMPILKAN HEADER EKSKLUSIF (Hasil Desain Terakhir Kita)
# Gambar ini sudah mengandung Gradient, Nama ANGIETCLASS, dan Logo MBP Besar
header_url = "http://googleusercontent.com/image_generation_content/12"
st.image(header_url, use_container_width=True)

st.write("---") # Garis pemisah tipis agar rapi

# 3. KOTAK LOGIN DENGAN FITUR "ENTER" (MENGGUNAKAN st.form)
# Baris ini membungkus input agar tombol Enter di keyboard otomatis memicu Sign In
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1]) # Agar kotak login berada di tengah
    
    with col2:
        with st.form("login_form"):
            st.markdown("<h3 style='text-align: center;'>SIGN IN - APS E-LEARNING</h3>", unsafe_allow_html=True)
            
            username = st.text_input("Username", placeholder="Masukkan Username Anda")
            password = st.text_input("Password", type="password", placeholder="Masukkan Password Anda")
            
            # Tombol Submit (Akan terpicu otomatis saat menekan Enter)
            submit_button = st.form_submit_button("SIGN IN", use_container_width=True)

        # 4. LOGIKA SETELAH TOMBOL DIKLIK ATAU TEKAN ENTER
        if submit_button:
            # Contoh Validasi Sederhana
            if username == "admin" and password == "123":
                st.success(f"Selamat Datang di ANGIETCLASS, {username}!")
                st.balloons() # Efek perayaan kecil agar mahasiswa senang
                # Di sini Bapak bisa arahkan ke materi Google Classroom atau halaman lain
            else:
                st.error("Maaf, Username atau Password salah. Silakan coba lagi.")

# 5. FOOTER (Identitas Tambahan)
st.markdown("<br><p style='text-align: center; color: gray;'>© 2026 ANGIET CLASS - Politeknik MBP Medan</p>", unsafe_allow_html=True)
