from flask import Flask, render_template

DEBUG = True

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist'
            )
app.config.from_object(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()