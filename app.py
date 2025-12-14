import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Album Kenangan IMAM",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Islamic theme with dark emerald background
st.markdown("""
<style>
    body {
        background-color: #005b41; /* Dark emerald background */
        color: #FFFFFF; /* White text for contrast */
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #005b41;
    }
    .stApp {
        background-color: #005b41;
    }
    h1, h2, h3 {
        color: #FFFFFF; /* White headers */
        text-align: center;
    }
    .stButton>button {
        background-color: #FFFFFF;
        color: #005b41;
        border: 2px solid #FFFFFF;
    }
    .stButton>button:hover {
        background-color: #F0F0F0;
        border-color: #F0F0F0;
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
        color: #FFFFFF;
    }
    .stSidebar {
        background-color: #003d2b; /* Darker green sidebar */
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for organizational support text
with st.sidebar:
    st.markdown("### Tentang IMAM")
    st.markdown("Ikatan Mahasiswa Muslim Amerika (IMAM) adalah organisasi yang berkomitmen untuk memperkuat ukhuwah dan pengembangan diri mahasiswa Muslim di Amerika.")
    st.markdown("---")
    st.markdown("**Visi:** Menjadi wadah bagi mahasiswa Muslim untuk berkontribusi positif bagi masyarakat.")
    st.markdown("**Misi:** Meningkatkan pemahaman agama, pendidikan, dan solidaritas antar sesama.")

# Header with logo and title
col1, col2 = st.columns([1, 4])  # Small column for logo, larger for title

with col1:
    st.image("logo/Gambar_WhatsApp_2025-12-14_pukul_07.34.52_965dc02a-removebg-preview.png", width=80)

with col2:
    st.title("🌙 Album Kenangan IMAM 🌙")
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
        st.image(photo, caption=f"Kenangan {i+1}", width='stretch')

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
if "show_more" not in st.session_state:
    st.session_state.show_more = False

if st.button("Lihat Lebih Banyak Kenangan"):
    st.session_state.show_more = not st.session_state.show_more

if st.session_state.show_more:
    st.subheader("Link Kenangan Tambahan")
    additional_links = [
        ("WWR", "https://drive.google.com/drive/folders/1wbgyBU_QOjAn4Vohr73PR_nQEm73BSuK"),
        ("IMBER 1", "https://drive.google.com/drive/folders/1Jff_wl8WBQoM00FBSW6N3XBTwOiYPMqz?usp=drive_link"),
        ("IMBER 2", "https://drive.google.com/drive/folders/1C_vPvuhqEa-muo2xOORR4XVphgFlaTLZ"),
        ("SEMINAR KEMUSLIMAHAN", "https://drive.google.com/drive/folders/1rNibp9MjbaBTY5v-G9pVfpFwq_tpAKZS"),
        ("Idul adha", "https://drive.google.com/drive/folders/1Dtg2eHbJeQa3ffBD_Y1NQQ9hlGz3kPUm"),
        ("Kajian Akbar", "https://drive.google.com/drive/folders/1-ertmL1D20WJZWvYbhUFUM5565TmWG7K"),
        ("Kajian Syiar", "https://drive.google.com/drive/folders/1_eiGAXft_P2WIgaapURTBAVdyGkew-cq"),
        ("Khataman 25 April", "https://drive.google.com/drive/folders/1L5GUxOzBGTFbCQXSPX4CdZKO2K2NHM90"),
        ("Muharram", "https://drive.google.com/drive/folders/13d6sHpa8i4JRcH2excDM5Zn_spq9Vg0H"),
        ("Simtudduror", "https://drive.google.com/drive/folders/1APHuLSXnToHjuXWWzzxo-wh_1r08Z7M0"),
        ("Raker", "https://drive.google.com/drive/folders/1vNjqiPwFFsOXeiibRgQqPJ9lQ3SppaA-"),
        ("Sidang ART", "https://drive.google.com/drive/folders/1-R4mhFtJHfALagOzal9fEfiLu5RU--KM")
    ]
    for name, link in additional_links:
        st.markdown(f"[{name}]({link})", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Dibuat dengan 🌙 untuk memperkuat ukhuwah dan kenangan abadi.")
