from app import db


class Client(db.Model):

    __tablename__ = 'clients_client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text())
    redirect_url = db.Column(db.Text())
    secret = db.Column(db.String(40), index=True)

    def __repr__(self):
        return '<Client %r>' % (self.name)

