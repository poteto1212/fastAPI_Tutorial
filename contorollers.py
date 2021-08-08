from fastapi import FastAPI, Depends, HTTPException  # new
from fastapi.security import HTTPBasic,HTTPBasicCredentials  # new
from fastapi import security 
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED  # new
 
import db  # new
from models import User, Task  # new
 
import hashlib  # new

app=FastAPI(
    title='FastAPIで作るアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう',
    version='0.9 beta'
)


#テンプレートの設定
templates=Jinja2Templates(directory="templates")
jinja_env=templates.env

def index(request: Request):
    return templates.TemplateResponse('index.html',
                                    {'request':request}
                                    )

def admin(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # Basic認証で受け取った情報
    username = credentials.username
    password = hashlib.md5(credentials.password.encode()).hexdigest()
 
    # データベースからユーザ名が一致するデータを取得
    user = db.session.query(User).filter(User.username == username).first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all() if user is not None else []
    db.session.close()
 
    # 該当ユーザがいない場合
    if user is None or user.password != password:
        error = 'ユーザ名かパスワードが間違っています'
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=error,
            headers={"WWW-Authenticate": "Basic"},
        )
 
    # 特に問題がなければ管理者ページへ
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'user': user,
                                       'task': task})
