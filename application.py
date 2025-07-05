import threading

from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
import asyncio

from timer import convertMinutesToSeconds, countdown

app = Flask(__name__)
bootstrap = Bootstrap5(app)
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


if __name__ == "__main__":
    app.run()
