import streamlit as st
import os

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Amos Marbun | Elite Developer",
    page_icon="🚀",
    layout="wide"
)

# =============================
# PREMIUM CSS
# =============================
st.markdown("""
<style>

.big-title {
    font-size: 56px;
    font-weight: 800;
}

.subtitle {
    font-size: 22px;
    color: #9aa0a6;
    margin-bottom: 15px;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-top: 70px;
    margin-bottom: 25px;
}

.card {
    padding: 25px;
    border-radius: 20px;
    background: #161b22;
    box-shadow: 0 12px 35px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

.stat {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
}

.stat-label {
    text-align: center;
    color: #9aa0a6;
}

img {
    border-radius: 50%;
    box-shadow: 0 0 40px rgba(0, 170, 255, 0.5);
}

</style>
""", unsafe_allow_html=True)

# =============================
# AUTO PROFILE IMAGE
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
        st.image(profile_image, width=280)
    else:
        st.markdown("## 👨‍💻")

with col2:
    st.markdown('<div class="big-title">Amos Marbun</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Python • Streamlit • Automation Engineer</div>', unsafe_allow_html=True)

    st.write(
        "Membangun sistem automation, dashboard monitoring, bot operasional, "
        "dan solusi digital yang meningkatkan efisiensi bisnis secara signifikan."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.link_button("🚀 Projects", "#projects")

    with c2:
        st.link_button("📞 Contact", "#contact")

    with c3:
        st.link_button("📄 Download CV", "https://drive.google.com")

st.markdown("---")

# =============================
# STATS
# =============================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="stat">10+</div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-label">Projects Built</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stat">24/7</div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-label">Automation Systems</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stat">100%</div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-label">Operational Focus</div>', unsafe_allow_html=True)

# =============================
# SKILLS
# =============================
st.markdown('<div class="section-title">🛠️ Core Skills</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write("🐍 Python")
    st.write("⚙️ Automation")
    st.write("🔌 API Integration")

with col2:
    st.write("🌐 Streamlit Apps")
    st.write("📊 Monitoring Dashboard")
    st.write("☁️ Cloud Deploy")

with col3:
    st.write("📈 Data Analysis")
    st.write("📂 CSV Processing")
    st.write("🤖 Bot Development")

# =============================
# PROJECTS
# =============================
st.markdown('<div class="section-title" id="projects">🚀 Featured Projects</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Operational Monitoring Dashboard")
st.write("Dashboard real-time untuk monitoring performa operasional dan jadwal kerja.")

c1, c2 = st.columns(2)
with c1:
    st.link_button("🔗 Live Demo",
        "https://jadwal-kerja-eqhfsftfwps6axdunrghan.streamlit.app")
with c2:
    st.link_button("💻 Source Code",
        "https://github.com/amosmarbun86-droid/jadwal-kerja")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤖 Telegram Alarm System")
st.write("Bot alarm otomatis H-10, start loading, dan selesai loading untuk operasional logistik.")

c1, c2 = st.columns(2)
with c1:
    st.link_button("🔗 Demo Bot",
        "https://t.me/routealarmsiborong2026_bot")
with c2:
    st.link_button("💻 Source Code",
        "https://github.com/amosmarbun86-droid/alarm-telegram-24jam")

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# ABOUT
# =============================
st.markdown('<div class="section-title">👤 About Me</div>', unsafe_allow_html=True)

st.write(
    "Developer berfokus pada solusi automation dan sistem monitoring operasional. "
    "Berpengalaman membangun aplikasi berbasis Python & Streamlit untuk meningkatkan "
    "efisiensi kerja dan visibilitas data."
)

# =============================
# CONTACT
# =============================
st.markdown('<div class="section-title" id="contact">📞 Contact</div>', unsafe_allow_html=True)

st.write("📧 Email: amos.marbun86@gmail.com")
st.write("💼 GitHub: https://github.com/amosmarbun86-droid")
st.write("📱 WhatsApp: 085772366047")

st.markdown("---")
st.caption("© 2026 Amos Marbun — Elite Automation Developer")
