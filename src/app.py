from flask import Flask
import pandas as pd

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

@app.route('/saravanan')
def hello_saravanan():
    return 'Hello, Saravanan!'

@app.route('/sakthivel')
def hello_sakthivel():
    return 'Hello, sakthivel! '

@app.route('/pandas')
def pandas():
    return pd.Series(range(1, 11))
    
if __name__ == '__main__':
    app.run(debug=True, port=8085)
