from django.db import models
import datetime

class Product(models.Model):
    pno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    maf_date = models.DateField()
    exp_date = models.DateField(default=datetime.date(2020,1,1))

