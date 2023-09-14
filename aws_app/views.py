from aws_app.models import aws_app
from aws_app.serializers import awsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class aws_List(APIView):
    def get(self, request, format=None):
        aws_app = aws_app.objects.all()
        serializer = awsSerializer(aws_app, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = awsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)