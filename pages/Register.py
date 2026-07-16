from pathlib import Path
import streamlit as st
from data.db import insert_user

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Register",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).resolve().parent.parent

# =====================================
# LOAD CSS
# =====================================

with open(ROOT / "styles" / "login.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# =====================================
# MAIN
# =====================================

def main():

    left, right = st.columns([1.2, 1])

    # =====================================
    # LEFT SECTION
    # =====================================

    with left:

        st.title("🤝 Skill Swap")

        st.markdown("## Learn • Teach • Grow Together")

        st.write("""
        Join thousands of learners and mentors.

        Share your knowledge, learn new skills,
        collaborate on real-world projects,
        and grow your career with Skill Swap.
        """)

        st.success("🌍 1000+ Active Learners")

        st.success("🤝 500+ Successful Skill Swaps")

        st.success("📚 200+ Skills Available")

        st.info("🚀 Start Your Learning Journey")

    # =====================================
    # RIGHT SECTION
    # =====================================

    with right:

        st.title("🚀 Create Your Account")

        st.caption(
            "Create an account to start learning and teaching."
        )

        st.divider()

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        username = st.text_input(
            "Username",
            placeholder="Choose a username"
        )

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Confirm password"
        )

        location = st.text_input(
            "Location",
            placeholder="City, State"
        )

        skills_offer = st.text_input(
            "Skills You Can Teach",
            placeholder="Python, Java, Canva..."
        )

        skills_learn = st.text_input(
            "Skills You Want to Learn",
            placeholder="AI, Spring Boot..."
        )

        agree = st.checkbox(
            "I agree to the Terms & Conditions"
        )
        st.divider()

        # =====================================
        # CREATE ACCOUNT BUTTON
        # =====================================

        if st.button(
            "🚀 Create Account",
            use_container_width=True
        ):

            success, message = insert_user(

                full_name=full_name,

                username=username,

                email=email,

                password=password,

                location=location,

                skills_offer=skills_offer,

                skills_learn=skills_learn

            )

            if success:

                st.success(message)

                st.balloons()

                st.switch_page("pages/Login.py")

            else:

                st.error(message)

        st.write("")

        st.markdown("---")

        st.write("Already have an account?")

        if st.button(
            "🔑 Login",
            use_container_width=True
        ):

            st.switch_page("pages/Login.py")


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    main()