from django.contrib import admin
from trello.models import GroupModel, CardModel, TodoModel, CommentModel

admin.site.register(GroupModel)
admin.site.register(CardModel)
admin.site.register(TodoModel)
admin.site.register(CommentModel)

