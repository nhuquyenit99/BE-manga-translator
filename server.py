from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import translate_manga

class TranslateInfo(BaseModel):
    url: str
    file_name: str
    page: int
    lang: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return 'Welcome!'

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}



@app.post('/translate/')
async def translate(data: TranslateInfo):
    return translate_manga(image_path=data.url, file_name=data.file_name, page=data.page, lang=data.lang)
