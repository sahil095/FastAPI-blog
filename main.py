from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html", 
        {
            "request": request, 
            "posts": posts, 
            "title": "Home Page"
        }
    )


@app.get("/posts/{post_id}", include_in_schema=False)
def get_post(request:Request, post_id:int):
    for post in posts:
        if post.get("id") == post_id:
            title = post['title']
            return templates.TemplateResponse(
                "post.html", 
                {
                    "request": request, 
                    "post": post, 
                    "title": title
                }
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!")



@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!")