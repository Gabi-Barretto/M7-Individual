from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Monte a pasta de arquivos estáticos
app.mount("/static", StaticFiles(directory="curriculo/static"), name="static")

@app.get("/")
def read_root():
    return FileResponse(Path("curriculo/index.html"))
