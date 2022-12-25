from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=60, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='/no_image-1')
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="brands")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="update_brands")
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.code}-{self.name}'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=60, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='/no_image-1')
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="categories")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="update_categories")
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.code}-{self.name}'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=60, unique=True, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="products", db_index=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products", db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='/no_image-1')
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(default=0)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="products")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="update_products")
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.code}-{self.name}'
