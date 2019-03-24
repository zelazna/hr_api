from app import db


class Match(db.Model):
    __tablename__ = 'matchs'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'job_id', name='unique_match'),
    )
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('matchs', lazy=True))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    job = db.relationship('Job', backref=db.backref('matchs', lazy=True))
    interest = db.Column(db.Boolean)
