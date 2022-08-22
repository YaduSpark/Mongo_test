import mongoengine
from mongoengine import Document, fields

# Create your models here.


class ProductCategory(Document):
    uid = fields.IntField(required=True, unique=True)
    name = fields.StringField(required=True)
    description = fields.StringField(null = True)


class ProductManufacturer(Document):
    uid = fields.IntField(required=True, unique=True)
    name = fields.StringField(required=True)
    description = fields.StringField(null = True)


class Product(Document):
    uid = fields.IntField(required=True, unique=True)
    name = fields.StringField(required=True)
    category = fields.ReferenceField(ProductCategory, reverse_delete_rule=mongoengine.CASCADE)
    manufacturer = fields.ReferenceField(ProductManufacturer, reverse_delete_rule=mongoengine.CASCADE)