import streamlit as st
import os

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Amos Marbun | Portfolio",
    page_icon="🚀",
    layout="wide"
)

# =============================
# PREMIUM CSS
# =============================
st.markdown("""
<style>

.big-title {font-size: 56px; font-weight: 800;}
.subtitle {font-size: 22px; color: #9aa0a6;}
.section-title {font-size: 34px; font-weight: 700; margin-top: 60px;}

.card {
    padding: 25px;
    border-radius: 18px;
    background: #161b22;
    box-shadow: 0 10px 35px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

.stat {font-size: 42px; font-weight: 800; text-align:center;}
.stat-label {text-align:center; color:#9aa0a6;}

img {
    border-radius: 50%;
    box-shadow: 0 0 40px rgba(0,170,255,0.6);
}

</style>
""", unsafe_allow_html=True)

# =============================
# NAVBAR (SUPER STABLE)
# =============================
page = st.radio(
    "",
    ["🏠 Home", "🚀 Projects", "📞 Contact"],
    horizontal=True
)

st.markdown("---")

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
# HOME PAGE
# =============================
if page == "🏠 Home":

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
            "dan solusi digital untuk meningkatkan efisiensi bisnis."
        )

        st.link_button("📄 Download CV", "https://drive.google.com")

    st.markdown("---")

    # STATS
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="stat">10+</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">Projects Built</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="stat">24/7</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">Automation Systems</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="stat">100%</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">Operational Focus</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🛠️ Core Skills</div>', unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)

    with s1:
        st.write("🐍 Python")
        st.write("⚙️ Automation")
        st.write("🔌 API Integration")

    with s2:
        st.write("🌐 Streamlit Apps")
        st.write("📊 Monitoring Dashboard")
        st.write("☁️ Cloud Deploy")

    with s3:
        st.write("📈 Data Analysis")
        st.write("🤖 Bot Development")
        st.write("📂 CSV Processing")

# =============================
# PROJECTS PAGE
# =============================
elif page == "🚀 Projects":

    st.markdown('<div class="section-title">🚀 Featured Projects</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Operational Monitoring Dashboard")
    st.write("Dashboard real-time untuk monitoring operasional.")

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
    st.write("Bot alarm otomatis untuk operasional logistik.")

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🔗 Demo Bot",
            "https://t.me/routealarmsiborong2026_bot")
    with c2:
        st.link_button("💻 Source Code",
            "https://github.com/amosmarbun86-droid/alarm-telegram-24jam")

    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# CONTACT PAGE
# =============================
elif page == "📞 Contact":

    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    st.write("📧 Email: amos.marbun86@gmail.com")
    st.write("💼 GitHub: https://github.com/amosmarbun86-droid")
    st.write("📱 WhatsApp: 085772366047")

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("© 2026 Amos Marbun — Professional Portfolio")
