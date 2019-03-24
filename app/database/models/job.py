from app import db


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True, index=True)
    text = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    url = db.Column(db.String(400), unique=True, nullable=False, index=True)
    email = db.Column(db.String(400))
    ref = db.Column(db.String(200))
