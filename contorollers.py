from fastapi import FastAPI
from starlette.requests import Request
#テンプレートエンジンの導入
from starlette.templating import Jinja2Templates


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
    return templates.TemplateResponse('admin.html',
                                    {'request':request,
                                    'username':'admin'}
                                    )

