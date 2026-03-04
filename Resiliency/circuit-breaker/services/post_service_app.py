from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://root:root@localhost:27017/")
db = client["testdb"]

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/posts/{profile_id}")
def get_posts(profile_id: str):
    posts = list(db.posts.find(
        {"profile_id": profile_id},
        {"_id": 0}
    ))
    return posts