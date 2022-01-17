from django.shortcuts import render
from .models import BookappModel
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
#reading the data
@api_view(['GET'])
def Booklist(request):
    booksobj=BookappModel.objects.all()
    serializers=BookappSerializer(booksobj,many=True)
    return Response(serializers.data)
@api_view(['POST'])
def Post_Booklist(request):
    booksobj=BookappModel.objects.all()
    serializers=BookappSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
@api_view(['POST'])
def Update_Booklist(request):
    booksobj=BookappModel.objects.get(id=id)
    serializers=BookappSerializer(instance=booksobj,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
@api_view(['GET','DELETE'])
def Delete_Booklist(request,id):
    booksobj=BookappModel.objects.get(id=id)
    booksobj.delete()
    return Response("field is deleted")

