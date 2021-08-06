#モデル設計に必要なモジュール
from datetime import datetime
from db import Base

from sqlalchemy import Column,String,DateTime,ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER,BOOLEAN

import hashlib

#データベースディレクトリ
SQLITE3_NAME="./db.sqlite3"


#ユーザーモデル
class User(Base):
    __tablename__='user'
    #主キー
    id=Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,  
    )
    #ユーザー名
    usename=Column('username',String(256))
    #パスワード
    password=Column('password',String(256))
    #メールアドレス
    email=Column('mail',String(256))

    #インスタンス生成時に自動呼出し
    def __init__(self,username,password,mail):
        self.username = username
        #パスワードのハッシュ化
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail

    #テーブルの表示名
    def __str__(self):
        return str(self.id)+':'+self.username

#タスクモデル
class Task(Base):
    __tablename__="task"
    id = Column(
    INTEGER(unsigned=True),
    primary_key=True,
    autoincrement=True,
    )

    #外部キー
    user_id = Column('user_id',ForeignKey('user.id'))
    content = Column('content',String(256))
    deadline = Column('deadline',DateTime,default=None,nullable=False)