from fastapi import FastAPI


def get_app() -> FastAPI:
    app = FastAPI()
    return app


app = get_app()


@app.get('/users/')
async def get_users():
    return {"users": [
        {"username": "c0mrade"},
        {"username": "aselkk"},
        {"username": "Israilov"},
        {"username": "Bakai"},
    ]}
