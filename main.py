from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Sahil Sehgal",
        "title": "Fast API is Good",
        "content": "Backend framework to create API Endpoints",
        "date_posted": "March 06, 2026"
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is good",
        "content": "Python for Backend, API, ML, and everything",
        "date_posted": "March 05, 2026"
    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/post", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def home():
    return posts
