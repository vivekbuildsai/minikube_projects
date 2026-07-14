from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alice"},
    {"id": 3, "name": "David"}
]

@app.route("/")
def home():
    return "Employee Backend API is running!"

@app.route("/employees")
def get_employees():
    return jsonify(employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
