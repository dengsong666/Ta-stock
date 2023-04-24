from fastapi import APIRouter, Depends, HTTPException
from app import index

# 属于该模块的路由
router = APIRouter(
    # 路径前缀，该模块下所有路径操作的前缀
    prefix="/stock-index",
    # 标签
    tags=["stock-index"],
    # 响应
    responses={404: {"description": "users Not found"}}
)


# 查询指数
@router.get('/search')
async def search(input_value):
    return index.search(input_value)


# 保存指数
@router.get('/get-day')
async def save(name, code, source):
    return index.get_day(name, code, source)

