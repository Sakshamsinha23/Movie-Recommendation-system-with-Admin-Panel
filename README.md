<img width="1920" height="1080" alt="Screenshot (88)" src="https://github.com/user-attachments/assets/65a52306-15e1-4ca6-bbde-c9a740109b0b" /># Movie-Recommendation-system-with-Admin-Panel
A smart movie recommender app built with Streamlit. Suggests top 5 similar movies using content-based filtering and cosine similarity. Includes a secure admin panel to add or delete movies. Posters are fetched from TMDB and OMDb, with fallback support for missing images
🎬 Movie Recommender System
A sleek and intelligent Movie Recommendation System built with Streamlit, powered by cosine similarity, with an integrated 🔐 Admin Panel to manage your movie database on the fly!

🚀 Features
✨ Smart Recommendations
Get 5 similar movies based on your selection using content-based filtering (cosine similarity).
<img width="1920" height="1080" alt="Screenshot (88)" src="https://github.com/user-attachments/assets/a53a1560-badb-44bd-be25-a76b39ba72dd" />

🖼 Dynamic Poster Fetching
Fetches posters using:

✅ TMDB API

✅ OMDb API (fallback)

🟥 Local Unavailable placeholder if both fail
Live link - https://movie-recommendation-system-f7d79db1d849.herokuapp.com/

🛡 Admin Panel with Login
<img width="1920" height="1080" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/d7ecf643-4604-4883-8c5c-bffdc58a1379" />

Add New Movies (with TMDB ID)

Delete Movies from list

Protected with username-password login

Hidden from normal users

<img width="1920" height="1080" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/6232a9ad-2983-443f-9982-e5ed0a6714e5" />



🌙 Modern Dark UI
Fully styled with a modern black theme and clean UI separation using tabs.
<img width="1920" height="1080" alt="Screenshot (83)" src="https://github.com/user-attachments/assets/3a92fd2e-d935-40a8-884b-bc6da86cc8e4" />

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
