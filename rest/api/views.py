from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import Item
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item_detail(request, pk):
    items = Item.objects.filter(pk=pk)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateItem(request,pk):
    items = Item.objects.filter(pk=pk).first()
    serializer = ItemSerializer(items,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
@api_view(['DELETE'])
def deleteItem(request,pk):
    items = Item.objects.get(pk=pk)
    items.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    