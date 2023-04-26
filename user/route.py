from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql import models, schemas
from sql.database import get_engine, get_db
from . import crud

models.Base.metadata.create_all(bind=get_engine('../'))


# 属于该模块的路由
user_router = APIRouter(
    # 路径前缀，该模块下所有路径操作的前缀
    prefix="/users",
    # 标签
    tags=["stock-index"],
    # 响应
    responses={404: {"description": "users Not found"}}
)


@user_router.post("", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    print(user)
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# @user_router.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @user_router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
