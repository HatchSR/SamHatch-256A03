from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_group = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} ({self.user_group})"
