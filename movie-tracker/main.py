import streamlit as st
import requests

# Set wide layout and custom page title
st.set_page_config(page_title="Anime Search Engine", layout="wide")

# Stylish Header
st.markdown(
    """
    <h1 style='text-align: center; color: #FF4B4B; font-family: "Trebuchet MS", sans-serif;'>
        🔥 Anime Explorer 🔍
    </h1>
    <p style='text-align: center; color: #AAAAAA;'>Search your favorite anime and get details in style!</p>
    <hr>
    """,
    unsafe_allow_html=True
)

# Search Input
query = st.text_input("Enter Anime Name")

if st.button("Search") and query:
    url = f"https://api.jikan.moe/v4/anime?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data["data"]

        if results:
            for anime in results:
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image(anime["images"]["jpg"]["image_url"], use_container_width=True)

                with col2:
                    st.markdown(f"### <span style='color:#FF4B4B'>{anime['title']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<b>🌟 Score:</b> <span style='color:#FFD700'>{anime['score']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<b>📺 Episodes:</b> {anime['episodes']} | <b>⏳ Status:</b> {anime['status']}", unsafe_allow_html=True)
                    synopsis = anime.get('synopsis')
                    if synopsis:
                        st.markdown(f"<p style='color:#DDDDDD;'>{synopsis[:300]}...</p>", unsafe_allow_html=True)
                    else:
                        st.markdown("<p style='color:#888888;'>No synopsis available.</p>", unsafe_allow_html=True)

                st.markdown("---")
        else:
            st.warning("No anime found! Try another name.")
    else:
        st.error("Failed to fetch anime data from the API.")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 13px; color: #999999;'>Made with ❤️ by Vikram using Streamlit and Jikan API</p>
    """,
    unsafe_allow_html=True
)
