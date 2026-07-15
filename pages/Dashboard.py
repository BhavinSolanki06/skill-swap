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

    username = "Bhavin"

    # =====================================
    # NAVBAR
    # =====================================

    logo, menu = st.columns([2, 4])

    with logo:
        st.title("🤝 Skill Swap")

    with menu:

        c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        if st.button(
            "Dashboard",
            key="nav_dashboard",
            use_container_width=True
        ):
            st.switch_page("pages/Dashboard.py")

    with c2:
        if st.button(
            "Search",
            key="nav_search",
            use_container_width=True
        ):
            st.switch_page("pages/Search.py")

    with c3:
        if st.button(
            "Chat",
            key="nav_chat",
            use_container_width=True
        ):
            st.switch_page("pages/Chat.py")

    with c4:
        if st.button(
            "Profile",
            key="nav_profile",
            use_container_width=True
        ):
            st.switch_page("pages/Profile.py")

    with c5:
        if st.button(
            "Logout",
            key="nav_logout",
            use_container_width=True
        ):
            st.switch_page("app.py")

    st.divider()

    # =====================================
    # WELCOME SECTION
    # =====================================

    st.markdown(f"## 👋 Welcome Back, {username}!")

    st.write(
        """
        Continue your learning journey, connect with talented people,
        exchange skills and build amazing projects together.
        """
    )

    st.info(
        "💡 Tip of the Day: Learn one new skill and teach one skill today!"
    )

    st.divider()

    # =====================================
    # DASHBOARD OVERVIEW
    # =====================================

    st.markdown("## 📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        with st.container(border=True):

            st.markdown("# 📚")

            st.subheader("Skills")

            st.markdown("## 5")

            st.caption("Skills You Offer")

    with col2:

        with st.container(border=True):

            st.markdown("# 🤝")

            st.subheader("Connections")

            st.markdown("## 12")

            st.caption("Learning Partners")

    with col3:

        with st.container(border=True):

            st.markdown("# 💬")

            st.subheader("Chats")

            st.markdown("## 4")

            st.caption("Active Conversations")

    with col4:

        with st.container(border=True):

            st.markdown("# ⭐")

            st.subheader("Rating")

            st.markdown("## 4.9")

            st.caption("Community Rating")

    st.divider()
    # =====================================
    # SEARCH SECTION
    # =====================================

    st.markdown("## 🔍 Find Skills")

    st.write(
        "Search for a skill and discover people who are ready to teach or learn with you."
    )

    search = st.text_input(
        "Search Skills",
        placeholder="Python, Java, UI/UX, Canva...",
        key="search_input"
    )

    btn1, btn2 = st.columns([1, 5])

    with btn1:
        st.button(
            "Search",
            key="search_button",
            use_container_width=True
        )

    with btn2:
        st.caption(
            "🔥 Popular Skills: Python • Java • Figma • SQL • AI • Public Speaking"
        )

    st.divider()

    # =====================================
    # RECOMMENDED PEOPLE
    # =====================================

    st.markdown("## ⭐ Recommended People")

    users = [

        {
            "name": "Priya Shah",
            "role": "Graphic Designer",
            "skills": "Canva • Photoshop • Figma",
            "location": "Ahmedabad",
            "rating": "4.9 ⭐"
        },

        {
            "name": "Rahul Patel",
            "role": "Java Developer",
            "skills": "Java • Spring Boot • MySQL",
            "location": "Surat",
            "rating": "4.8 ⭐"
        },

        {
            "name": "Neha Patel",
            "role": "Python Developer",
            "skills": "Python • Streamlit • AI",
            "location": "Vadodara",
            "rating": "5.0 ⭐"
        }

    ]

    for user in users:

        with st.container(border=True):

            left, right = st.columns([5, 1])

            with left:

                st.subheader(f"👤 {user['name']}")

                st.write(f"**💼 {user['role']}**")

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

    # =====================================
    # RECENT ACTIVITY
    # =====================================

    st.markdown("## 📅 Recent Activity")

    with st.container(border=True):

        st.success("✅ Connected with Rahul Patel")

        st.success("✅ Accepted Skill Swap Request")

        st.info("📚 Completed Java Learning Session")

        st.info("💬 Started a new conversation with Priya Shah")

    st.divider()

    # =====================================
    # QUICK ACTIONS
    # =====================================

    st.markdown("## ⚡ Quick Actions")

    q1, q2, q3, q4 = st.columns(4)

    with q1:
        st.button(
            "➕ Add Skill",
            key="quick_add_skill",
            use_container_width=True
        )

    with q2:
        st.button(
            "🔍 Find Partner",
            key="quick_find_partner",
            use_container_width=True
        )

    with q3:
        st.button(
            "💬 Open Chats",
            key="quick_open_chat",
            use_container_width=True
        )

    with q4:
        st.button(
            "👤 My Profile",
            key="quick_profile",
            use_container_width=True
        )


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    main()