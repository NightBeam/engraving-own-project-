from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template("main.html", title="engraving")

@app.errorhandler(404)
def showError(error):
    return "404"

if __name__ == "__main__":
    app.run(debug=True)