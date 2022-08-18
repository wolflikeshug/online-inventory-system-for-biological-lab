from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route('/rooms')
def rooms():
    return render_template("rooms.html")

@app.route('/freezers')
def freezers():
    return render_template("freezers.html")

@app.route('/samples')
def samples():
    return render_template("samples.html")

if __name__ == "__main__":
    app.run(debug=True)