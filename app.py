
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/fruits"
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/user/add", methods=["POST"])
def add_user():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        print("Received form data:", first_name, last_name, email)  # Debug output


        new_user = Users(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_user)
        db.session.commit()
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
