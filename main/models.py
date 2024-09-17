from django.db import models
import uuid



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    #image = models.ImageField(upload_to='products/') work with Pillow package
    stock = models.IntegerField()
    

    def __str__(self):
        return self.name
    
class FormEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    data1 = models.CharField(max_length=255)
    data2 = models.TextField()
    data3 = models.IntegerField()