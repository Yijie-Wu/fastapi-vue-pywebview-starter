import os

from app import create_app
from app.settings import STATIC_DIR
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = create_app()

app.mount("/assets", StaticFiles(directory=os.path.join(STATIC_DIR, 'assets')), name="assets")


@app.get('/', response_class=HTMLResponse)
def index():
    with open(os.path.join(STATIC_DIR, 'index.html'), encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app')
