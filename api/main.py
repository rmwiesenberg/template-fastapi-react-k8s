from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.model import MyModel

THIS_DIR = Path(__file__).absolute().parent
VERSION_FILE = THIS_DIR.parent / "VERSION"

ORIGINS = [
    "http://api.template.com",
    "https://api.template.com",
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()


@app.get("/")
async def root():
    return {"version": VERSION_FILE.read_text()}


@app.post("/echo")
async def echo(msg: MyModel):
    return msg


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
