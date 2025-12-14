import streamlit as st
import time

# --- KONFIGURASI DAN WARNA ---
COLOR_ACCENT = "#005B41" # Hijau Emerald Resmi UKM
COLOR_BACKGROUND = "#FFFDD0" # Cream/Kuning Pucat
LOGO_PATH = "assets/logo_imam.png"

st.set_page_config(
    page_title="Album Kenangan IMAM",
    page_icon="🌙",
    layout="wide", # Tetap wide, tapi kita akan sentralisasi secara manual
    initial_sidebar_state="expanded"
)

# --- LOAD CUSTOM CSS ---
with open("styles.css", "r") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# --- KODE SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.header("Pusat Dokumentasi")
    st.markdown("---")
    st.info("💡 **Visi IMAM:** Memperkuat ukhuwah dan pengembangan diri mahasiswa Muslim.")

    st.subheader("📚 Folder Kenangan")
    
    additional_links = [
        ("WWR", "https://drive.google.com/drive/folders/1wbgyBU_QOjAn4Vohr73PR_nQEm73BSuK"),
        ("IMBER 1", "https://drive.google.com/drive/folders/1Jff_wl8WBQoM00FBSW6N3XBTwOiYPMqz?usp=drive_link"),
        ("IMBER 2", "https://drive.google.com/drive/folders/1C_vPvuhqEa-muo2xOORR4XVphgFlaTLZ"),
        ("SEMINAR KEMUSLIMAHAN", "https://drive.google.com/drive/folders/1rNibp9MjbaBTY5v-G9pVfpFwq_tpAKZS"),
        ("Idul adha", "https://drive.google.com/drive/folders/1Dtg2eHbJeQa3ffBD_Y1NQQ9hlGz3kPUm"),
        ("Kajian Akbar", "https://drive.google.com/drive/folders/1-ertmL1D20WJZWvYbhUFUM5565TmWG7K"),
        ("Kajian Syiar", "https://drive.google.com/drive/folders/1_eiGAXft_P2WIgaapURTBAVdyGkew-cq"),
        ("Raker", "https://drive.google.com/drive/folders/1vNjqiPwFFsOXeiibRgQqPJ9lQ3SppaA-"),
        ("Sidang ART", "https://drive.google.com/drive/folders/1-R4mhFtJHfALagOzal9fEfiLu5RU--KM")
    ]
    
    for name, link in additional_links:
        st.markdown(f"[{name}]({link})") 
    st.markdown("---")
    st.caption("Dibuat dengan cinta untuk ukhuwah abadi.")


# --- KODE KONTEN UTAMA (HEADER SENTRALISASI) ---

# 1. HEADER (Logo dan Judul dibuat Rapat dan agak ke tengah)
# Rasio: [Kosong Kiri (0.5), Logo (1), Judul (4), Kosong Kanan (1.5)] -> Total 7, lebih ke kiri
col_kiri, col_logo, col_title, col_kanan = st.columns([0.5, 1, 4, 1.5])

with col_logo:
    # Logo
    try:
        st.image(LOGO_PATH, width=80) 
    except FileNotFoundError:
        st.error("❌ Logo tidak ditemukan. Cek 'logo/...'")

with col_title:
    # Judul dan Subheader
    st.markdown('<div class="centered-title">', unsafe_allow_html=True)
    st.title("Album Kenangan IMAM 🌙")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="touching-text">
    "Setiap kenangan adalah anugerah dari Allah. Mari kita perkuat ukhuwah melalui jejak-jejak indah yang telah kita lalui bersama."
    </div>
    """, unsafe_allow_html=True)

# Efek salju (animasi)
st.snow()

# --- 2. SENTRALISASI KONTEN UTAMA (Foto & Video) ---
# Gunakan kolom kosong yang lebih kecil untuk membatasi lebar konten
col_main_kiri, col_main_tengah, col_main_kanan = st.columns([0.5, 6, 0.5])

with col_main_tengah:
    st.markdown("---")
    
    # === A. FOTO GRID ===
    st.header("Foto Kenangan")

    photo_paths = [
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.17_0e4b2043.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.22_72fe8b47.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.22_40e25966.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.23_72e6edc9.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_ebff6e54.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_2b2cdf86.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_c5d10d7b.jpg",
        "images/Gambar WhatsApp 2025-12-14 pukul 01.11.31_359eb00d.jpg"
    ]
    
    cols_photo = st.columns(4) # Mengubah menjadi 4 kolom agar lebih padat
    for i, photo in enumerate(photo_paths):
        try:
            with cols_photo[i % 4]: # Memastikan foto masuk ke kolom 1, 2, 3, 4 secara bergantian
                st.image(photo, caption=f"Kenangan {i+1}", use_column_width=True)
        except FileNotFoundError:
            cols_photo[i % 4].warning(f"⚠️ Gambar {i+1} tidak ditemukan.")

    st.markdown("---")

    # === B. VIDEO UTAMA ===
    st.header("Video Utama Memory")
    video_path = "https://drive.google.com/file/d/11grWg3bJbICl5p0RP5jCoQhjAFGvgA5V/view?usp=drive_link"

    # Sentralisasi Video di dalam Konten Tengah
    vid_col_kiri, vid_col_tengah, vid_col_kanan = st.columns([1, 4, 1])
    with vid_col_tengah:
        st.video(video_path)

    # Pesan penutup
    st.markdown("""
    <div class="touching-text" style="text-align: center;">
        "Kenangan ini adalah bukti bahwa kebahagiaan sejati tak pernah pudar. Terima kasih atas setiap detik yang telah kita bagi."
    </div>
    """, unsafe_allow_html=True)

    # Tombol (Optional)
    if st.button("Teguhkan Kembali Niat"):
        st.balloons()
        st.success("Bismillah, semoga Allah berkahi setiap langkah kita. ✨")

    # Footer
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #555;'>Dibuat dengan 🌙 untuk memperkuat ukhuwah dan kenangan abadi.</div>", unsafe_allow_html=True)