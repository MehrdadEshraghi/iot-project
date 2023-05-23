from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Station)
admin.site.register(Module)
admin.site.register(Sensor)
admin.site.register(Log)