from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class RoadMaps(models.Model):
    roadmap=models.FileField(upload_to='roadMaps/')
    def __str__(self):
        return self.roadmap
class playList(models.Model):
    link=models.CharField(max_length=100)
    def __str__(self):
        return self.link
    
class Resources(models.Model):
    resource=models.FileField('Rescourses/')
    def __str__(self):
        return self.resource