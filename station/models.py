from django.db import models

# Create your models here.

class Sensor(models.Model):
    type = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    sampling_rate = models.CharField(max_length=30)
    operational_capacity = models.DecimalField(decimal_places=3, max_digits=7)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    # logs = 

class Module(models.Model):
    mobile_number = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    protocol_type = models.CharField(max_length=10, choices=[('this', 'that'), ('that', 'that')])
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='+')

class Station(models.Model):
    x = models.CharField(max_length=30)
    y = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    nominal_capacity = models.DecimalField(decimal_places=3, max_digits=7)
    operational_capacity = models.DecimalField(decimal_places=3, max_digits=7)
    modules = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='+')
