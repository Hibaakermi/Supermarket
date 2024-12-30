from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)    
    address = models.TextField()




class cart(models.Model):
    uid = models.ForeignKey(Users,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    item_price = models.BigIntegerField()