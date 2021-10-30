from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__name__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    RECAPTCHA_PUBLIC_KEY = environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = environ.get("RECAPTCHA_PRIVATE_KEY")
