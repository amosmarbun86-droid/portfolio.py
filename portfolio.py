import streamlit as st

# ===== CONFIG =====
st.set_page_config(
    page_title="Amos Marbun | Portfolio",
    page_icon="st.image("screenshot.png", width=180)",
    layout="wide"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
.big-title {
    font-size: 48px;
    font-weight: bold;
}
.subtitle {
    font-size: 22px;
    color: #9aa0a6;
}
.card {
    padding:20px;
    border-radius:15px;
    background-color:#111827;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin-bottom:20px;
}
.section-title {
    font-size:28px;
    font-weight:bold;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# ===== HERO SECTION =====
st.markdown('<div class="big-title">👨‍💻 Amos Marbun</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Python & Streamlit Developer</div>', unsafe_allow_html=True)

st.write("""
Spesialis dalam membangun aplikasi otomatisasi, dashboard monitoring,
dan sistem operasional berbasis web.
""")

colA, colB = st.columns(2)

with colA:
    st.link_button("🚀 Lihat Project", "#project")

with colB:
    st.link_button("💬 Hubungi Saya", "https://wa.me/6285772366047")

st.markdown("---")

# ===== SKILL =====
st.markdown('<div class="section-title">🛠️ Skill</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Backend")
    st.write("Python")
    st.write("Automation")
    st.write("API Integration")

with col2:
    st.markdown("### Web & App")
    st.write("Streamlit")
    st.write("Dashboard System")
    st.write("Deploy Cloud")

with col3:
    st.markdown("### Data")
    st.write("Pandas")
    st.write("Data Analysis")
    st.write("CSV Processing")

# ===== PROJECT =====
st.markdown('<div id="project" class="section-title">🚀 Project Unggulan</div>', unsafe_allow_html=True)

# CARD 1
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Dashboard Monitoring Operasional")
st.write("Dashboard real-time untuk memantau performa operasional dan jadwal kerja.")

st.link_button("🔗 Demo App",
"https://jadwal-kerja-eqhfsftfwps6axdunrghan.streamlit.app")

st.link_button("💻 Source Code",
"https://github.com/amosmarbun86-droid/jadwal-kerja")
st.markdown('</div>', unsafe_allow_html=True)

# CARD 2
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤖 Sistem Notifikasi Telegram")
st.write("Bot otomatis untuk alarm H-10, start & selesai loading.")

st.link_button("🔗 Demo Bot",
"https://t.me/routealarmsiborong2026_bot")

st.link_button("💻 Source Code",
"https://github.com/amosmarbun86-droid/alarm-telegram-24jam")
st.markdown('</div>', unsafe_allow_html=True)

# ===== ABOUT =====
st.markdown('<div class="section-title">👤 Tentang Saya</div>', unsafe_allow_html=True)

st.write("""
Developer yang fokus membangun solusi praktis untuk efisiensi kerja.
Berpengalaman membuat sistem monitoring, alarm otomatis,
dan aplikasi operasional berbasis web.
Siap bekerja remote, freelance, maupun full-time.
""")

# ===== CONTACT =====
st.markdown('<div class="section-title">📞 Kontak</div>', unsafe_allow_html=True)

st.write("📧 Email: amos.marbun86@gmail.com")
st.write("💼 GitHub: https://github.com/amosmarbun86-droid")
st.write("📱 WhatsApp: 085772366047")

st.markdown("---")
st.caption("© 2026 Amos Marbun | Built with Streamlit")
