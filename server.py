from fastapi import FastAPI
from pydantic import BaseModel

class ImageInfo(BaseModel):
    url: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}



@app.post('/translate/')
async def translate_manga(image: ImageInfo):
    return { "image_url": image.url }
