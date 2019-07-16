from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from trello.serializers import GroupModelSerializer, CardModelSerializer, TodoModelSerializer, CommentModelSerializer
from trello.models import GroupModel, CardModel, TodoModel, CommentModel

class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = CardModel.objects.all()
    serializer_class = CardModelSerializer

    def destroy(self, *args, **kwargs):
        b = CardModel.objects.get(pk=kwargs.get('pk'))
        b.delete()
        b.save()
        return Response("Deleted")

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer

    # def update_status(self):
    #     serializer = self.serializer_class
    #
    #     if self.request.method == 'PUT':
    #         serializer = TodoModelSerializer
    #         serializer['todo_status'] = True
    #         serializer.save()
    #
    #     return serializer

    def update(self, *args, **kwargs):
        print(kwargs.get('pk'))
        a = TodoModel.objects.get(pk=kwargs.get('pk'))
        a.todo_status = True
        a.save()
        return Response("Updated.")

class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelSerializer
