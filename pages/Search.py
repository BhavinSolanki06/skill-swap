from pathlib import Path
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Search",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).resolve().parent.parent

# =====================================
# LOAD CSS
# =====================================

with open(ROOT / "styles" / "search.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# =====================================
# MAIN
# =====================================

def main():

    # ===============================
    # NAVBAR
    # ===============================

    logo, menu = st.columns([2,4])

    with logo:
        st.title("🤝 Skill Swap")

    with menu:

        c1,c2,c3,c4,c5 = st.columns(5)

        with c1:
            if st.button(
                "Dashboard",
                key="dashboard",
                use_container_width=True
            ):
                st.switch_page("pages/Dashboard.py")

        with c2:
            st.button(
                "🔍 Search",
                key="search",
                use_container_width=True,
                disabled=True
            )

        with c3:
            st.button(
                "Chat",
                key="chat",
                use_container_width=True
            )

        with c4:
            st.button(
                "Profile",
                key="profile",
                use_container_width=True
            )

        with c5:
            if st.button(
                "Logout",
                key="logout",
                use_container_width=True
            ):
                st.switch_page("app.py")

    st.divider()

    # ===============================
    # HERO
    # ===============================

    st.markdown("# 🔍 Find Your Perfect Learning Partner")

    st.write(
        """
        Search for students and professionals
        based on skills, interests and experience.
        """
    )

    st.divider()
    # ===============================
    # SEARCH SECTION
    # ===============================

    st.markdown("## 🔎 Search Skills")

    st.write(
        "Find people based on the skills you want to learn."
    )

    search = st.text_input(
        "Search Skills",
        placeholder="Python, Java, AI, Canva...",
        key="search_input"
    )

    btn1, btn2 = st.columns([1,5])

    with btn1:
        st.button(
            "Search",
            key="search_button",
            use_container_width=True
        )

    with btn2:
        st.caption(
            "🔥 Popular Skills: Python • Java • AI • SQL • Canva • Figma • Video Editing"
        )

    st.divider()

    # ===============================
    # SEARCH RESULTS
    # ===============================

    st.markdown("## ⭐ Recommended People")

    users = [

        {
            "name":"Bhavin solanki",
            "role":"Java Backend Developer",
            "skills":"Java • Spring Boot • MySQL",
            "location":"Surat",
            "rating":"4.9 ⭐"
        },

        {
            "name":"Prbhat tiwari",
            "role":"Graphic Designer",
            "skills":"Canva • Photoshop • Figma",
            "location":"Ahmedabad",
            "rating":"4.8 ⭐"
        },

        {
            "name":"Trushil ",
            "role":"Python Developer",
            "skills":"Python • Streamlit • AI",
            "location":"Vadodara",
            "rating":"5.0 ⭐"
        },

        {
            "name":"Abhishek Yadav",
            "role":"AI Engineer",
            "skills":"Machine Learning • Python • TensorFlow",
            "location":"Mumbai",
            "rating":"4.7 ⭐"
        }

    ]

    for user in users:

        with st.container(border=True):

            left, right = st.columns([5,1])

            with left:

                st.subheader(f"👤 {user['name']}")

                st.write(f"💼 **{user['role']}**")

                st.write(f"🛠️ {user['skills']}")

                st.write(f"📍 {user['location']}")

                st.write(f"⭐ {user['rating']}")

            with right:

                st.button(
                    "Connect",
                    key=f"connect_{user['name']}",
                    use_container_width=True
                )

    st.divider()

    # ===============================
    # QUICK FILTERS
    # ===============================

    st.markdown("## 🚀 Popular Categories")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.button("💻 Programming", key="programming", use_container_width=True)

    with c2:
        st.button("🎨 Design", key="design", use_container_width=True)

    with c3:
        st.button("🤖 AI & ML", key="ai", use_container_width=True)

    with c4:
        st.button("📈 Marketing", key="marketing", use_container_width=True)


# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":
    main()