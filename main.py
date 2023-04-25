import os

import uvicorn as uvicorn
from fastapi import FastAPI, Request

from stock.route import stock_router
from user.route import user_router

app = FastAPI()
app.include_router(stock_router)
app.include_router(user_router)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
