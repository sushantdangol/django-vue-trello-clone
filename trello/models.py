from django.db import models
from django.conf import settings

class GroupModel(models.Model):
    group_title = models.CharField(max_length=255)
    group_created_at = models.DateTimeField(auto_now=True)
    group_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name = "Group"

class CardModel(models.Model):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=255)
    card_description = models.TextField()
    images = models.ImageField(blank=True)
    card_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.card_title, self.group.group_title)

    class Meta:
        verbose_name = "Card"
        ordering = ('-card_created_at',)

class TodoModel(models.Model):
    card = models.ForeignKey(CardModel, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=255)
    todo_status = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.card.card_title, self.todo_name)

    class Meta:
        verbose_name = "Todo"

class CommentModel(models.Model):
    card = models.ForeignKey(CardModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return "Comment by: {}".format(self.user.first_name)



    