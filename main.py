from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

listOfWeapons = ['AK','M4','DEAGLE','SWD']

@app.route('/main/<wp>')
def mainPage(wp):
    return render_template("main.html", title="engraving", item=wp)

@app.route('/')
def WeaponsChangerPage():
    return render_template("weaponsChanger.html", listOfWeapons=listOfWeapons)

@app.errorhandler(404)
def showError(error):
    return "404"



if __name__ == "__main__":
    app.run(debug=True)