from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="upload_images")
    
    def __str__(self):
        return self.product_name