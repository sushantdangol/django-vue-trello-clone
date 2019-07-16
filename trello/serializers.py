from rest_framework import serializers
from trello.models import GroupModel, CardModel, TodoModel, CommentModel

class GroupModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupModel
        fields = ('group_title', 'pk')

class CardModelSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.group_title', read_only=True)

    class Meta:
        model = CardModel
        fields = ('pk', 'group_name', 'group', 'card_title', 'card_description', 'images')

class TodoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoModel
        fields = ('pk','todo_name', 'card', 'todo_status')

class CommentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = ('pk','card', 'user', 'comment')