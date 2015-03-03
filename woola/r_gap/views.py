from django.shortcuts import render

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import GapSerializer

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


"""
@api_view(['GET', 'POST'])
def gapviewme(request, format=None):
  if request.method == 'GET':
    items = Item.objects.all()
    serializer = GapSerializer(items, many=True)
    print(serializer.data)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = GapSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class GapViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = GapSerializer



  # GET request.  Will response with a JSON object
  #def list(self, request):
   # pass


"""
  def create(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      # Add item to database
      #Item.objects.

      # Return Success response
      return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    # Return Unsuccess response
    return Response({
                'status' : 'Bad request',
                'message' : 'Sumtingwong!!!!'
              }, status=status.HTTP_400_BAD_REQUEST)
"""
