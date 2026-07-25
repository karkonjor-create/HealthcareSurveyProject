from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

# MongoDB connection
uri = "mongodb+srv://karkonjor_db_user:MyMongo2026@cluster0.tnjvfqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0YOUR_MONGODB_CONNECTION_STRING"

client = MongoClient(uri, server_api=ServerApi("1"))

db = client["healthcare_db"]
collection = db["survey"]

# Read all documents
data = list(collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

# Remove MongoDB ObjectId
if "_id" in df.columns:
    df = df.drop(columns=["_id"])

# Save CSV
df.to_csv("exports/survey_data.csv", index=False)

print("CSV exported successfully!")