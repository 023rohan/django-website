from django.db import models
from datetime import datetime



# Create your models here.
class Product(models.Model):
    
    id = models.AutoField
    name = models.CharField(max_length=30,default="")
    desc = models.TextField(max_length=3000,default="")
    value = models.IntegerField(default="")
    #value21 = models.IntegerField(default="")
    category = models.TextField(max_length=300,default="")
    #amount  = models.CharField(max_length=20,default="")
    #price = models.IntegerField(default=0)
    subcategory = models.TextField(max_length=300,default="")
    image = models.ImageField(upload_to="shop/images",default="")
    date = models.DateField(("DATE"),default=datetime.now())
    
    

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=70,default="")
    email = models.CharField(max_length=70,default="")
    phone = models.IntegerField(default="")
    desc = models.TextField(max_length=300,default="")
    

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    item_json = models.TextField(max_length=300,default="")
    name = models.CharField(max_length=70,default="")
    email = models.CharField(max_length=70,default="")
    amount = models.IntegerField(default=0)
    #Value  = models.IntegerField(default=0)
    phone = models.IntegerField(default="")
    address = models.CharField(max_length=300,default="") 
    state = models.CharField(max_length=300,default="")
    city = models.CharField(max_length=300,default="")
    zip_code = models.CharField(max_length=300,default="")
    

    def __str__(self):
        return self.name

class Updateorder(models.Model):
    update_order = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField(max_length=3000,default="")
    update_time  = models.DateField(("DATE"),default=datetime.now())

    def __str__(self):
        return self.update_desc[0:7] + "..."

