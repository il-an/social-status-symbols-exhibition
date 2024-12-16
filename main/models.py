# Create your models here.
from django.db import models
from django.db.models import Model
from sorl.thumbnail import ImageField


class Category(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    description_eng = models.TextField(blank=True)
    description_author = models.CharField(max_length=150, blank=True)
    time = models.CharField(max_length=100, blank=True)
    owner = models.CharField(max_length=100, blank=True)
    picture = ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
