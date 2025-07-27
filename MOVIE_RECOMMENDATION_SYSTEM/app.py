import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ✅ API Keys
tmdb_api_key = '8265bd1679663a7ea12ac168da84d2e8'
omdb_api_key = 'dfad5699ccf8ec0f67360e33ec495883'

# ✅ Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "bitconnect@123"

# ✅ Track login state
if 'admin_logged_in' not in st.session_state:
    st.session_state['admin_logged_in'] = False

# ✅ TMDB poster fetch
def fetch_poster_tmdb(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=en-US"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as e:
        print(f"[TMDB] Error for movie_id {movie_id}: {e}")
    return None

# ✅ OMDb fallback
def fetch_poster_omdb(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}"
        response = requests.get(url)
        data = response.json()
        if data.get("Response") == "True" and data.get("Poster") != "N/A":
            return data["Poster"]
        else:
            print(f"[OMDb] No poster for '{title}'")
    except Exception as e:
        print(f"[OMDb] Error: {e}")
    return None

# ✅ Final fallback
def fetch_best_poster(movie_id, title):
    poster = fetch_poster_tmdb(movie_id)
    if poster:
        return poster
    poster = fetch_poster_omdb(title)
    if poster:
        return poster
    return os.path.join("static", "Unavailable.png")

# ✅ Recommend logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]]['title']
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_titles.append(title)
        recommended_posters.append(fetch_best_poster(movie_id, title))

    return recommended_titles, recommended_posters

# ✅ Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ✅ Streamlit Layout
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

# Tabs
tab1, tab2 = st.tabs(["🔍 Recommender", "🛠 Admin Panel 🔐"])

# === TAB 1: RECOMMENDER ===
with tab1:
    selected_movie_name = st.selectbox(
        'Select a movie to get recommendations:',
        movies['title'].values
    )

    if st.button('Recommend'):
        with st.spinner("🔍 Fetching recommendations..."):
            names, posters = recommend(selected_movie_name)

        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.text(names[idx])
                st.image(posters[idx])

# === TAB 2: ADMIN PANEL ===
with tab2:
    if not st.session_state['admin_logged_in']:
        st.subheader("🔐 Admin Login Required")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.success("✅ Logged in as Admin!")
                st.session_state['admin_logged_in'] = True
            else:
                st.error("❌ Invalid credentials.")
    else:
        st.subheader("📋 Current Movie List")
        st.dataframe(movies[['title', 'movie_id']].sort_values(by='title').reset_index(drop=True))

        st.markdown("---")
        st.subheader("➕ Add New Movie")

        new_title = st.text_input("Movie Title")
        new_id = st.text_input("TMDB Movie ID (numeric)")

        if st.button("Add Movie"):
            if new_title and new_id:
                try:
                    new_entry = pd.DataFrame({'title': [new_title], 'movie_id': [int(new_id)]})
                    movies = pd.concat([movies, new_entry], ignore_index=True)
                    pickle.dump(movies.to_dict(), open('movie_dict.pkl', 'wb'))
                    st.success(f"✅ '{new_title}' added successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to add movie: {e}")
            else:
                st.warning("⚠ Please enter both title and ID.")

        st.markdown("---")
        st.subheader("❌ Delete Movie")

        if not movies.empty:
            del_title = st.selectbox("Select a movie to delete", movies['title'].values)

            if st.button("Delete Movie"):
                movies = movies[movies['title'] != del_title]
                pickle.dump(movies.to_dict(), open('movie_dict.pkl', 'wb'))
                st.success(f"🗑 '{del_title}' deleted successfully!")

        st.markdown("---")
        if st.button("Logout 🔓"):
            st.session_state['admin_logged_in'] = False
            st.success("👋 Logged out successfully.")