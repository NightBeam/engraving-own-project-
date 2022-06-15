from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def mainPage():
    if(request.args.get('type')):
        print('good job')
    return render_template("main.html", title="engraving")

@app.errorhandler(404)
def showError(error):
    return "404"

if __name__ == "__main__":
    app.run(debug=True)