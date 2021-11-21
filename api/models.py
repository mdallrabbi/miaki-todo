from django.db import models


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
