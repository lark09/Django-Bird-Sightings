from django.db import models
from django.urls import reverse

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})


TIMES =(
        ('M', 'Morning'),
        ('N', 'Noon'),
        ('E', 'Evening'),
)

class Sighting(models.Model):
    date = models.DateField('Sighting date')
    sighting = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return f"{self.get_sighting_display()} on {self.date}"