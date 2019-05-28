from flask import Flask
from flask import render_template
from flask import request
from recommender_awesome import get_recommendations

app = Flask(__name__)


@app.route('/')
def input_page():
    return render_template('index_awesome.html')

@app.route('/get_recommendations')
def output_page():
    movie1 = request.args.get('movie1', '-')  # reads parameter 'movie1' from the URL
    movie2 = request.args.get('movie2', '-')
    movie3 = request.args.get('movie3', '-')
    movies = [movie1, movie2, movie3]

    rating1 = request.args.get('rating1', '-')  # reads parameter 'movie1' from the URL
    rating2 = request.args.get('rating2', '-')
    rating3 = request.args.get('rating3', '-')
    ratings = [rating1, rating2, rating3]
    #
    # DO OR CALL YOUR CALCULATIONS Here
    #
    movies = get_recommendations(movies, ratings)

    return render_template('recommendations.html', movies=movies)
