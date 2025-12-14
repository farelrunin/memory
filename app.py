import streamlit as st
import time
import random
import base64
from PIL import Image
import pillow_heif
from io import BytesIO

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
    
    # === A. GALERI MOODBOARD ===
    st.subheader("Kilasan Momen-Momen Indah")

    gallery_items = [
        {"type": "image", "path": "images/_MG_3192.JPG"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.17_0e4b2043.jpg"},
        {"type": "video", "path": "assets/video/VID_20250606_171025.mp4"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.22_72fe8b47.jpg"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.22_40e25966.jpg"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.23_72e6edc9.jpg"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_ebff6e54.jpg"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_2b2cdf86.jpg"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_c5d10d7b.jpg"},
        {"type": "image", "path": "images/Gambar WhatsApp 2025-12-14 pukul 01.11.31_359eb00d.jpg"},
        {"type": "image", "path": "images/IMG_1601.JPG"},
        {"type": "image", "path": "images/IMG_1614.JPG"},
        {"type": "image", "path": "images/IMG_1759.JPG"},
        {"type": "image", "path": "images/IMG_1829.JPG"},
        {"type": "image", "path": "images/IMG_1851.JPG"},
        {"type": "image", "path": "images/IMG_3796.HEIC"},
        {"type": "image", "path": "images/IMG_3821.HEIC"},
        {"type": "image", "path": "images/IMG_5348.JPG"},
    ]

    def get_base64_image(image_path):
        try:
            ext = image_path.split('.')[-1].lower()
            if ext == 'heic':
                # Convert HEIC to JPG
                heif_file = pillow_heif.open_heif(image_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )
                # Convert to RGB if necessary
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                # Save to BytesIO as JPG
                buffer = BytesIO()
                image.save(buffer, format='JPEG')
                buffer.seek(0)
                return base64.b64encode(buffer.read()).decode('utf-8')
            else:
                with open(image_path, "rb") as img_file:
                    return base64.b64encode(img_file.read()).decode('utf-8')
        except (FileNotFoundError, Exception) as e:
            st.error(f"Error loading image {image_path}: {e}")
            return None

    html_elements = []
    failed_images = []
    for item in gallery_items:
        if item["type"] == "image":
            width = random.randint(150, 300)
            rotate = random.uniform(-5, 5)
            margin = random.randint(0, 10)
            base64_img = get_base64_image(item["path"])
            if base64_img:
                ext = item["path"].split('.')[-1].lower()
                mime_type = f"image/{ext}" if ext in ['jpg', 'jpeg', 'png', 'gif'] else "image/jpeg"
                html = f'<img src="data:{mime_type};base64,{base64_img}" width="{width}" style="transform: rotate({rotate}deg); margin: {margin}px;" />'
            else:
                failed_images.append(item["path"])
                html = f'<div style="width: {width}px; height: 100px; background: #ccc; display: inline-block; margin: {margin}px; transform: rotate({rotate}deg);">Image not found</div>'
        elif item["type"] == "video":
            width = random.randint(200, 350)
            rotate = random.uniform(-5, 5)
            margin = random.randint(0, 10)
            html = f'<video width="{width}" height="auto" autoplay loop muted playsinline style="transform: rotate({rotate}deg); margin: {margin}px;"><source src="{item["path"]}" type="video/mp4">Browser Anda tidak mendukung tag video.</video>'
        html_elements.append(html)

    if failed_images:
        st.warning(f"Failed to load {len(failed_images)} image(s): {', '.join(failed_images)}")

    gallery_html = '<div class="moodboard-gallery">' + ''.join(html_elements) + '</div>'
    st.markdown(gallery_html, unsafe_allow_html=True)

    st.markdown("---")

    # === B. VIDEO UTAMA ===
    st.header("Video Utama Memory")

    # Gunakan kolom yang lebih lebar untuk video
    vid_col_kiri, vid_col_tengah, vid_col_kanan = st.columns([1, 4, 1])

    with vid_col_tengah:
        # GANTI BARIS INI DENGAN LINK YOUTUBE ANDA
        youtube_url = "https://youtu.be/MGaQYAODMZY?si=2DzOCyzVc8bxcReR"
        # Fungsi st.video akan menangani tautan YouTube dengan sempurna
        st.video(youtube_url)

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