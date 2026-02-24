import streamlit as st

st.set_page_config(
    page_title="Amos Marbun Portfolio",
    page_icon="💼",
    layout="wide"
)

# ===== HERO SECTION (GLOBAL STYLE) =====
col1, col2 = st.columns([1, 2])

with col1:
    st.image("screenshot.png", width=220)

with col2:
    st.title("Amos Marbun")
    st.subheader("Python & Streamlit Developer")

    st.write(
        "Membangun aplikasi otomatisasi kerja, dashboard monitoring, "
        "dan sistem operasional berbasis web."
    )

    cta1, cta2 = st.columns(2)
    with cta1:
        st.link_button("🚀 Lihat Project", "#project")
    with cta2:
        st.link_button("📞 Hubungi Saya", "#contact")

st.markdown("---")

# ===== SKILL =====
st.header("🛠️ Skill")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Backend**
    - Python
    - Automation
    - API Integration
    """)

with col2:
    st.markdown("""
    **Web & App**
    - Streamlit
    - Dashboard System
    - Deploy Cloud
    """)

with col3:
    st.markdown("""
    **Data**
    - Pandas
    - Data Analysis
    - CSV Processing
    """)

st.markdown("---")

# ===== PROJECT =====
st.header("🚀 Project Unggulan")

# Project 1
st.subheader("📊 Dashboard Monitoring Operasional")

st.write(
    "Dashboard real-time untuk memantau performa operasional dan jadwal kerja."
)

p1, p2 = st.columns(2)

with p1:
    st.link_button(
        "🔗 Demo App",
        "https://jadwal-kerja-eqhfsftfwps6axdunrghan.streamlit.app"
    )

with p2:
    st.link_button(
        "💻 Source Code",
        "https://codespaces.new/amosmarbun86-droid/jadwal-kerja"
    )

st.markdown("")

# Project 2
st.subheader("🤖 Sistem Notifikasi Telegram")

st.write(
    "Bot otomatis untuk alarm H-10, start loading, dan selesai loading."
)

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

st.markdown("---")

# ===== ABOUT =====
st.header("👤 Tentang Saya")

st.write(
    "Developer yang fokus membangun solusi praktis untuk efisiensi kerja, "
    "monitoring operasional, dan otomatisasi berbasis web. "
    "Siap bekerja remote, freelance, maupun full-time."
)

st.markdown("---")

# ===== CONTACT =====
st.header("📞 Kontak")

st.write("📧 Email: amos.marbun86@gmail.com")
st.write("💼 GitHub: https://github.com/amosmarbun86-droid")
st.write("📱 WhatsApp: 085772366047")

st.markdown("---")
st.caption("© 2026 Amos Marbun — Portfolio")
