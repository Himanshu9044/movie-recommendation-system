import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "movie_metadata.csv")
model_path = os.path.join(BASE_DIR, "models", "similarity.pkl")

movies = pd.read_csv(data_path, low_memory=False)

movies = movies[
    [
        "movie_title",
        "genres",
        "director_name",
        "actor_1_name",
        "actor_2_name",
        "actor_3_name",
        "plot_keywords",
        "imdb_score"
    ]
]

movies.fillna("", inplace=True)
movies["movie_title"] = movies["movie_title"].str.strip()

movies["tags"] = (
    movies["genres"] + " " +
    movies["director_name"] + " " +
    movies["actor_1_name"] + " " +
    movies["actor_2_name"] + " " +
    movies["actor_3_name"] + " " +
    movies["plot_keywords"]
)

tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
vectors = tfidf.fit_transform(movies["tags"])
similarity = cosine_similarity(vectors)

os.makedirs(os.path.dirname(model_path), exist_ok=True)
pickle.dump((movies, similarity), open(model_path, "wb"))

print("✅ Model trained & saved")
