# from flask import Flask, request, jsonify
# from recommender import recommend

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return {"message": "Movie Recommendation System is running"}

# @app.route("/recommend", methods=["GET"])
# def get_recommendation():
#     movie = request.args.get("movie")
#     if not movie:
#         return jsonify({"error": "movie parameter is required"}), 400

#     recommendations = recommend(movie)
#     return jsonify({
#         "input_movie": movie,
#         "recommendations": recommendations
#     })

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

import streamlit as st
from recommender import recommend
import pickle
import os

st.set_page_config(page_title="Netflix Movie Recommender", layout="wide")

st.title("🎬 Netflix-Style Movie Recommendation System")
st.write("Select a movie and get similar recommendations")

# Load movies list from model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models", "similarity.pkl")

movies, similarity = pickle.load(open(model_path, "rb"))
movie_list = sorted(movies["movie_title"].str.strip().unique())

selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    recs = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recs, 1):
        st.write(f"{i}. {movie}")

