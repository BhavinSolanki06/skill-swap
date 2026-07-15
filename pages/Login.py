from pathlib import Path
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Login",
    page_icon="🤝",
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
    # LEFT HERO SECTION
    # =====================================

    with left:

        st.markdown("# 🤝 Skill Swap")

        st.markdown("## Learn • Teach • Grow Together")

        st.write(
            """
            Welcome to Skill Swap!

            Connect with students and professionals,
            exchange skills, collaborate on projects,
            and build your future together.
            """
        )

        st.divider()

        st.success("🌍 1000+ Active Learners")

        st.success("🤝 500+ Successful Skill Swaps")

        st.success("📚 200+ Skills Available")

        st.success("🚀 Build Your Career Together")

    # =====================================
    # LOGIN CARD
    # =====================================

    with right:

        st.markdown("## 👋 Welcome Back")

        st.write("Login to continue your learning journey.")

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email",
            key="email"
        )

        password = st.text_input(
            "Password",
            placeholder="Enter your password",
            type="password",
            key="password"
        )

        remember = st.checkbox(
            "Remember Me",
            key="remember"
        )

        if st.button(
            "Login",
            key="login_btn",
            use_container_width=True
        ):
            st.switch_page("pages/Dashboard.py")

        st.markdown("---")

        st.write("Don't have an account?")

        if st.button(
            "Create Account",
            key="register_btn",
            use_container_width=True
        ):
            st.switch_page("pages/Register.py")


if __name__ == "__main__":
    main()