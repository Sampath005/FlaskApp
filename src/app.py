from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/sam')
def hello_sam():
    return 'Hello, Sampath!'

@app.route('/sathiya')
def hello_sathya():
    return 'Hello, Sathiya!'

@app.route('/sathiya')
def hello_saravanan():
    return 'Hello, Saravanan!'
    
if __name__ == '__main__':
    app.run(debug=True, port=8085)
