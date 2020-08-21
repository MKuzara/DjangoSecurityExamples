from django.db import models

# Create your models here.
class Secret(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    is_secret = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    