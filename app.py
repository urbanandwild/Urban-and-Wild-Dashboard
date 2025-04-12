import streamlit as st
from PIL import Image
import os

logo_path = os.path.join("images", "logo.jpeg")
if os.path.exists(logo_path):
    st.image(logo_path, width=250)

st.markdown(
    "<h1 style='text-align: center; color: #333;'>Urban and Wild Dashboard</h1>",
    unsafe_allow_html=True
)

def check_password():
    def password_entered():
        if st.session_state["password"] == "urbanwild123":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter password to access internal dashboard", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter password to access internal dashboard", type="password", on_change=password_entered, key="password")
        st.error("Incorrect password")
        return False
    else:
        return True

if check_password():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", [
        "Home", "Parent Plants", "Upcoming Hybrids", "Seed Collection",
        "Inventory", "Care Tips", "Amazon Favorites"
    ])
    st.write(f"You selected: {page}")
    st.info("Content for each page will be loaded here. Expand this dashboard as needed.")
else:
    st.warning("This is a public view. Only public content will be shown.")
    st.subheader("Care Tips & Tricks")
    with open("data/tips.md", "r") as f:
        st.markdown(f.read())
    st.subheader("Amazon Favorites")
    st.markdown("- [FoxFarm Happy Frog Soil](https://www.amazon.com/)")
st.markdown("- [Maxsea Fertilizer](https://www.amazon.com/)")
