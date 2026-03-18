import streamlit as st
import sqlite3

# --- 1. SETUP DATABASE (Penyimpanan Mahasiswa) ---
def create_usertable():
    conn = sqlite3.connect('users_data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
    conn.commit()
    conn.close()

def add_userdata(username, password):
    conn = sqlite3.connect('users_data.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

# --- 2. TAMPILAN HALAMAN ---
st.set_page_config(page_title="ANGIET CLASS | APS E-LEARNING", layout="wide")
create_usertable()

# Header Desain Kita (Gambar Logo)
header_url = "https://raw.githubusercontent.com/apsmanurat-bit/aps-elearning/main/logo.png" # Ganti dengan link logo Bapak jika ada
st.image("https://via.placeholder.com/1200x300.png?text=ANGIET+CLASS+-+APS+E-LEARNING", use_container_width=True)

# --- 3. MENU SIDEBAR (Pilihan Login/Daftar) ---
menu = ["Login", "Daftar Akun Baru"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

if choice == "Login":
    st.subheader("Silakan Login")
    with st.form("login_form"):
        username = st.text_input("Username (NIM)")
        password = st.text_input("Password", type='password')
        submit_button = st.form_submit_button("SIGN IN")
        
        if submit_button:
            result = login_user(username, password)
            if result:
                st.success(f"Selamat Datang, {username}!")
                st.balloons()
                # Di sini nanti kita pasang link ke materi Bapak
            else:
                st.error("Username atau Password salah. Silakan daftar dulu jika belum punya akun.")

elif choice == "Daftar Akun Baru":
    st.subheader("Buat Akun Mahasiswa")
    new_user = st.text_input("Username Baru (Saran: Pakai NIM)")
    new_password = st.text_input("Password Baru", type='password')
    
    if st.button("Daftar Sekarang"):
        add_userdata(new_user, new_password)
        st.success("Akun berhasil dibuat! Silakan pindah ke menu Login di sebelah kiri.")
