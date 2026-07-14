from pathlib import Path
from PIL import Image
import streamlit as st

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Skill Swap",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).resolve().parent

# ==========================
# LOAD CSS
# ==========================

with open(ROOT / "styles" / "landing.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================
# MAIN
# ==========================

def main():

    # ==========================
    # NAVBAR
    # ==========================

    logo, menu = st.columns([2, 3])

    with logo:
        st.title("🤝 Skill Swap")

    with menu:

        home, about, login, register = st.columns(4)

        with home:
            st.button("Home", use_container_width=True)

        with about:
            st.button("About", use_container_width=True)

        with login:
            st.button("Login", use_container_width=True)

        with register:
            st.button("Register", use_container_width=True)

    st.divider()
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # ==========================
    # HERO
    # ==========================

    left, right = st.columns([2, 1])

    with left:

        st.subheader("LEARN • TEACH • GROW TOGETHER")

        st.title("Exchange Skills with Students and Professionals")

        st.write(
            """
            Learn programming, design, writing, editing and many more
            skills through peer-to-peer learning.

            Build projects together, expand your network and become
            industry ready.
            """
        )

        btn1, btn2 = st.columns(2)

        with btn1:
            st.button("Get Started", use_container_width=True)

        with btn2:
            st.button("Explore Skills", use_container_width=True)

    with right:

        img = Image.open(ROOT / "assets" / "images" / "handshake.jpg")

        img = img.resize((330, 330))

        st.image(img)

    # ==========================
    # CATEGORIES
    # ==========================

    st.header("🚀 Explore Skill Categories")

    st.write(
        "Choose a category and discover people who can teach or learn with you."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.subheader("💻 Programming")

            st.write("• Python")
            st.write("• Java")
            st.write("• C++")
            st.write("• Web Development")

            st.button("Explore", key="programming")

    with col2:

        with st.container(border=True):

            st.subheader("🎨 Design & Editing")

            st.write("• Canva")
            st.write("• Photoshop")
            st.write("• Figma")
            st.write("• Video Editing")

            st.button("Explore", key="design")

    with col3:

        with st.container(border=True):

            st.subheader("✍️ Content & Writing")

            st.write("• Blogging")
            st.write("• Copywriting")
            st.write("• Script Writing")
            st.write("• Content Writing")

            st.button("Explore", key="writing")

    st.divider()
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # ==========================
    # ABOUT
    # ==========================

    st.header("📖 About Skill Swap")

    st.write(
        """
        Skill Swap is a peer-to-peer learning platform where students and
        professionals teach each other without traditional course fees.

        Whether you are a programmer looking to learn design, a designer
        wanting to improve coding skills, or a writer interested in web
        development, Skill Swap helps you find the perfect learning partner.

        Learn together, teach together and grow together.
        """
    )

    st.divider()
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
        # ==========================
    # HOW IT WORKS
    # ==========================

    st.header("🚀 How Skill Swap Works")

    st.write(
        "Follow these simple steps to start learning and sharing your skills."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown("# 👤")
            st.subheader("Create Profile")
            st.write(
                "Create your profile and add the skills you can teach and the skills you want to learn."
            )

    with c2:
        with st.container(border=True):
            st.markdown("# 🔍")
            st.subheader("Find Skills")
            st.write(
                "Browse different categories and search for people with the skills you need."
            )

    with c3:
        with st.container(border=True):
            st.markdown("# 🤝")
            st.subheader("Connect")
            st.write(
                "Send a skill swap request and connect with students and professionals."
            )

    with c4:
        with st.container(border=True):
            st.markdown("# 🎯")
            st.subheader("Learn Together")
            st.write(
                "Exchange knowledge, collaborate on projects and grow together."
            )

    st.divider()
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # ==========================
    # FOOTER
    # ==========================

    st.header("🤝 Skill Swap")

    st.write(
        "Connecting students and professionals through peer-to-peer learning."
    )

    f1, f2, f3 = st.columns(3)

    with f1:
        st.subheader("Quick Links")
        st.write("🏠 Home")
        st.write("ℹ️ About")
        st.write("🔑 Login")
        st.write("📝 Register")

    with f2:
        st.subheader("Support")
        st.write("📧 Contact Us")
        st.write("❓ Help Center")
        st.write("🔒 Privacy Policy")
        st.write("📄 Terms & Conditions")

    with f3:
        st.subheader("Follow Us")
        st.write("💼 LinkedIn")
        st.write("🐙 GitHub")
        st.write("📸 Instagram")
        st.write("▶️ YouTube")

    st.divider()
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center; color:gray;">
            © 2026 Skill Swap | Made with ❤️ by Bhavin Solanki
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":
    main()