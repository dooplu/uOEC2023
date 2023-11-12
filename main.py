from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/reports", methods=['GET', 'POST'])
@app.route("/reports/<link>+<username>")
def reports(link="", username=""):
    if request.method == 'GET':
        return render_template("reports.html", link=link, username=username)
    else: 
        formLink = request.form["link"]
        formUsername = request.form["username"]
        formDesc = request.form["desc"]
        print(formLink, formUsername, formDesc)
        return render_template("reports.html", link=link, username=username)

@app.route("/admin")
def admin():
    return "<h1> admin </h1>"