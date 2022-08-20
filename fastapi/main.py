from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

#Post pydantic model
class Post(BaseModel): 
    title: str
    content: str
    published : bool = True
    rating : Optional[int]= None


@app.get("/")   # This is an HTTP 'get' method with the path, this path decorator just referenes the path that we have to go in the URL in browser
async def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


# @app.post("/newPost")
# async def create_posts(payload: dict = Body(...)):
#     print (payload)
#     return {"new_post": f"title {payload['title']} content {payload['content']}"}
#title string and content string is mandatory in the data schema

@app.post("/newPost")
async def create_posts(newPost: Post): #referencing the post pydantic model, does the data validation and also verifies the schema of the data being sent from the front-end
    print (newPost.rating)
    print(newPost.dict()) #converting the pydantic object into a python dictionary
    return {"data" :"new_post"}


