from rest_framework import serializers
from station.models import *

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = (
            'module_id', 't_value',
            'p_value',
        )
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'