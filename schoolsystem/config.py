import os
from schoolsystem import app

# dev_db = 'sqlite:////'+os.path.join(os.path.dirname(app.root_path),'test_mac.db')
# dev_db = 'sqlite:///'+os.path.join(os.path.dirname(app.root_path),'test_mac.db')

SECRET_KEY = os.getenv('SECRET_KEY', '11111111')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Dallasryp123@localhost:8889/schoolsystem'     #mac
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/schoolsystem'   #win
POST_PER_PAGE = 5
