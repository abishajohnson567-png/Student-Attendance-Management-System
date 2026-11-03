import sqlite3
from flask import Blueprint, request, jsonify
api = Blueprint("api", __name__, url_prefix="/api")
FIELDS = "roll name email phone course section year gender dob blood guardian address photo".split()

def run(sql, args=(), fetch=False):
    with sqlite3.connect("attendance.db") as db:
        cur = db.execute(sql, args)
        return [dict(zip([c[0] for c in cur.description], r)) for r in cur.fetchall()] if fetch else cur.lastrowid

@api.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "GET":
        return jsonify(run("SELECT * FROM students", fetch=True))
    return jsonify(id=run(f"INSERT INTO students ({','.join(FIELDS)}) VALUES ({','.join('?' * len(FIELDS))})", [request.json.get(f, "") for f in FIELDS])), 201

@api.route("/students/<int:sid>", methods=["DELETE"])
def remove(sid):
    run("DELETE FROM students WHERE id=?", (sid,))
    run("DELETE FROM attendance WHERE student_id=?", (sid,))
    return jsonify(ok=True)

@api.route("/attendance", methods=["GET", "POST"])
def attendance():
    if request.method == "GET":
        return jsonify(run("SELECT * FROM attendance", fetch=True))
    for r in request.json:
        run("INSERT OR REPLACE INTO attendance VALUES (?,?,?,?)", (r["student_id"], r["date"], r["status"], r.get("remark", "")))
    return jsonify(ok=True), 201
