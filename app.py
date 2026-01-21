from flask import Flask, request, jsonify
from recommender import recommend

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Movie Recommendation System is running"}

@app.route("/recommend", methods=["GET"])
def get_recommendation():
    movie = request.args.get("movie")
    if not movie:
        return jsonify({"error": "movie parameter is required"}), 400

    recommendations = recommend(movie)
    return jsonify({
        "input_movie": movie,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
