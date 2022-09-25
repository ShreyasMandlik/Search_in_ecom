from django.db import models
from shop_admin.models import *
from category.models import *


class advertise(models.Model):
    id= models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=30)
    top_deals=models.IntegerField()
    image_url=models.TextField()
    shop_admin_id=models.ForeignKey(shopadmin,on_delete=models.DO_NOTHING)
    category_id=models.ForeignKey(category,on_delete=models.DO_NOTHING)