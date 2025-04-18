import streamlit as st
import bcrypt
from cryptography.fernet import Fernet
import hashlib
import base64  # Import base64 module

# Initialize session state if not already initialized
if "user_data" not in st.session_state:
    st.session_state.user_data = {}  # Store users in a dictionary

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "encrypted_data" not in st.session_state:
    st.session_state.encrypted_data = {}  # Store encrypted data

# Title of the app
st.title("🔐 Secure Data Encryption System")

# Function to generate a key from the passkey
def generate_key_from_passkey(passkey: str):
    # Hash the passkey and use the hash as the encryption key
    passkey_hash = hashlib.sha256(passkey.encode()).digest()  # Use SHA-256 hash
    return Fernet(base64.urlsafe_b64encode(passkey_hash[:32]))  # Generate key for Fernet

# Show the sidebar only if the user is logged in
if st.session_state.logged_in:
    # Sidebar with options
    with st.sidebar:
        st.write("-----------------------------")
        st.write(f"Logged in as: {st.session_state.username}")
        option = st.radio("Select an option", ["Store Data", "Retrieve Data", "Logout"])
        
        if option == "Logout":
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state.encrypted_data = {}  # Reset encrypted data
            st.rerun()  # Rerun the app to reset the login state

    # Content after logging in
    if option == "Store Data":
        st.subheader("Store Data")
        # Input data and passkey to encrypt
        data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Enter your passkey", type="password")
        
        if st.button("Encrypt and Store Data"):
            if data and passkey:
                try:
                    # Generate the key from the passkey
                    cipher = generate_key_from_passkey(passkey)

                    # Encrypt the data using the derived key
                    encrypted_data = cipher.encrypt(data.encode())

                    # Store encrypted data in session state under the user's username
                    if st.session_state.username not in st.session_state.encrypted_data:
                        st.session_state.encrypted_data[st.session_state.username] = []

                    st.session_state.encrypted_data[st.session_state.username].append(encrypted_data)

                    st.success("Data encrypted and stored successfully.")
                except Exception as e:
                    st.error(f"Error encrypting data: {e}")
            else:
                st.error("Please enter both data and a passkey.")

    elif option == "Retrieve Data":
        st.subheader("Retrieve Data")
        
        # Check if the user has any encrypted data stored
        if st.session_state.username in st.session_state.encrypted_data:
            encrypted_list = st.session_state.encrypted_data[st.session_state.username]
            st.write("Your encrypted data:")
            for idx, enc_data in enumerate(encrypted_list):
                st.write(f"{idx + 1}. Encrypted Data #{idx + 1}")  # Display encrypted data label
                st.write(enc_data.decode())  # Display the actual encrypted data as a string
        else:
            st.write("No encrypted data found. Please store some data first.")

        # Input passkey to decrypt data
        passkey = st.text_input("Enter your passkey to retrieve the original data", type="password")
        
        if st.button("Decrypt Data"):
            if passkey:
                # Check if encrypted data exists for the logged-in user
                if st.session_state.username in st.session_state.encrypted_data:
                    encrypted_list = st.session_state.encrypted_data[st.session_state.username]
                    
                    decrypted_data = None
                    for encrypted_data in encrypted_list:
                        try:
                            # Generate the cipher with the passkey-derived key
                            cipher = generate_key_from_passkey(passkey)

                            # Decrypt the data
                            decrypted_data = cipher.decrypt(encrypted_data).decode()
                            
                            # If decryption is successful, display the decrypted data
                            st.success("Decrypted data:")
                            st.write(decrypted_data)
                            break
                        except Exception as e:
                            # If decryption fails, continue to the next data or display an error message
                            st.error(f"Error decrypting data: {e}")
                else:
                    st.write("No encrypted data found for this user.")
            else:
                st.error("Please enter a passkey to decrypt the data.")
    
else:
    # Show login or sign up options if not logged in
    st.header("Select an option")
    select = st.radio('Select an option', ['Login', 'Sign Up'])

    if select == "Login":
        input_username = st.text_input("Enter username")
        password_input = st.text_input("Enter your password", type="password")
        login = st.button('Login')

        if login:
            # Check if the user exists in session state and validate the password
            if input_username in st.session_state.user_data:
                hashed_password = st.session_state.user_data[input_username]
                if bcrypt.checkpw(password_input.encode('utf-8'), hashed_password):
                    # Set session state for login
                    st.session_state.logged_in = True
                    st.session_state.username = input_username
                    st.rerun()  # Refresh the page after login using st.experimental_rerun()
                else:
                    st.write("Incorrect password. Please try again.")  # Message for incorrect password
            else:
                st.write("Username not found. Please sign up first.")  # Message for username not found

    elif select == "Sign Up":
        st.markdown("**📝 Create an Account**")
        input_username = st.text_input("Enter username")
        password_input = st.text_input("Enter your password", type="password")
        signup = st.button('Sign Up')

        if signup:
            if input_username and password_input:
                # Check if the username already exists
                if input_username not in st.session_state.user_data:
                    # Hash the password to store it securely
                    hashed_password = bcrypt.hashpw(password_input.encode('utf-8'), bcrypt.gensalt())
                    
                    # Store the username and hashed password in session state
                    st.session_state.user_data[input_username] = hashed_password
                    st.success("Account created!! Please log in.")
                else:
                    st.write("Username already exists. Please choose a different one.")  # Handle duplicate username
            else:
                st.write("Please enter both a username and password.")  # Message for missing fields
