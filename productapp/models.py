from django.db import models

# Create your models here.
class product(models.Model):
    productid=models.IntegerField(primary_key=True)
    productname=models.CharField(max_length=10)
    productcost=models.DecimalField(max_digits=10,decimal_places=2)
    productmfdt=models.DateField()
    productexpdt=models.DateField()
