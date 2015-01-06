import sys

from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.models import User
from app.clients.models import Client

def create_all():
    return db.create_all()

def drop_all():
    return db.drop_all()

def load_fixture():
    drop_all()
    create_all()
    u = User(**{
        'name': "Dush",
        'email': 'dushyantrijhwani@gmail.com',
        'password': generate_password_hash('123456'),
    })
    db.session.add(u)
    db.session.commit()
    print u.id
    c = Client(
        name='ib',
        description='IB',
        secret='topsecret',
        redirect_url='http://testapp:8090/login.html'
    )
    db.session.add(c)
    db.session.commit()

    u.clients.append(c)
    db.session.add(u)
    db.session.commit()

if __name__ == '__main__':

    try:
        command = sys.argv[1]
    except IndexError:
        msg = "In this naive command tool, you need to supply a command."
        raise Exception(msg)

    try:
        command_method = globals()[command]
    except KeyError:
        msg = "Could not find your command %s, can you find it %s" % (command, globals().keys())
        raise Exception(msg)

    print command_method()
