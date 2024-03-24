from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE
    )

    objects = models.Manager()

    def __str__(self):
        return self.title
