from myapi.extensions import db, pwd_context


class Food(db.Model):
    """Basic user model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<Food %s>" % self.username
