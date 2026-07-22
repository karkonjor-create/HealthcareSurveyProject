from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)

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