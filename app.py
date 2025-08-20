import streamlit as st
import joblib
import pandas as pd
import difflib

# Load saved files
vectorizer = joblib.load("vectorizer.pkl")
similarity = joblib.load("similarity.pkl")
movies_data = pd.read_pickle("movies_data.pkl")

# All movie titles
list_of_all_titles = movies_data['title'].dropna().unique().tolist()

# --- Custom CSS (Cyan + Purple theme) ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #f5f5f5;
        font-family: 'Poppins', sans-serif;
    }
    .title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
        text-shadow: 2px 2px 20px rgba(79, 172, 254, 0.7);
        margin-bottom: 30px;
        animation: fadeInDown 1s ease-in-out;
    }
    /* Search box */
    div[data-baseweb="select"] > div {
        background-color: #1c1c1c !important;
        border-radius: 8px !important;
        border: 2px solid #00f2fe !important;
        color: white !important;
        box-shadow: 0px 0px 12px rgba(79, 172, 254, 0.6);
    }
    /* Dropdown menu */
    ul {
        background-color: #1c1c1c !important;
        border-radius: 6px !important;
    }
    li:hover {
        background: linear-gradient(90deg, #00f2fe, #4facfe) !important;
        color: black !important;
    }
    /* Recommendations */
    .recommendation {
        background: rgba(255, 255, 255, 0.05);
        padding: 12px 18px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 18px;
        transition: transform 0.3s, box-shadow 0.3s;
        box-shadow: 0px 0px 6px rgba(0,0,0,0.5);
        cursor: pointer;
    }
    .recommendation:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(79, 172, 254, 0.8);
        background: rgba(79, 172, 254, 0.1);
    }
    /* Animations */
    @keyframes fadeInDown {
        0% {opacity: 0; transform: translateY(-20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    /* Footer */
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 15px;
        font-weight: 600;
        color: #f5f5f5;
        text-shadow: 1px 1px 5px #000;
        letter-spacing: 1px;
    }
    .footer span {
        background: -webkit-linear-gradient(45deg, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# --- Recommendation function ---
def recommend_movie(movie_name):
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    if not find_close_match:
        return ["No close match found. Please try again."]

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match].index.values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i, movie in enumerate(sorted_similar_movies[1:21], start=1):  # top 20
        index = movie[0]
        title_from_index = movies_data.iloc[index]['title']
        recommended_movies.append(title_from_index)
    return recommended_movies

# --- UI ---
st.markdown("<h1 class='title'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Autocomplete dropdown
typed_movie = st.selectbox(
    "Search for a movie:",
    options=list_of_all_titles,
    index=None,
    placeholder="Type to search..."
)

# Instant recommendations
if typed_movie:
    recommendations = recommend_movie(typed_movie)
    st.write(f"### 🎥 Recommended Movies for **{typed_movie}**:")
    for i, title in enumerate(recommendations, start=1):
        st.markdown(f"<div class='recommendation'>{i}. {title}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>🚀 Developed & Deployed by <span>Sagar Kallimani</span></div>", unsafe_allow_html=True)
