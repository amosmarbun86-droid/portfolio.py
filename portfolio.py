import streamlit as st
import os

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Amos Marbun | Developer",
    page_icon="🚀",
    layout="wide"
)

# =============================
# CSS PREMIUM CLEAN
# =============================
st.markdown("""
<style>
.big-title {font-size: 52px; font-weight: 800;}
.subtitle {font-size: 22px; color: #9aa0a6; margin-bottom: 20px;}
.section-title {font-size: 30px; font-weight: 700; margin-top: 60px;}
img {border-radius: 50%;}
</style>
""", unsafe_allow_html=True)

# =============================
# AUTO PROFILE IMAGE DETECTOR
# =============================
possible_images = [
    "profile.png",
    "profile.jpg",
    "foto.png",
    "foto.jpg",
    "screenshot.png"
]

profile_image = None

for img in possible_images:
    if os.path.exists(img):
        profile_image = img
        break

# =============================
# HERO SECTION
# =============================
col1, col2 = st.columns([1, 2])

with col1:
    if profile_image:
        st.image(profile_image, width=260)
    else:
        st.info("👤 Foto profil belum ditambahkan")

with col2:
    st.markdown('<div class="big-title">Amos Marbun</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Python & Streamlit Engineer</div>', unsafe_allow_html=True)

    st.write(
        "Membangun sistem automation, dashboard monitoring, "
        "dan solusi operasional berbasis web yang scalable dan efisien."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.link_button("🚀 View Projects", "#projects")

    with c2:
        st.link_button("📩 Contact Me", "#contact")

    with c3:
        st.link_button(
            "📄 Download CV",
            "https://drive.google.com"
        )

st.markdown("---")

# =============================
# SKILLS
# =============================
st.markdown('<div class="section-title">🛠️ Skills</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🐍 Python  \n⚙️ Automation  \n🔌 API Integration")

with col2:
    st.markdown("🌐 Streamlit  \n📊 Dashboard System  \n☁️ Cloud Deploy")

with col3:
    st.markdown("📈 Pandas  \n📂 CSV Processing  \n📊 Data Analysis")

# =============================
# PROJECTS
# =============================
st.markdown('<div class="section-title" id="projects">🚀 Featured Projects</div>', unsafe_allow_html=True)

st.subheader("📊 Operational Monitoring Dashboard")
st.write("Real-time dashboard untuk monitoring performa operasional dan jadwal kerja.")
st.link_button("🔗 Live Demo",
    "https://jadwal-kerja-eqhfsftfwps6axdunrghan.streamlit.app")

st.subheader("🤖 Telegram Alarm System")
st.write("Bot otomatis alarm H-10, start loading, dan selesai loading untuk operasional logistik.")
st.link_button("🔗 Demo Bot",
    "https://t.me/routealarmsiborong2026_bot")

# =============================
# ABOUT
# =============================
st.markdown('<div class="section-title">👤 About Me</div>', unsafe_allow_html=True)

st.write(
    "Developer yang berfokus pada automation system dan monitoring dashboard "
    "menggunakan Python & Streamlit."
)

# =============================
# CONTACT
# =============================
st.markdown('<div class="section-title" id="contact">📞 Contact</div>', unsafe_allow_html=True)

st.write("📧 Email: amos.marbun86@gmail.com")
st.write("💼 GitHub: https://github.com/amosmarbun86-droid")
st.write("📱 WhatsApp: 085772366047")

st.markdown("---")
st.caption("© 2026 Amos Marbun — Professional Developer Portfolio")
