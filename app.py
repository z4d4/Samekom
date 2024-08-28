from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "sanzo_2020"

@app.route("/samekom")
def index():
    flash("Pa Nama Kitak?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hai " + str(request.form['name_input']) + ", kamek sayang kitak k!")
    return render_template("index.html")