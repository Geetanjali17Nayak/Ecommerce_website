from django.db import models
from base.models import basemodel

# Create your models here.

class Category(basemodel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload="categories")




class Product(basemodel):
    product_name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price=models.IntegerField()
    product_description=models.TextField(max_length=500)

# diffrent image class because we have to upload many images for one product

class Product_image(basemodel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE , related_name="product_images")
    image=models.ImageField(upload="product")     
    