from pathlib import Path
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Register",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).resolve().parent.parent

# =====================================
# LOAD CSS
# =====================================

with open(ROOT / "styles" / "register.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# =====================================
# MAIN
# =====================================

def main():

    left, right = st.columns([1.2, 1])

    # =====================================
    # LEFT HERO SECTION
    # =====================================

    with left:

        st.markdown("# 🤝 Skill Swap")

        st.markdown("## Learn • Teach • Grow Together")

        st.write(
            """
            Join thousands of learners and mentors.

            Share your knowledge, learn new skills,
            collaborate on real-world projects,
            and grow your career with Skill Swap.
            """
        )

        st.divider()

        st.success("🌍 1000+ Active Learners")

        st.success("🤝 500+ Successful Skill Swaps")

        st.success("📚 200+ Skills Available")

        st.success("🚀 Start Your Learning Journey")

    # =====================================
    # REGISTER CARD
    # =====================================

    with right:

        st.markdown("## 🚀 Create Your Account")

        st.write(
            "Create an account to start learning and teaching."
        )

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
            key="fullname"
        )

        username = st.text_input(
            "Username",
            placeholder="Choose a username",
            key="username"
        )

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email",
            key="email"
        )

        password = st.text_input(
            "Password",
            placeholder="Create a password",
            type="password",
            key="password"
        )
        confirm_password = st.text_input(
            "Confirm Password",
            placeholder="Re-enter your password",
            type="password",
            key="confirm_password"
        )

        skills_offer = st.text_input(
            "Skills You Can Teach",
            placeholder="Example: Python, Java, Canva",
            key="skills_offer"
        )

        skills_learn = st.text_input(
            "Skills You Want to Learn",
            placeholder="Example: AI, UI/UX, Video Editing",
            key="skills_learn"
        )

        agree = st.checkbox(
            "I agree to the Terms & Conditions",
            key="terms"
        )
        if st.button(
            "Create Account",
            key="register_btn",
            use_container_width=True
        ):
            st.switch_page("pages/Dashboard.py")

        st.markdown("---")

        st.write("Already have an account?")

        if st.button(
            "Login",
            key="login_btn",
            use_container_width=True
        ):
            st.switch_page("pages/Login.py")


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    main()