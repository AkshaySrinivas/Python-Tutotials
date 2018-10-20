from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello Flask!'

@app.route("/about")
def about():
    return '<h1>About Works</h1>'

if(__name__=='__main__'):
    app.run(debug='true')