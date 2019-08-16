"""Default configuration

Use env var to override
"""
import os
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
CELERY_BROKER_URL = "amqp://guest:guest@localhost/"
CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost/"


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def create_db_url(user, pw, url, db):
    return f"postgresql://{user}:{pw}@{url}/{db}"


POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

# DB
SQLALCHEMY_DATABASE_URI = create_db_url(POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB)
