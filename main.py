from fastapi import FastAPI

from route import index

app = FastAPI()
app.include_router(index.router)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
