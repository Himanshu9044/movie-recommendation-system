import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models", "similarity.pkl")

movies, similarity = pickle.load(open(model_path, "rb"))

def recommend(movie_title, top_n=10):
    movie_title = movie_title.strip()

    if movie_title not in movies["movie_title"].values:
        return []

    idx = movies[movies["movie_title"] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:30]

    final = sorted(
        scores,
        key=lambda x: movies.iloc[x[0]].imdb_score,
        reverse=True
    )[:top_n]

    return [movies.iloc[i[0]].movie_title for i in final]
