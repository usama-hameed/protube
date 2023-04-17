from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .serializers import VideoSerializer, CommentSerializer
from .models import Videos, Comments
from django.core.exceptions import BadRequest
from django.http import HttpResponseBadRequest
from django.db import DatabaseError


class VideoView(viewsets.ViewSet):
    def list(self, request):
        try:
            videos = Videos.objects.all()
            serialized_data = VideoSerializer(videos, many=True)
            return Response(serialized_data.data)
        except DatabaseError as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        data = request.data

        try:
            Videos.objects.create(**data)
            return Response({'message': 'Video is Saved', 'status': status.HTTP_200_OK})
        except Exception as error:
            raise BadRequest(error)

    def update(self, request, pk=None):
        data = request.data
        try:
            Videos.objects.filter(id=pk).update(**data)
            return Response({'message': 'Updated', 'status': status.HTTP_200_OK})
        except Exception as error:
            raise BadRequest(error)

    def delete(self, request, pk=None):
        try:
            Videos.objects.delete(id=pk).delete()
            return Response({'message': 'Video Deleted Successfully', 'status': status.HTTP_200_OK})
        except Exception as error:
            raise BadRequest(error)


class CommentsView(viewsets.ViewSet):

    def list(self, request):
        data = request.data.dict()
        try:
            comments = Comments.objects.filter(video=data['video'])
            serialized_data = CommentSerializer(comments, many=True)
            return Response(serialized_data.data)
        except DatabaseError as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = request.data.dict()
        data['video'] = Videos.objects.get(id=data['video']).id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message': serializer.errors})

    def update(self, request, pk=None):
        data = request.data
        try:
            Comments.objects.filter(id=pk).update(**data)
            return Response({'message': 'Updated', 'status': status.HTTP_200_OK})
        except Exception as error:
            raise BadRequest(error)

    def delete(self, request, pk=None):
        try:
            Comments.objects.delete(id=pk).delete()
            return Response({'message': 'Comment Deleted Successfully', 'status': status.HTTP_200_OK})
        except Exception as error:
            raise BadRequest(error)
