from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/sam')
def hello():
    return 'Hello, Sam!'



if __name__ == '__main__':
    app.run(debug=True)
