from flask import Flask, jsonify
from utilits import json_open, find_movie, release_year, rating_movie, movie_genre

app = Flask(__name__)


@app.route('/')
def movie_all():
    data = json_open()
    return jsonify(data)


@app.route('/movie/<title>')
def search_movie(title):
    result = find_movie(title)
    return jsonify(result)


@app.route('/movie/<first_year>/to/<second_year>')
def search_movie_years(first_year, second_year):
    result = release_year(first_year, second_year)
    return jsonify(result)


@app.route('/rating/<rating>')
def movie_by_rating(rating):
    if rating == "children":
        choose = "'G'"
    elif rating == "family":
        choose = "'G', 'PG', 'PG-13'"
    elif rating == "adult":
        choose = "'R', 'NC-17'"
    result = rating_movie(str(choose))
    return jsonify(result)


@app.route('/genre/<genre>')
def movie_by_genre(genre):
    result = movie_genre(genre)
    return jsonify(result)


app.run()
