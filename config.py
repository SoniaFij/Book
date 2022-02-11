import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kukabura'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower () in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    BOOK_MAIL_SUBJECT_PREFIX = '[Book]'
    BOOK_MAIL_SENDER = 'Żako The Papug <zakothepapug.gmail.com>'
    BOOK_ADMIN = os.environ.get('BOOK_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False