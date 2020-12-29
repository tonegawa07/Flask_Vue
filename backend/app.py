from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import mysql.connector
# import json
# from flask_restful import Api, Resource

# DEBUG = True

app = Flask(__name__)
            # static_folder='../frontend/dist/static',
            # template_folder='../frontend/dist'
            # )

# app.config.from_object(__name__)

cors = CORS(app)

conn = mysql.connector.connect(
    host = 'db',
    port = 3306,
    user = os.environ.get('MYSQL_USER'),
    password = os.environ.get('MYSQL_PASSWORD'),
    database = os.environ.get('MYSQL_DATABASE'),
)

@app.route('/', methods=['GET'])
# @app.route('/<path:path>')
# def index(path):
    # return render_template('index.html')

def select_all():
    conn.ping(reconnect=True)
    cur = conn.cursor()
    cur.execute('SELECT * FROM COMMENT')
    sql_result = cur.fetchall()

    result = []

    for item in sql_result:
        index = item[0]
        title = item[1]
        category = item[2]
        content = item[3]

        result.append(dict(index=index, title=title, category=category, content=content))

    return jsonify(results=result)

# init_db(app)
# api = Api(app)
if __name__ == '__main__':
    app.run()