from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route('/rooms')
def rooms():
    return render_template("rooms.html")

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/people')
def people():
    return render_template("people.html")

@app.route('/freezers')
def freezers():
    return render_template("freezers.html")

@app.route('/samples')
def samples():
    return render_template("samples.html")

# Temporary page to show Allison team forms/may use later
@app.route('/mockup')
def mockup():
    return render_template("mockup.html")

if __name__ == "__main__":
    app.run(debug=True)