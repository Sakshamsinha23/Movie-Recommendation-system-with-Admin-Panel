# Movie-Recommendation-system-with-Admin-Panel
A smart movie recommender app built with Streamlit. Suggests top 5 similar movies using content-based filtering and cosine similarity. Includes a secure admin panel to add or delete movies. Posters are fetched from TMDB and OMDb, with fallback support for missing images
🎬 Movie Recommender System
A sleek and intelligent Movie Recommendation System built with Streamlit, powered by cosine similarity, with an integrated 🔐 Admin Panel to manage your movie database on the fly!

🚀 Features
✨ Smart Recommendations
Get 5 similar movies based on your selection using content-based filtering (cosine similarity).

🖼 Dynamic Poster Fetching
Fetches posters using:

✅ TMDB API

✅ OMDb API (fallback)

🟥 Local Unavailable placeholder if both fail

🛡 Admin Panel with Login

Add New Movies (with TMDB ID)

Delete Movies from list

Protected with username-password login

Hidden from normal users

🌙 Modern Dark UI
Fully styled with a modern black theme and clean UI separation using tabs.

🧠 How It Works
Movie data is loaded from movie_dict.pkl

Cosine similarity is precomputed and loaded from similarity.pkl

On selecting a movie, similar movies are recommended using top 5 similarity scores.

Posters are fetched dynamically using APIs.

📦 Movie-Recommender-System
├── app.py                # 🎯 Main Streamlit application
├── movie_dict.pkl        # 🎬 Movie metadata (titles & TMDB IDs)
├── similarity.pkl        # 🧠 Precomputed cosine similarity matrix
├── static/
│   └── Unavailable.png   # 🚫 Placeholder poster if API fetch fails
├── README.md             # 📘 Project documentation (you're reading it!)




✅ Once logged in, you'll be able to:
Add
Delete
View

📥 Add a new movie by title + TMDB ID

🗑 Delete existing movies

🔓 Logout securely
