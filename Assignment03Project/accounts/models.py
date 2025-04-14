from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.user_group})"

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through='user_group')

    def __str__(self):
        return self.name