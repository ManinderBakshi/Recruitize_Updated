import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    '''Config settings class.'''
   

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']


    SECRET_KEY = 'maninderbakshi'
        