import streamlit as st


def show_login_form():
    """
    Displays the login form.
    Returns:
        email, password, remember_me, login_clicked
    """

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.markdown("## 🔐 Login")

    email = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    remember_me = st.checkbox("Remember Me")

    login_clicked = st.button(
        "Login",
        use_container_width=True
    )

    st.markdown(
        "<p style='text-align:center;'>Don't have an account? <b>Register</b></p>",
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    return email, password, remember_me, login_clicked