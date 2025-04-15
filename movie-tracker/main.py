import streamlit as st


st.title("Movie Tracker")

menue = ["add movie", "view movie"]

choices = st.sidebar.selectbox("view movies", menue)

if choices == "add movie":
    st.subheader("Add your fvt movie")
elif choices == "view movie":
    st.subheader("you have viewed")



