import streamlit as st
import bcrypt

st.title("🔐 Secure data Encryption System")
st.write("Choose Option")
select = st.radio(['login', 'Sign up'])

if select == "login":
    st.markdown("🔓 Login")
    st.write("username")
    input_username = st.text_input("Enter username")
    st.markdown("password")
    password_input = st.text_input("Enter your password", type="password")
    login = st.button('login')
    
    if login:
        st.session_state.logged_in = True
        st.session_state.username = input_username
        st.title("👋 Welcome to the Secure Data Encryption System!")
        st.markdown(f"🧑 Logged in as: {input_username}")
        st.write("---------------------------------------------")
        st.markdown("🔐 What you can do here:")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("📥 Store Data")
            st.write("Encrypt sensitive data and store it securely using your own passkey.")
        
        with col2:
            st.markdown("🔓 Retrieve Data")
            st.write("Decrypt and view your stored data anytime using your passkey.")
        
        st.info("Use the sidebar menu to navigate between tools.")
        st.info("🔒 Your data is encrypted using advanced cryptography and stored securely.")

else:
    st.markdown("📝 Create an Account")
    st.write("username")
    input_username = st.text_input("Enter username")
    st.markdown("password")
    password_input = st.text_input("Enter your password", type="password")
    signup = st.button('Signup')
    
    if signup:
        # Hash the password to store it securely
        # `encode('utf-8')` converts the password into a byte format because bcrypt requires it in bytes
        # `bcrypt.gensalt()` generates a random salt to make each password unique before hashing it
        # `bcrypt.hashpw()` hashes the password along with the salt (making it more secure)
        hashed_password = bcrypt.hashpw(password_input.encode('utf-8'), bcrypt.gensalt())
        
        # Store the username and hashed password in session state
        st.session_state.user_data = (input_username, hashed_password)
        st.success("Account created!! Please login.")
