from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response, request, redirect, jsonify

app = Flask(__name__)


connection = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="movieDB"
)
cursor = connection.cursor(dictionary=True)



@app.route('/')
def index():

    return "Robert Deniro Movies API"


@app.route('/all')
def all():

    cursor.execute('SELECT * FROM movies')
    result = cursor.fetchall()
    
    return jsonify(result)


@app.route('/movie/<int:id>')
def movie(id):
    cursor.execute('SELECT * FROM movies WHERE id = ' + str(id))
    result = cursor.fetchall()
    
    if not result:
        return jsonify({"Error":"Movie Not Found"})

    return jsonify(result[0])


@app.route("/create/", methods=["POST"])
def create():
    data = request.json
    Title = data["Title"]
    ReleaseYear = data["ReleaseYear"]
    Score = data["Score"]


    query =f"INSERT INTO movies(Title, ReleaseYear, Score) VALUE (\'{Title}\', {ReleaseYear}, {Score})"

    cursor.execute(query)
    connection.commit()

    return jsonify(query)

@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    Title = data["Title"]
    ReleaseYear = data["ReleaseYear"]
    Score = data["Score"]
    
    query = f"UPDATE movies SET Title = \'{Title}\', ReleaseYear = {ReleaseYear} ,Score = {Score} WHERE id = {id}"

    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()



    cursor.execute('SELECT * FROM movies WHERE id = ' + str(id))
    result = cursor.fetchall()

    return jsonify(result)

@app.route("/delete/<int:id>", methods=["DELETE"])
def deleteMovie(id):
    cursor.execute('DELETE FROM movies WHERE id = ' + str(id))
    connection.commit()


    return str(id) + " was deleted from DB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)