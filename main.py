from flask import *
import DatabaseManager

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
        report = {"link":formLink, "username":formUsername, "desc":formDesc}
        DatabaseManager.insertalldata(report)
        return render_template("reports.html", link=link, username=username)

@app.route("/admin")
def admin():
    reports = DatabaseManager.getdata()
    print(reports)
    return render_template("admin.html", reports=reports)