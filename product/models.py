from django.db import models
from category.models import *
from brand.models import *
from shop_admin.models import *
from profiles.models import *


class Ecomproduct(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    review=models.TextField()
    product_id=models.IntegerField()
    base_price=models.IntegerField()
    price=models.IntegerField()
    ratings=models.IntegerField()
    sales=models.IntegerField()
    stocks=models.IntegerField()
    Image_url=models.URLField()
    details=models.TextField()
    weights=models.IntegerField()
    barcode=models.TextField()
    manufacturing_date=models.DateField()
    expiry_date=models.DateField()

    category_id=models.ForeignKey(category,on_delete=models.DO_NOTHING)
    brand_id=models.ForeignKey(brands,on_delete=models.DO_NOTHING)
    shop_admin_id=models.ForeignKey(shopadmin,on_delete=models.DO_NOTHING)



class Review_List(models.Model):
    id=models.BigAutoField(primary_key=True)
    review_date=models.DateField()
    review=models.TextField()
    product_ratings=models.TextField()
    # user_id=models.ForeignKey(User_Profiles,on_delete=models.DO_NOTHING)
    product_id=models.ForeignKey(Ecomproduct,on_delete=models.CASCADE)

