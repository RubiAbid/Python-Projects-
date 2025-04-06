import streamlit as st
import re
import random
import string

# Function to suggest a strong password
def suggest_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Common weak passwords
blacklist = ["password", "123456", "password123", "qwerty", "abc123", "admin", "letmein"]

# Strength Checker
def check_password_strength(password):
    score = 0
    suggestions = []

    # Blacklist check
    if password.lower() in blacklist:
        return 0, ["This password is too common. Choose something more unique."]

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Upper & lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one digit (0–9).")

    # Special char check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!@#$%^&*).")

    return score, suggestions

# App UI
st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Meter")

st.write("Check your password strength based on best security practices.")

password_input = st.text_input("Enter your password", type="password")

if password_input:
    score, feedback = check_password_strength(password_input)

    # Strength display
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Could be stronger.")
    else:
        st.error("❌ Weak Password - Needs improvement.")

    # Show feedback
    if feedback:
        st.markdown("**Suggestions:**")
        for tip in feedback:
            st.write(f"- {tip}")

    # Suggest strong password
    st.markdown("💡 Try a strong password suggestion:")
    st.code(suggest_strong_password(), language='text')

st.markdown("---------")
st.caption(" Built by **RUBI ABID**")
