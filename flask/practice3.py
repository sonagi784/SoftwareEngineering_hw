from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_ice2(name):
    return '2016113519 유지훈<br>Hello ICE student %s' % name

if __name__ == '__main__':
    app.run(debug=True)