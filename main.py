from fastapi import FastAPI

import data.index

app = FastAPI()


@app.get("/index")
async def search():
    return data.crawling.search_index()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
