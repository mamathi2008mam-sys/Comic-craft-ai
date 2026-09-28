from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.schemas import StoryRequest
from backend.story_generator import generate_story


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(title="ComicCraft AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND_DIR)),
    name="static"
)


@app.get("/")
def home():
    return FileResponse(
        str(FRONTEND_DIR / "index.html")
    )


@app.get("/health")
def health():
    return {
        "status": "success",
        "message": "ComicCraft API is running!"
    }


@app.post("/generate")
def generate(request: StoryRequest):

    comic = generate_story(
        request.story_prompt,
        request.character_name,
        request.setting,
        request.tone,
        request.art_style
    )

    return {
        "success": True,
        "title": comic["title"],
        "panels": comic["panels"]
    }
