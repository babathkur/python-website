from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open("config.json", "r") as file:    
    paramss = json.load(file)["params"]

    
local_server = True
app = Flask(__name__)

if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = paramss['local_uri']
else:
     app.config["SQLALCHEMY_DATABASE_URI"] = paramss['prod_uri']


db = SQLAlchemy(app)
# db.init_app(app)

class Contact(db.Model):
   sno = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), nullable=False)
   email = db.Column(db.String(50), nullable=False)
   phone_num = db.Column(db.String(50), nullable=False)
   msg = db.Column(db.String(50), nullable=False)
   date = db.Column(db.String(50), nullable=True)
 

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def hello_worldss():
    return render_template("about.html")
@app.route("/contact",methods=["POST", "GET"])
def contact():
    if  request.method == "POST":
        name = request.form.get('name')
        emails = request.form.get('email_add')
        phone = request.form.get('phone')
        mssg = request.form.get('msg')
        entry = Contact(name = name, phone_num = phone, email = emails, msg = mssg,date = datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")
@app.route("/post")
def post():
    return render_template("post.html")
app.run(debug=True)
