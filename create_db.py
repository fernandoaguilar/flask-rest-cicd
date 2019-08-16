# This must be contained in a function so we can call it with Zappa
import os
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def db_create():
    dbname = os.getenv('POSTGRES_DB_NAME')
    user = os.getenv('POSTGRES_DB_USER')
    password = os.getenv('POSTGRES_PW')
    host = os.getenv('POSTGRES_URL')

    con = None
    con = connect(dbname='postgres', user=user, host=host, password=password)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute('CREATE DATABASE ' + dbname)
    cur.close()
    con.close()

    # self.stdout.write(self.style.SUCCESS('All Done'))


def db_init():
    from myapi.app import create_app, db

    app = create_app()
    app.app_context().push()

    from myapi.models import User, Food

    # if you have more models just add them here
    # from project.models.model2 import Model2
    # from project.models.lots_of_models import Model3, Model4, Model5

    db.create_all()
    f = Food(name='Ramen')
    db.session.add(f)
    f = Food(name='Tacos')
    db.session.add(f)
    f = Food(name='Pizza')
    db.session.add(f)
    f = Food(name='Burgers')
    db.session.add(f)
    f = Food(name='Sushi')
    db.session.add(f)
    f = Food(name='Pho')
    db.session.add(f)
    f = Food(name='Kabob')
    db.session.add(f)
    f = Food(name='Falafel')
    db.session.add(f)
    f = Food(name='Sichuan')
    db.session.add(f)
    f = Food(name='Korean BBQ')
    db.session.add(f)
    db.session.commit()


if __name__ == "__main__":
    db_create()
    db_init()
