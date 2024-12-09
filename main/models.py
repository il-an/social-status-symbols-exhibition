# Create your models here.
from django.db.models import Model
from django.db import models
from sorl.thumbnail import ImageField


class Category(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
