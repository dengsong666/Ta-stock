from fastapi import APIRouter, Depends, HTTPException
from data import zhongzheng_index

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
async def search(input):
    print(input)
    return zhongzheng_index.search(input)

# 保存指数
@router.get('/get-day')
async def save(name, code):
    return zhongzheng_index.get_day(name, code)