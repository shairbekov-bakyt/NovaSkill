from fastapi import FastAPI


def get_app() -> FastAPI:
    app = FastAPI()
    return app


app = get_app()


@app.get('/problems/')
async def get_problems():
    return {"problem": [
        {"name": "Trie"},
        {"name": "Binary Tree"},
        {"name": "Isort Algorithm"},
    ]}
