import streamlit as st

st.set_page_config(
    page_title="Amos Marbun Portfolio",
    page_icon="💼",
    layout="wide"
)

# ===== HEADER =====
st.image("screenshot.png")
st.subheader("Python & Streamlit Developer")

st.write("""
Membangun aplikasi untuk otomatisasi kerja, dashboard monitoring,
dan sistem operasional berbasis web.
""")

st.markdown("---")

# ===== SKILL =====
st.header("🛠️ Skill")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    - Python
    - Streamlit
    - Pandas
    """)

with col2:
    st.markdown("""
    - Automation
    - API Integration
    - Telegram Bot
    """)

with col3:
    st.markdown("""
    - Dashboard
    - Data Analysis
    - Deploy App
    """)

st.markdown("---")

# ===== PROJECT =====
st.header("🚀 Project Unggulan")

st.subheader("📊 Dashboard Monitoring Operasional")
st.write("""
Dashboard real-time untuk memantau performa operasional.
""")

st.link_button("🔗 Demo App", "https://jadwal-kerja-eqhfsftfwps6axdunrghan.streamlit.app")
st.link_button("💻 Source Code", "https://codespaces.new/amosmarbun86-droid/jadwal-kerja")

st.markdown("")

st.subheader("🤖 Sistem Notifikasi Telegram")
st.write("""
Bot otomatis untuk alarm dan pengingat jadwal.
""")

st.link_button("🔗 Demo Bot", "https://routealarmsiborong2026_bot")
st.link_button("💻 Source Code", "https://github.com/username/project2")

st.markdown("---")

# ===== ABOUT =====
st.header("👤 Tentang Saya")

st.write("""
Saya developer yang fokus membuat aplikasi praktis untuk
meningkatkan efisiensi kerja dan monitoring data.
Siap bekerja remote, freelance, maupun full-time.
""")

st.markdown("---")

# ===== CONTACT =====
st.header("📞 Kontak")

st.write("📧 Email: amos.marbun86.@gmail.com")
st.write("💼 GitHub: https://github.com/username")
st.write("📱 WhatsApp: 085772366047")

st.markdown("---")
st.caption("© 2026 Amos Marbun")
