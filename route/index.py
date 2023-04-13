from fastapi import APIRouter, Depends, HTTPException
from data import index
# 属于该模块的路由
index_router = APIRouter(
    # 路径前缀，该模块下所有路径操作的前缀
    prefix="/stock-index",
    # 标签
    tags=["stock-index"],
    # 响应
    responses={404: {"description": "users Not found"}}
)

# 查询指数
@index_router.get('/search/{input_text}')
async def search(input_text):
    return index.search(input_text)


@index_router.post('/save/{name}/{code}')
async def save(name,code):
    return index.save_day(name,code)





