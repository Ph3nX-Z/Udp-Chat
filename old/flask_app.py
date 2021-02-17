from flask import Flask
import os
from flask import Flask, session, request, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = os.urandom(24)

liste = [("Ph3nX","un message","10:10"),("User2","un message qui est super interessant et captivant","10:11")]

@app.route('/', methods=['GET','POST'])                     
def index():
    return render_template("index.html", liste_message=liste)

app.run(port=80,threaded=True,host="0.0.0.0")