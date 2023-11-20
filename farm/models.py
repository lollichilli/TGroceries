"""Data model"""

from config import db, mm

class Products(db.Model):
    __tablename__ = "PRODUCTS"
    name = db.Column(db.String, primary_key=True)
    kind = db.Column(db.String)
    owner = db.Column(db.String)
    price = db.Column(db.Integer)
    image_url = db.Column(db.String)


class ProductsSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        load_instance = True


