from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()  # SQLAlchemy 객체 db
migrate = Migrate()  # Migrate 객체 migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)  # config.py에 있는 설정들 애플리케이션 객체에 적용
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models  # 데이터 모델 가져옴
    
    # Blueprint
    # 블루브린트 사용이 없다면 create_app 함수 내부에 계속 라우트 함수를 추가해야 함 (hello_pybo같은)
    from .views import main_views, post_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(post_views.bp)
    
    return app
