from flask import Flask, request, render_template, jsonify, make_response
# import json
# from flask_restful import Api, Resource
# from flask_cors import CORS

DEBUG = True

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist'
            )

app.config.from_object(__name__)

# cors = CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


# init_db(app)
# api = Api(app)
if __name__ == '__main__':
    app.run()