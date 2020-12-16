from django.contrib import admin
from . models import *

admin.site.register(device_table)
admin.site.register(sensor_table)
admin.site.register(nodemcu_table)
