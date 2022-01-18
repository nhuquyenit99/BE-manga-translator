from fastapi import FastAPI
from pydantic import BaseModel
from main import translate_manga

class ImageInfo(BaseModel):
    url: str
    file_name: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}



@app.post('/translate/')
async def translate(image: ImageInfo):
    return translate_manga(image_path=image.url, file_name=image.file_name)
