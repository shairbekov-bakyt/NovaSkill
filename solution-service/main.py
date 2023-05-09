from fastapi import FastAPI


def get_app() -> FastAPI:
    app = FastAPI()
    return app


app = get_app()


@app.get('/solutions/')
async def get_solution():
    return {"solutions": [
        {"problem_id": 1},
        {"problem_id": 2},
        {"problem_id": 3},
        {"problem_id": 4},
    ]}
