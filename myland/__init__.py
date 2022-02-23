from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)  # config.py에 있는 설정들 애플리케이션 객체에 적용
    
    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models  # 데이터 모델 가져옴
    
    # Blueprint
    # 블루브린트 사용이 없다면 create_app 함수 내부에 계속 라우트 함수를 추가해야 함 (hello_pybo같은)
    from .views import main_views, post_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(post_views.bp)
    app.register_blueprint(auth_views.bp)
    
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    return app
