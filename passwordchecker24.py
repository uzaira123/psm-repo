import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength by Uzaira Waheed", page_icon="🌖", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
.main {text-align:center}
.stTextInput {width: 60% !important; margin: auto;}
.stButton button {width: 50%; background-color: #4CAF50; color: white; font-size:18px; }
.stButton button:hover { background-color: #45a049}
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check how secure it is. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase (A-Z) and lowercase (a-z) letters.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Input field
password = st.text_input("Enter your password:", type="password", help="Make sure your password is strong 🔐")

# Check button
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Display results
        if score == 4:
            st.success("✅ Strong Password - Your password is secure.")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider improving it.")
        else:
            st.error("❌ Weak Password - Follow the suggestions below to make it stronger.")

        # Show suggestions
        if feedback:
            with st.expander("🔍 Suggestions to Improve Your Password"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Please enter a password first.")
