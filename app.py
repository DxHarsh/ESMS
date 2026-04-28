from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db_2024_27"
)

@app.route("/students")
def students():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CSE")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "roll_no": row[0],
            "name": row[1],
            "sem": row[2]
        })

    cursor.close()
    db.close()
    return jsonify(data)
@app.route("/test")
def test():
    
    return jsonify(['Working'])
app.run(debug=True)

