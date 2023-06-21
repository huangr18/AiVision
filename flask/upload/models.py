from upload import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    firstname = db.Column(db.String(length=30), nullable=False)
    video_URL = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=1024))

    def __repr__(self):
        return f'User {self.username}'