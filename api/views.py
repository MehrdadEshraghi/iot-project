from rest_framework.response import Response
from rest_framework.decorators import api_view
from station.models import *
from .serializers import *

@api_view(['GET'])
def getLogs(request):
    items = Log.objects.all()
    serializer = GetLogSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addLog(request):
    serializer = LogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getStations(request):
    items = Station.objects.all()
    serializer = StationSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getModules(request):
    items = Module.objects.all()
    serializer = ModuleSerializer(items, many=True)

    return Response(serializer.data)