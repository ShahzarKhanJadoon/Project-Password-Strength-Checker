#imports
import re
import streamlit as st


st.set_page_config(page_title="Password Strength Checker", layout="centered")

st.title("Password Strength Checker")
st.subheader("Check the strength of your password")
st.write("Enter a password to check its strength")


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
  
    if re.search(r'[A-Z]', password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters")

    if re.search(r'[\d]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number")
    
    if re.search(r'[!@#$%^&*()_+{}|:"<>?~-]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character")

    
    if score == 4:
        st.success("Password is strong")
    elif score == 3:
        st.warning("Password is medium ")
    else:
        st.error("Password is weak")
    

    if feedback:
        with st.expander("Improve your password"):
            for item in feedback:
                st.write(f"- {item}")

password = st.text_input("Enter your password", type="password", help="Password should be at least 8 characters long, contain both uppercase and lowercase letters, at least one number, and one special character")


if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("Please enter a password")




    

                                 