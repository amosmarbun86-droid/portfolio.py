import streamlit as st

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Amos Marbun | Developer",
    page_icon="🚀",
    layout="wide"
)

# =============================
# CUSTOM CSS (CLEAN PREMIUM)
# =============================
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.big-title {
    font-size: 52px;
    font-weight: 800;
}

.subtitle {
    font-size: 22px;
    color: #9aa0a6;
    margin-bottom: 20px;
}

.section-title {
    font-size: 30px;
    font-weight: 700;
    margin-top: 60px;
    margin-bottom: 25px;
}

.card {
    padding: 25px;
    border-radius: 20px;
    background: #161b22;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

.skill-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #111827;
    text-align: center;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HERO SECTION
# =============================
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 👋")

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
            "https://drive.google.com/your-cv-link"
        )

st.markdown("---")

# =============================
# SKILLS
# =============================
st.markdown('<div class="section-title">🛠️ Skills</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="skill-card">🐍 Python<br>⚙️ Automation<br>🔌 API Integration</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="skill-card">🌐 Streamlit<br>📊 Dashboard System<br>☁️ Cloud Deploy</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="skill-card">📈 Pandas<br>📂 CSV Processing<br>📊 Data Analysis</div>', unsafe_allow_html=True)

# =============================
# PROJECTS
# =============================
st.markdown('<div class="section-title" id="projects">🚀 Featured Projects</div>', unsafe_allow_html=True)

# Project 1
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Operational Monitoring Dashboard")
st.write("Real-time dashboard untuk monitoring performa operasional dan jadwal kerja.")

p1, p2 = st.columns(2)
with p1:
    st.link_button(
        "🔗 Live Demo",
        "https://jadwal-kerja-eqhfsftfwps6axdunrghan.streamlit.app"
    )
with p2:
    st.link_button(
        "💻 Source Code",
        "https://github.com/amosmarbun86-droid/jadwal-kerja"
    )
st.markdown('</div>', unsafe_allow_html=True)

# Project 2
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤖 Telegram Alarm System")
st.write("Bot otomatis alarm H-10, start loading, dan selesai loading untuk operasional logistik.")

p1, p2 = st.columns(2)
with p1:
    st.link_button(
        "🔗 Demo Bot",
        "https://t.me/routealarmsiborong2026_bot"
    )
with p2:
    st.link_button(
        "💻 Source Code",
        "https://github.com/amosmarbun86-droid/alarm-telegram-24jam"
    )
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# ABOUT
# =============================
st.markdown('<div class="section-title">👤 About Me</div>', unsafe_allow_html=True)

st.write(
    "Saya adalah developer yang berfokus pada automation system dan monitoring dashboard. "
    "Berpengalaman membangun aplikasi berbasis Python & Streamlit untuk meningkatkan efisiensi operasional."
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
