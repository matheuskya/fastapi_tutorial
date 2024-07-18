from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


# schema usando pydantic, autentica o formato de dados passado para os endpoints
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{
    "title": "title of post 1",
    "content": "content of post 1",
    "id": "4"
}, {
    "title": "title of post 2",
    "content": "content of post 2",
    "id": "4"
}]


@app.get("/")
def root():
    return {"message": "hello world"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_post(post: Post):
    print(post.published)
    return {"data": "new post"}
