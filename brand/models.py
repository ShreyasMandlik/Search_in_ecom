from django.db import models

class brands(models.Model):
    brand_id= models.BigAutoField(primary_key=True)
    product=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    sales=models.IntegerField()
    image_url=models.TextField()