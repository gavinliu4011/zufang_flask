from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='statics', static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/zufang?charset=utf8'
    # 追踪数据库的修改行为，如果不设置会报警告，不影响代码的执行
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 显示sql语句
    # SQLALCHEMY_ECHO = True

    db.init_app(app)

    from zufang_flask.house_view import house

    app.register_blueprint(house)

    return app
