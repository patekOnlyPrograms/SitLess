from flask_bootstrap import Bootstrap5
from flask import Flask, render_template




app = Flask(__name__)
bootstrap = Bootstrap5(app)
@app.route("/")
@app.route("/index")
def main():
    return render_template('index.html')




if __name__ == "__main__":
    app.run()
