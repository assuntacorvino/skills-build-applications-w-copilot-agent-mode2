
from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    _id = models.ObjectIdField()
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.points}"
