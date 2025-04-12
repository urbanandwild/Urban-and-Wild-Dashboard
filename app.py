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

st.markdown("### Substrate & Amendments")
st.markdown("""
- [Coco Coir](https://amzn.to/3Gli05C)
- [Orchiata Classic](https://amzn.to/43LFQRZ)
- [Orchiata Precision](https://amzn.to/4icXjWQ)
- [Perlite 1/4"](https://amzn.to/3Gizuj3)
- [Perlite 3/8"](https://amzn.to/428pJg3)
- [Pumice](https://amzn.to/43QhaYA)
- [Tree Fern](https://amzn.to/3YwTqoL)
""")

st.markdown("### Cups & Pots")
st.markdown("""
- [3\" Pot](https://amzn.to/4ibSEEw)
- [Clear Seedling Cups](https://amzn.to/4lrj0VV)
- [Clear Self-Watering Pots 5\", 6\", 7\"](https://amzn.to/3RQiPpy)
- [Deli Containers](https://amzn.to/42HMisa)
- [Seed Tray with Dome](https://amzn.to/3EjNcSs)
- [Tray](https://amzn.to/4cuL8Dv)
""")

st.markdown("### Labeling")
st.markdown("""
- [Label Maker for Plant Tags](https://amzn.to/4cqHYRc)
- [Labels](https://amzn.to/42v7HUj)
""")

st.markdown("### Nutrients & Treatments")
st.markdown("""
- [CALiMAGic](https://amzn.to/3RgpoSf)
- [Fertilizer](https://amzn.to/4cuOvKH)
- [Humic Acid](https://amzn.to/44lgMBo)
- [Insecticidal Soap](https://amzn.to/42v7HUj)
- [Kleen Kelp](https://amzn.to/42rZXlH)
- [Mycorrhizal Fungi](https://amzn.to/3Rgkt3J)
- [Osmocote](https://amzn.to/3El8kYi)
- [pH Down](https://amzn.to/42v8MLR)
- [pH Meter](https://amzn.to/4j1TjK4)
- [pH Up](https://amzn.to/4loYjKB)
- [Super Thrive](https://amzn.to/42C6lXY)
- [SuperThrive ProTekt](https://amzn.to/4j1SIbi)
""")
