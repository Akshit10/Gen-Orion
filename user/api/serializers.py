from rest_framework import serializers
from django.contrib.auth.models import *
from user.models import sensor_table    

class userSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  '__all__'

class sensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = sensor_table
        fields = ['user','sensor_id','sensor_name','value']