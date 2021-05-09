from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response, request, redirect, jsonify

app = Flask(__name__)


connection = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="devcitiesData"
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



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)