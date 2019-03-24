import factory

from app import db
from app.database import User


class SQLAlchemyModelFactory(factory.Factory):
    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = db.session
        session.begin(nested=True)
        obj = model_class(*args, **kwargs)
        session.add(obj)
        session.commit()
        return obj


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
