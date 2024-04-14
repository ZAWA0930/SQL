from enum import unique
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'  # 修正された行

# 現在の作業中のディレクトリを基準に絶対パスを返す
basedir = os.path.abspath(os.path.dirname(__file__))
# DBがSQLiteであることを明示 +appファイルがある場所にDB作成
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# DB変更履歴→不要
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# DBテーブル定義
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)  # uniqueで重複不可
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    administrator = db.Column(db.String(1))
    
    # 受け取った値を格納
    def __init__(self, email, username, password, administrator):  # 修正された行
        
        self.email = email
        self.username = username
        self.password = password
        self.administrator = administrator
    
    # Usernameを表示
    def __repr__(self):
        return f"UserName: {self.username}"



if __name__ == '__main__':
    app.run(debug=True)