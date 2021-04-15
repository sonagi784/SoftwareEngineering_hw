from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_dongguk():
    return '2016113519 유지훈<br/>Hello Dongguk University Students!'

if __name__ == '__main__':
    app.run()