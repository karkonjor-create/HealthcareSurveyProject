from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from user import User
app = Flask(__name__)   # <-- ADD THIS LINE
uri = "mongodb+srv://karkonjor_db_user:MyMongo2026@cluster0.tnjvfqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))
from pymongo.server_api import ServerApi

client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print(e)
db = client["healthcare_db"]
collection = db["survey"]

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Process the submitted survey
@app.route("/submit", methods=["POST"])
def submit():

    age = request.form.get("age")
    gender = request.form.get("gender")
    income = request.form.get("income")

    user = User(age, gender, income)

    print(user.to_dict())
    collection.insert_one(user.to_dict())
    return f"""
    <h2>Survey Submitted Successfully!</h2>

    <p><strong>Age:</strong> {age}</p>
    <p><strong>Gender:</strong> {gender}</p>
    <p><strong>Income:</strong> {income}</p>

    <br>
    <a href="/">Return to Survey</a>
    """


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
@app.route("/submit", methods=["POST"])
def submit():
    age = request.form.get("age")
    gender = request.form.get("gender")
    income = request.form.get("income")

    user = User(age, gender, income)
    
    collection.insert_one(user.to_dict())

    print(user.to_dict())

    return f"""
    <h2>Survey Submitted Successfully!</h2>

    <p><strong>Age:</strong> {age}</p>
    <p><strong>Gendfrom flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from user import User
er:</strong> {gender}</p>
    <p><strong>Income:</strong> {income}</p>

    <br>
    <a href="/">Return to Survey</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)