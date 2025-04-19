import re
import streamlit as st
# page styling
st.set_page_config(page_title="Password S trenght by Uzaira Waheed",page_icon="🌖", layout="centered")
# custom css
st.markdown("""
<style>
.main {text-align:center}
.stTextInput {width: 60% !important; margin; auto;}
.stButton button {width: 50%; background-color #4CAF50; color: white; font-size:18px; }
.stButton button:hover { background-color: #45a049}
 </style>
""" ,unsafe_allow_html=True)

#page title and description
def check_Password_strenght(Password):
    score = 0
    feedback = []

 if len(Password) >=8:  
    score += 1 #increased score by 1

else :
    feedback.append("❌ Password should be **atleast 8 character long**.")

if re.search(r"[A-Z]", Password) and re.search(r"[a-z]",Password):
    score += 1

else :
    feedback.append("❌ Password should Include **uppercase (A-Z) lowercase (a-z) letters**.")

if re.search(r"\d",Password):
    score += 1 

else :
    feedback.append("❌ Password should Include ** atleast one number (0-9) **.")

#special characters
if re.search(r"[!@#$%^&*]")
    score += 1 

else :
    feedback.append("❌ Include **atleast one special character (!@#$%^&*)**.")

#display password strenght results
if score ==4:
    st.ssucess("✅ **Storng Password** - Your Password is secure.")

elif score ==3
    st.info("⚠️ **Moderate Password** -Consider imporving secuirty by adding more feacture")


else :
    feedback.append("❌ Include **Week Password** - Follow the suggestion below the strenght it.")

#feedback
if feedback:
    with st.expander("🔍**Improved your Password**"):
for item in feedback:
    st.writen(item)
Password st.text_input("Enter your Password:",type="Password", help="Ensure your Passwordis strong🔐")

#button working
if st.button("Check Strength"):
    if password:
        check_Password_strenght(Password)
st.warning("⚠️Please Enter the Password first!") #show warning if psassword empty













