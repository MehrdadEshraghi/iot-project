from django.db import models

# Create your models here.

class Sensor(models.Model):
    type = models.CharField(max_length=32, choices= [('temperature', 'temperature'), ('pressure', 'pressure')])
    model = models.CharField(max_length=32)
    sampling_rate = models.CharField(max_length=32)
    operational_capacity = models.DecimalField(decimal_places=3, max_digits=7)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, blank=True, null=True)
    # logs = models.ForeignKey('Log', on_delete=models.CASCADE, related_name='+', blank=True, null=True)

class Module(models.Model):
    module_id = models.CharField(max_length= 32)
    mobile_number = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    protocol_type = models.CharField(max_length=10, choices=[('one', 'two'), ('three', 'four')])
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='+')

class Station(models.Model):
    x = models.CharField(max_length=30)
    y = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    nominal_capacity = models.DecimalField(decimal_places=3, max_digits=7)
    operational_capacity = models.DecimalField(decimal_places=3, max_digits=7)
    modules = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='+', blank=True, null=True)

class Log(models.Model):
    # modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    module_id = models.CharField(max_length= 32)
    p_value = models.DecimalField(decimal_places=3, max_digits=7)
    t_value = models.DecimalField(decimal_places=3, max_digits=7)
    # unit = models.CharField(max_length=10, choices= [('C', 'C'), ('hPa', 'hPa')])
    # type = models.CharField(max_length=10, choices= [('temperature', 'temperature'), ('pressure', 'pressure')])
    createdAt = models.DateTimeField(auto_now_add=True)
    # date = models.DateField()
    # time = models.TimeField()