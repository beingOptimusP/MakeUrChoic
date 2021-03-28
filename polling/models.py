from django.db import models

# Create your models here.
class CreatPoll(models.Model):
    Title = models.TextField()
    o1 = models.CharField( max_length=50)
    o2 = models.CharField( max_length=50)
    o3 = models.CharField( max_length=50)
    o4 = models.CharField( max_length=50)
    on1= models.IntegerField(default=0)
    on2= models.IntegerField(default=0)
    on3= models.IntegerField(default=0)
    on4= models.IntegerField(default=0)
    one_1=models.IntegerField(default=0)
    two_1=models.IntegerField(default=0)
    three_1=models.IntegerField(default=0)
    four_1=models.IntegerField(default=0)
    


class OpenPoll(models.Model):
    Title = models.TextField()
    o1 = models.CharField( max_length=50)
    o2 = models.CharField( max_length=50)
    o3 = models.CharField( max_length=50)
    o4 = models.CharField( max_length=50)
    on1= models.IntegerField(default=0)
    on2= models.IntegerField(default=0)
    on3= models.IntegerField(default=0)
    on4= models.IntegerField(default=0)

