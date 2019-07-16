from django.urls import path, include
from rest_framework import routers
from trello.views import GroupViewSet, CardViewSet, TodoViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('groups', GroupViewSet, basename="groups")
router.register('cards', CardViewSet, basename="cards")
router.register('todos', TodoViewSet, basename="todos")
router.register('comments', CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls)),
]