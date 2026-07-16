from pathlib import Path
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).resolve().parent.parent

# =====================================
# LOAD CSS
# =====================================

with open(ROOT / "styles" / "dashboard.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# =====================================
# MAIN
# =====================================

def main():

    # ===============================
    # LOGIN CHECK
    # ===============================

    if "user" not in st.session_state:

        st.warning("Please login first.")

        st.switch_page("pages/Login.py")

    user = st.session_state["user"]

    # ===============================
    # NAVBAR
    # ===============================

    logo, menu = st.columns([2,4])

    with logo:

        st.title("🤝 Skill Swap")

    with menu:

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:

            st.button(
                "📊 Dashboard",
                key="dashboard",
                disabled=True,
                use_container_width=True
            )

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

            if st.button(
                "👤 Profile",
                key="profile",
                use_container_width=True
            ):
                st.switch_page("pages/Profile.py")

        with c5:

            if st.button(
                "🚪 Logout",
                key="logout",
                use_container_width=True
            ):

                st.session_state.clear()

                st.switch_page("app.py")

    st.divider()

    # ===============================
    # WELCOME
    # ===============================

    st.markdown(
        f"## 👋 Welcome Back, {user['full_name']}!"
    )

    st.write("""
Continue your learning journey, connect with talented people,
exchange skills and build amazing projects together.
""")

    st.info(
        "💡 Tip of the Day: Learn one new skill every day."
    )

    st.divider()

    # ===============================
    # DASHBOARD OVERVIEW
    # ===============================

    skills = len(user["skills_offer"].split(","))

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        with st.container(border=True):

            st.markdown("# 📚")

            st.subheader("Skills")

            st.markdown(f"### {skills}")

            st.caption("Skills You Offer")

    with c2:

        with st.container(border=True):

            st.markdown("# 🤝")

            st.subheader("Connections")

            st.markdown("### 0")

            st.caption("Learning Partners")

    with c3:

        with st.container(border=True):

            st.markdown("# 💬")

            st.subheader("Chats")

            st.markdown("### 0")

            st.caption("Active Conversations")

    with c4:

        with st.container(border=True):

            st.markdown("# ⭐")

            st.subheader("Rating")

            st.markdown(f"### {user['rating']}")

            st.caption("Community Rating")

    st.divider()
    # =====================================
    # SEARCH SECTION
    # =====================================

    st.markdown("## 🔍 Find Skills")

    st.write(
        "Search for developers, designers and other learners."
    )

    search = st.text_input(
        "Search Skills",
        placeholder="Python, Java, AI, Canva..."
    )

    b1, b2 = st.columns([1,5])

    with b1:

        if st.button(
            "Search",
            key="search_button",
            use_container_width=True
        ):
            st.switch_page("pages/Search.py")

    with b2:

        st.caption(
            "🔥 Popular Skills: Python • Java • AI • Spring Boot • SQL • Canva"
        )

    st.divider()

    # =====================================
    # RECOMMENDED PEOPLE
    # =====================================

    st.markdown("## ⭐ Recommended People")

    users = [

        {
            "name":"Rahul Patel",
            "role":"Java Backend Developer",
            "skills":"Java • Spring Boot • MySQL",
            "location":"Surat",
            "rating":"4.9 ⭐"
        },

        {
            "name":"Priya Shah",
            "role":"Graphic Designer",
            "skills":"Canva • Photoshop • Figma",
            "location":"Ahmedabad",
            "rating":"4.8 ⭐"
        },

        {
            "name":"Neha Patel",
            "role":"Python Developer",
            "skills":"Python • AI • Streamlit",
            "location":"Vadodara",
            "rating":"5.0 ⭐"
        }

    ]

    for person in users:

        with st.container(border=True):

            left, right = st.columns([5,1])

            with left:

                st.subheader(f"👤 {person['name']}")

                st.write(f"💼 **{person['role']}**")

                st.write(f"🛠️ {person['skills']}")

                st.write(f"📍 {person['location']}")

                st.write(f"⭐ {person['rating']}")

            with right:

                st.button(
                    "Connect",
                    key=f"connect_{person['name']}",
                    use_container_width=True
                )

    st.divider()

    st.caption("© 2026 Skill Swap | Learn • Teach • Grow Together")


# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":
    main()