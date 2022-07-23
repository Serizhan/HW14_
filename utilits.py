import sqlite3
import json


def open_file_db(sql):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = sql
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return executed_query


def json_open():
    json_file = json.dumps(creat_dist(all_movie()))
    return json_file


def creat_dist(data):
    new_list = []
    for row in data:
        next_list = {"title": row[0], "country": row[1], "release_year": row[2], "genre": row[3], "description": row[4]}
        new_list.append(next_list)
    return new_list


def release_year(first, second):
    result = f"""SELECT title, release_year 
                       FROM netflix
                       WHERE release_year BETWEEN {first} AND {second}      
                       LIMIT 100       
                       """
    return open_file_db(result)


def find_movie(movie):
    result = f"""SELECT title, country, release_year, listed_in, description  
                       FROM netflix
                       WHERE title LIKE '%{movie}%'
                       ORDER BY release_year DESC               
                       """
    return creat_dist(open_file_db(result))


def all_movie():
    result = f"""SELECT title, country, release_year, listed_in, description  
                FROM netflix              
                """
    return open_file_db(result)


def rating_movie(list_):
    result = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating !='' AND rating IN ({list_})
            GROUP BY title, rating, description
    """
    return open_file_db(result)


def movie_genre(genre):
    result = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
    """
    return open_file_db(result)


def movie_by_two_cast(cast_1, cast_2):
    result = f"""
            SELECT COUNT(*), "cast"
            FROM netflix
            WHERE "cast" LIKE '%{cast_1}%' 
            AND "cast" LIKE '%{cast_2}%'

    """
    return open_file_db(result)


def movie_by_type_year_genre(type, year, genre):
    result = f"""
            SELECT title, description
            FROM netflix
            WHERE type = '{type}' 
            AND release_year = {year} 
            AND listed_in LIKE '%{genre}%'

    """
    json_file = json.dumps(open_file_db(result))
    return json_file


print(movie_by_type_year_genre('Movie', 2014, 'Horror'))
