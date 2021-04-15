from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_ice():
    return '2016113519 유지훈<br>Hello ICE students!'

if __name__ == '__main__':
    app.run(debug=True)