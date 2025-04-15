import streamlit as st


st.title("Movie Tracker")

menue = ["Add movie", "View movies"]

choices = st.sidebar.selectbox("View movies", menue)

if choices == "Add movie":
    st.subheader("Add your fvt movie")
elif choices == "View movies":
    st.subheader("movies you have viewed")


movie_list = []

if choices == "Add movie":
    title = st.text_input("Enter your title")
    genr = st.text_input("Enter the genr")
    status = st.selectbox("status",["watched ", "plan to watch", "donot want to watch"])
    
    if st.button("Add movie"):
        movie_list.append({"title": title, "genr": genr , "status":status})
        st.succes("")



