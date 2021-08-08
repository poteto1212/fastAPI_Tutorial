from fastapi import FastAPI
from starlette.requests import Request
#テンプレートエンジンの導入
from starlette.templating import Jinja2Templates


#データベース関連プログラムのインポート
import db
from models import User, Task

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

def admin(request: Request):
    #クエリ取得
    #管理ユーザーのみを取得する。
    user=db.session.query(User).filter(User.username=='admin').first()
    #管理ユーザーが書いたタスクを全て取得
    task=db.session.query(Task).filter(Task.user_id == user.id).all()
    #データ取得後はセッションをクローズ
    db.session.close()    
    return templates.TemplateResponse('admin.html',
                                    {'request':request,
                                    'user':user,
                                    'task':task}
                                    )

