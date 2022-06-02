from distutils.command.upload import upload
from django.db import models

# Create your models here.
exercise_choices =(
    ("1", "timebased"),
    ("2", "repbased"),
    
)
class Exercise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    type=models.CharField(choices=exercise_choices,default=1, max_length=50)
    duration=models.DurationField()
    no_of_reps=models.IntegerField()
    no_of_sets=models.IntegerField()
    score=models.IntegerField()
    images=models.ImageField(upload_to='images/')

class User:  
    pass #defalut Django user

class UserProgress(models.Model):
    id=models.IntegerField(primary_key=True)
    user=models.ForeignKey('User')
    date=models.DateField()
    score=models.IntegerField()
    exercises=models.ManyToManyField(Exercise)
