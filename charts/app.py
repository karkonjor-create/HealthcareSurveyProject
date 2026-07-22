from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return """
    <h1>Healthcare Income & Spending Survey</h1>
    <p>Welcome to our Healthcare Survey System.</p>
    <p>This application collects participant information for income and spending analysis.</p>
    """

# Run the application
if __name__ == "__main__":
    app.run(debug=True)