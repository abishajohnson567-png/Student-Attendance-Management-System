# Rollcall — Student Attendance Management System

## Run
    pip install flask
    python app.py
Open http://127.0.0.1:5000  (the database file attendance.db is created automatically)

## Structure
    app.py                 Flask website (16 lines)
    api.py                 REST API + SQLite (29 lines)
    templates/index.html   The whole interface
    static/css/style.css   All styling

## API
    GET/POST   /api/students
    DELETE     /api/students/<id>
    GET/POST   /api/attendance
