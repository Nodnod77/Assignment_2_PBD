from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    #image = models.ImageField(upload_to='products/') work with Pillow package
    stock = models.IntegerField()
    

    def __str__(self):
        return self.name
