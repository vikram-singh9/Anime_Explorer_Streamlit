import streamlit as st
import requests

st.set_page_config(page_title="Movie Finder 🎬", layout="wide")
st.markdown("<h1 style='text-align: center; color: orange;'>Movie Finder 🎬</h1>", unsafe_allow_html=True)

api_key = "YOUR_API_KEY"  # Replace this with your real TMDB API Key
query = st.text_input("🔍 Search Movie")

if st.button("Search") and query:
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data["results"]

        if results:
            for movie in results:
                col1, col2 = st.columns([1, 3])
                with col1:
                    if movie.get("poster_path"):
                        img_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                        st.image(img_url, use_column_width=True)
                with col2:
                    st.subheader(f"🎬 {movie['title']}")
                    st.write(f"⭐ Rating: {movie['vote_average']}")
                    st.write(f"🗓️ Release Date: {movie['release_date']}")
                    st.write(f"📖 Overview:\n{movie['overview'][:300]}...")
                st.markdown("---")
        else:
            st.warning("No movies found.")
    else:
        st.error("Failed to fetch data from TMDB API.")
