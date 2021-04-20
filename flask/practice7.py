from flask import Flask, render_template
app = Flask(__name__)

@app.route('/class/<className>')
def hello_class(className):
    return render_template('class.html', name=className)

if __name__ == '__main__':
    app.run(debug=True)