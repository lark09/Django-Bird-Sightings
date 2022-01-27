from django.db import models

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name