from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cat(db.Model):

    __tablename__ = 'cat'

    cat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    num_legs = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, breed: str, num_legs: int) -> None:
        self.name = name
        self.breed = breed
        self.num_legs = num_legs
