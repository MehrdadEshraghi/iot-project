from rest_framework.response import Response
from rest_framework.decorators import api_view
from station.models import Log
from .serializers import LogSerializer

@api_view(['GET'])
def getData(request):
    items = Log.objects.all()
    serializer = LogSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addLog(request):
    serializer = LogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)