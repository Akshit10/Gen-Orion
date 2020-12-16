from django.contrib.auth.models import User
from django.db import connections
from django.db import models

class device_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    device_id = models.IntegerField(unique=True)
    device_name = models.CharField(max_length=40)
    value = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

class sensor_table(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sensor_id = models.IntegerField(unique=True)
    sensor_name = models.CharField(max_length=40)
    value = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()    


class nodemcu_table(models.Model):
    id = models.AutoField(primary_key=True)
    val1 = models.CharField(max_length=30)
    val2 = models.CharField(max_length=30)
    date = models.DateTimeField(null=True)