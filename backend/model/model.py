from flask import request, jsonify
from flask_sqlalchemy import flask_sqlalchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema

db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///model/book.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

ma = Marshmallow()
class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book

class Bookmodel:
    def all_list(self):
        result = Book.query.all()
        bookschema = BookSchema(many=True)
        res = bookschema.dump(result)
        return jsonify(res)

    def update(self):
        json = request.get_json()
        id = json['id']
        title = json['title']
        author = json['author']
        publisher = json['publisher']
        t = Book.query.get(id)
        t.id=id
        t.title=title
        t.author=author
        t.publisher=publisher
        db.session.commit()

    def delete(self):
        json = request.get_json()
        id = json['id']
        result = Book.query.get(id)
        db.session.delete(result)
        db.session.commit()

    def add(self):
        json = request.get_json()
        title = json['title']
        author = json['author']
        publisher = json['publisher']
        t = Book(title=title,author=author,publisher=publisher)
        db.session.add(t)
        db.session.commit()
        result = Book.query.order_by(Book.id.desc()).first()
        # 今登録したデータのidを取得
        id = str(result.id)
        return id