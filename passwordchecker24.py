import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength by Uzaira Waheed", page_icon="🌖", layout="centered")

# Custom CSS (Style settings)
st.markdown("""
<style>
.main {text-align:center}
.stTextInput {width: 60% !important; margin: auto;}
.stButton button {width: 50%; background-color: #4CAF50; color: white; font-size:18px; }
.stButton button:hover { background-color: #45a049}
</style>
""", unsafe_allow_html=True)

# Page title aur description
st.title("🔐 Password Strength Checker")
st.write("Neeche apna password likhein taake hum uski security check kar sakein. 🔍")

# Password check karne wali function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password kam az kam 8 characters ka hona chahiye.")

    # Upper aur lowercase letters check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password mein uppercase (A-Z) aur lowercase (a-z) letters hone chahiyein.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password mein kam az kam ek number (0-9) hona chahiye.")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password mein kam az kam ek special character (!@#$%^&*) hona chahiye.")

    return score, feedback

# Password input field
password = st.text_input("Apna password likhein:", type="password", help="Mazboot password banaiye 🔐")

# Button click hone par action
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Result show karna
        if score == 4:
            st.success("✅ Bohat acha password hai — strong aur secure.")
        elif score == 3:
            st.info("⚠️ Password theek hai — lekin behtar banaya ja sakta hai.")
        else:
            st.error("❌ Password kamzor hai — neeche diye gaye suggestions ko follow karein.")

        # Feedback display karna
        if feedback:
            with st.expander("🔍 Password behtar banane ke liye tips"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Pehle password likhein phir check karein.")














