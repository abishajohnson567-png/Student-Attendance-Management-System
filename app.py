from flask import Flask, render_template
from api import api, run, FIELDS

app = Flask(__name__)
app.register_blueprint(api)

# Create the two tables (only the first time)
run("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, " + ",".join(f + " TEXT" for f in FIELDS) + ")")
run("CREATE TABLE IF NOT EXISTS attendance (student_id INTEGER, date TEXT, status TEXT, remark TEXT, PRIMARY KEY (student_id, date))")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
