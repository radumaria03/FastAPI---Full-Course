from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()



@app.get('/')
def index():
    return {'data': 'blog list'}




@app.get("/blog")
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f"{limit} published blogs"}
    else:
        return {'data':f"{limit} unpublished blogs"}
    
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')  
def create_blog(request: Blog):
    return f"Blog created with title '{request.title}"
    


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}

#if __name__== "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=9000)