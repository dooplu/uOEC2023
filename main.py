from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World ITS IDIR!</p>"

@app.route("/reports", methods=['GET', 'POST'])
@app.route("/reports/<link>+<username>")
def reports(link="", username=""):
    if request.method == 'GET':
        return render_template("reports.html", link=link, username=username)
    else: 
        pass

@app.route("/admin")
def admin():
    return "<h1> admin </h1>"