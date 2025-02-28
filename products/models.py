from django.db import models
from base.models import basemodel
from django.utils.text import slugify

# Create your models here.

class Category(basemodel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) # a slug field is a special field used to create human-readable, URL-safe identifiers for a model instance
    category_image = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self)->str:
        return self.category_name   



class Product(basemodel):
    product_name=models.CharField(max_length=50)
    slug = models.SlugField(unique=True , null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price=models.IntegerField()
    product_description=models.TextField(max_length=500)

# diffrent image class because we have to upload many images for one product

class Product_image(basemodel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE , related_name="product_images")
    image=models.ImageField(upload_to="product")     
    