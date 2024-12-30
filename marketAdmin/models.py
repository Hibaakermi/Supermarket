from django.db import models


class vegitables(models.Model):
    vname = models.CharField(max_length=30)
    vprice = models.IntegerField()
    vinfo = models.TextField()
    vamm = models.CharField(max_length=30,null=True)
    vimg= models.ImageField(upload_to='static/imagesv/')


class grocrey(models.Model):
    gname = models.CharField(max_length=30)
    gprice = models.IntegerField()
    ginfo = models.TextField()
    gamm = models.CharField(max_length=30,null=True)
    gimg= models.ImageField(upload_to='static/imagesg/')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

