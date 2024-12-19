from django.db import models
from django.contrib.auth.models import User

class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=100)
    duration = models.FloatField()  # Duration in minutes
    date = models.DateField()

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=100)
    target_value = models.FloatField()
    current_value = models.FloatField(default=0)
    achieved = models.BooleanField(default=False)
