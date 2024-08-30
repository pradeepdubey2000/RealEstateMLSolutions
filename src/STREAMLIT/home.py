import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏡",
)

st.write("# Welcome to the Gurgaon Real Estate Analytics App! 🏡")

st.sidebar.title("Navigation")
options = ["Home", "Price Predictor", "Analysis App", "Recommend Apartments"]
selection = st.sidebar.radio("Go to", options)

if selection == "Home":
    st.write("This is the home page. Use the sidebar to navigate to other pages.")

elif selection == "Price Predictor":
    st.write("## Price Predictor")
    # Use Streamlit's `include` to load the `Price Predictor` page
    st.write("Loading Price Predictor...")
    with st.spinner('Loading page...'):
        st.experimental_rerun()  # To dynamically load the page

elif selection == "Analysis App":
    st.write("## Analysis App")
    # Use Streamlit's `include` to load the `Analysis App` page
    st.write("Loading Analysis App...")
    with st.spinner('Loading page...'):
        st.experimental_rerun()  # To dynamically load the page

elif selection == "Recommend Apartments":
    st.write("## Recommend Apartments")
    # Use Streamlit's `include` to load the `Recommend Apartments` page
    st.write("Loading Recommend Apartments...")
    with st.spinner('Loading page...'):
        st.experimental_rerun()  # To dynamically load the page
