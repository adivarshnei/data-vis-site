from flask import Flask, render_template
from matplotlib import pyplot as plt

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return render_template("home.html")


@app.route("/about")
def about() -> str:
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
