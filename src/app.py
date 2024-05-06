from flask import Flask, request, jsonify
from Recommendation import load_data, recommend_movies

app = Flask(__name__)

# Load data
movies_with_ratings = load_data()

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json(force=True)
    genres = data.get('genres', [])
    min_rating = float(data.get('min_rating', 3.5))

    recommended = recommend_movies(movies_with_ratings, genres, min_rating=min_rating)

    if recommended.empty:
        return jsonify({'message': 'No recommendations found.'}), 404
    else:
        return jsonify(recommended[['title', 'average_rating', 'rating_count', 'genres']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)