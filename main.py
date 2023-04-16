from time import time

from fastapi import FastAPI,Request

from route import index

app = FastAPI()
app.include_router(index.router)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 请求前
    start_time = time()
    response = await call_next(request)
    # 请求后
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response