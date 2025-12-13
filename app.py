import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Album Kenangan IMAM",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for calming green Islamic theme
st.markdown("""
<style>
    body {
        background-color: #98FB98; /* Mint Green background */
        color: #808000; /* Olive Green text */
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #98FB98;
    }
    .stApp {
        background-color: #98FB98;
    }
    h1, h2, h3 {
        color: #008B8B; /* Dark Cyan (Emerald-like) */
        text-align: center;
    }
    .photo-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
    }
    .photo-item {
        flex: 1 1 200px;
        max-width: 200px;
    }
    .video-section {
        text-align: center;
        margin: 20px 0;
    }
    .touching-text {
        font-style: italic;
        text-align: center;
        margin: 20px 0;
        color: #808000;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌙 Album Kenangan IMAM 🌙")

# Inspirational introduction text
st.markdown("""
<div class="touching-text">
    "Setiap kenangan adalah anugerah dari Allah. Mari kita perkuat ukhuwah melalui jejak-jejak indah yang telah kita lalui bersama."
</div>
""", unsafe_allow_html=True)

# Star animation on load for tranquility
st.snow()

# Photo grid section
st.header("Foto Kenangan")

# Placeholder images from images folder (replace with your own images)
photo_paths = [
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.17_0e4b2043.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.22_72fe8b47.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.22_40e25966.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.23_72e6edc9.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_ebff6e54.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_2b2cdf86.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.06.24_c5d10d7b.jpg",  # Replace with your image path
    "images/Gambar WhatsApp 2025-12-14 pukul 01.11.31_359eb00d.jpg"   # Replace with your image path
]

# Display photos in grid
cols = st.columns(3)
for i, photo in enumerate(photo_paths):
    with cols[i % 3]:
        st.image(photo, caption=f"Kenangan {i+1}", use_container_width=True)

# Main video section
st.header("Video Utama Kenangan")

# Placeholder video (replace with your own video path)
video_path = "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4"  # Replace with actual video path

st.video(video_path)

# More touching text
st.markdown("""
<div class="touching-text">
    "Kenangan ini adalah bukti bahwa cinta dan kebahagiaan sejati tak pernah pudar. Terima kasih atas setiap detik yang telah kita bagi."
</div>
""", unsafe_allow_html=True)

# Simple navigation or button (if more content)
if st.button("Lihat Lebih Banyak Kenangan"):
    st.info("Fitur lebih lanjut akan ditambahkan di sini!")

# Footer
st.markdown("---")
st.markdown("Dibuat dengan 🌙 untuk memperkuat ukhuwah dan kenangan abadi.")
