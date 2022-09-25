from django.db import models

from shop_admin.models import *

class Employee(models.Model):
    id= models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    online=models.BooleanField(default=False)
    shop_admin_id=models.ForeignKey(shopadmin,on_delete=models.CASCADE)
