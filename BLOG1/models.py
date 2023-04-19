from django.db import models
from datetime import datetime


# Create your models here.
class blogpost(models.Model):
    blog_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=300,default="")
    head0  = models.CharField(max_length=300,default="")
    chead = models.TextField(max_length=3000,default="")
    head1  = models.CharField(max_length=300,default="")
    chead1  = models.TextField(max_length=300,default="")
    head2 = models.CharField(max_length=300,default="")
    chead2 = models.TextField(max_length=3000,default="")
    image =  models.ImageField(upload_to='shop/images',default='')
    date = models.DateField(("DATE"),default=datetime.now())

    def __str__(self):
        return self.title