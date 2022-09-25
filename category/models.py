from django.db import models
from brand.models import *

class category(models.Model):
    id = models.BigAutoField(primary_key=True)
    product=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    advertisement=models.TextField()
    image_url=models.TextField()
    brand_id = models.ForeignKey(brands, on_delete=models.DO_NOTHING)