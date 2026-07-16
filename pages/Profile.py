from pathlib import Path
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).resolve().parent.parent

# =====================================
# LOAD CSS
# =====================================

with open(ROOT / "styles/profile.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# =====================================
# MAIN
# =====================================

def main():

    # =====================================
    # LOGIN CHECK
    # =====================================

    if "user" not in st.session_state:

        st.warning("Please login first.")

        st.switch_page("pages/Login.py")

    user = st.session_state["user"]

    # =====================================
    # NAVBAR
    # =====================================

    logo, menu = st.columns([2,4])

    with logo:

        st.title("🤝 Skill Swap")

    with menu:

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:

            if st.button(
                "📊 Dashboard",
                key="dashboard",
                use_container_width=True
            ):
                st.switch_page("pages/Dashboard.py")

        with c2:

            if st.button(
                "🔍 Search",
                key="search",
                use_container_width=True
            ):
                st.switch_page("pages/Search.py")

        with c3:

            st.button(
                "💬 Chat",
                key="chat",
                use_container_width=True
            )

        with c4:

            st.button(
                "👤 Profile",
                key="profile",
                disabled=True,
                use_container_width=True
            )

        with c5:

            if st.button(
                "🚪 Logout",
                key="logout",
                use_container_width=True
            ):

                st.session_state.clear()

                st.switch_page("app.py")

    st.divider()

    # =====================================
    # PROFILE HEADER
    # =====================================

    st.markdown(f"# 👤 {user['full_name']}")

    st.write("Welcome to your Skill Swap profile.")

    st.info("Manage your profile and showcase your skills.")

    st.divider()

    # =====================================
    # PERSONAL INFORMATION
    # =====================================

    st.markdown("## 📋 Personal Information")

    left, right = st.columns(2)

    with left:

        st.write("**👤 Full Name**")
        st.write(user["full_name"])

        st.write("")

        st.write("**📧 Email**")
        st.write(user["email"])

    with right:

        st.write("**🆔 Username**")
        st.write(user["username"])

        st.write("")

        st.write("**📍 Location**")
        st.write(user["location"])

    st.divider()
    # =====================================
    # SKILLS SECTION
    # =====================================

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("## 📚 Skills I Can Teach")

        with st.container(border=True):

            skills_offer = user["skills_offer"].split(",")

            for skill in skills_offer:

                st.write(f"✅ {skill.strip()}")

    with c2:

        st.markdown("## 🎯 Skills I Want to Learn")

        with st.container(border=True):

            skills_learn = user["skills_learn"].split(",")

            for skill in skills_learn:

                st.write(f"🚀 {skill.strip()}")

    st.divider()

    # =====================================
    # PROFILE STATISTICS
    # =====================================

    st.markdown("## 📊 My Statistics")

    s1, s2, s3, s4 = st.columns(4)

    with s1:

        with st.container(border=True):

            st.markdown("# 📚")

            st.subheader("Skills")

            st.markdown(f"### {len(skills_offer)}")

            st.caption("Skills Offered")

    with s2:

        with st.container(border=True):

            st.markdown("# 🤝")

            st.subheader("Connections")

            st.markdown("### 0")

            st.caption("Learning Partners")

    with s3:

        with st.container(border=True):

            st.markdown("# 💬")

            st.subheader("Chats")

            st.markdown("### 0")

            st.caption("Messages")

    with s4:

        with st.container(border=True):

            st.markdown("# ⭐")

            st.subheader("Rating")

            st.markdown(f"### {user['rating']}")

            st.caption("Community Rating")

    st.divider()

    # =====================================
    # ACTION BUTTONS
    # =====================================

    st.markdown("## ⚙️ Account")

    b1, b2 = st.columns(2)

    with b1:

        st.button(
            "✏️ Edit Profile",
            key="edit_profile",
            use_container_width=True
        )

    with b2:

        st.button(
            "📤 Share Profile",
            key="share_profile",
            use_container_width=True
        )

    st.divider()

    st.caption("© 2026 Skill Swap | Learn • Teach • Grow Together")


# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":
    main()