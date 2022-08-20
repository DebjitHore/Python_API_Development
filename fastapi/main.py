from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

#Post pydantic model
class Post(BaseModel): 

    title: str
    content: str
    published : bool = True
    rating : Optional[int]= None

my_posts=[{"title": "title of post 1", "content": "content of post 1 ", "id":1}, {"title": "favorite foods", "content": "I like burgers", "id": 2}]

@app.get("/")   # This is an HTTP 'get' method with the path, this path decorator just referenes the path that we have to go in the URL in browser
async def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


# @app.post("/newPost")
# async def create_posts(payload: dict = Body(...)):
#     print (payload)
#     return {"new_post": f"title {payload['title']} content {payload['content']}"}
#title string and content string is mandatory in the data schema

@app.post("/newposts")
async def create_posts(newPost: Post): #referencing the post pydantic model, does the data validation and also verifies the schema of the data being sent from the front-end
    #print (newPost.rating)
    #print(newPost.dict()) #converting the pydantic object into a python dictionary
    post_dict= newPost.dict()
    post_dict['id']= randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data" : post_dict}

def find_post(id):
    for p in my_posts:
        if p['id']== id:
            return p

@app.get("/posts/{id}")
async def get_post(id: int):
    post= find_post(id)
    return {"post detail": post}
    