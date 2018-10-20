from flask import Flask, render_template, request
from data import Faculties
app = Flask(__name__)

getFaculties = Faculties()

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/faculties")
def senddata():
    return render_template('faculties.html',sendFacul=getFaculties)

@app.route("/about")
def about():
    return '<h1>About Works</h1>'

@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getname = request.form['name']
        getemail = request.form['email']
        return render_template('contact.html',name=getname,email=getemail)

if(__name__=='__main__'):
    app.run(debug=True)