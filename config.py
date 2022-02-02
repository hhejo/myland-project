import os

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'myland.db'))  # DB 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 이벤트 처리 옵션 비활성화
# myland.db 라는 데이터베이스 파일을 프로젝트의 루트 디렉터리에 저장
SECRET_KEY = 'dev'
