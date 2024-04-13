from django.db import models
from django.utils import timezone

# Create your models here.

class Submit(models.Model):
    name = models.CharField(max_length=30)
    # author = models.ForeignKey(
    #              'auth.User',
    #              on_delete=models.CASCADE,
    #              )
    GRADE = (('grade6','grade 6'),
             ('grade7','grade 7'))
    grade = models.CharField(max_length=50,choices=GRADE)
    project = models.CharField(max_length=50)
    progress = models.TextField()
    HOURS = ((1,1),
             (2,2),
             (3,3),
             (4,4),
             (5,5)
             )
    hours = models.IntegerField(choices=HOURS)
    LEARNING = (('Active_Recall','Active Recall'),
             ('Horizontal_Learning','Horizontal Learning'),
             ('Vertical_Learning','Vertical Learning'))
    learning = models.CharField(max_length=50,choices=LEARNING)
    how = models.TextField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name +  '' + self.grade
    
class Reading(models.Model):
    topic = models.CharField(max_length=30)
    details = models.TextField()
    
    def __str__(self):
        return self.topic 