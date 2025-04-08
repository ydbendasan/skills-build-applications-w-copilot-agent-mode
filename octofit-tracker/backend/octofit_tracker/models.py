from djongo import models
from djongo.models.fields import ObjectIdField

class User(models.Model):
    _id = ObjectIdField(primary_key=True)  # Use ObjectIdField for MongoDB compatibility
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    _id = ObjectIdField(primary_key=True)  # MongoDB compatibility
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)  # Use ManyToManyField for proper relationship management

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True)  # Add ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True)  # Add ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True)  # Add ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=255)
    description = models.TextField()