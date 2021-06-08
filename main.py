from diary import app

if __name__ == '__main__':
    app.debug = True
    #db.create_all()
    app.secret_key = "123"
    app.run(debug=True)