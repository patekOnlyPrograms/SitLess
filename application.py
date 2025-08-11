import threading
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

import asyncio

from timer import convertMinutesToSeconds, countdown

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///timerDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
from models import TimerLog

with app.app_context():
    db.create_all()
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        get_duration = request.form.get("duration")
        if get_duration:
            seconds=convertMinutesToSeconds(get_duration)
            thread = threading.Thread(target=start_async_timer, args=(seconds,))
            thread.start()
    return render_template('index.html')

def start_async_timer(seconds):
    asyncio.run(countdown(seconds))

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template('signup.html')

@app.route("/stretches", methods=["GET"])
def stretches():
    return render_template('stretches.html')


if __name__ == "__main__":
    app.run()
