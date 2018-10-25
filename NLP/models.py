from django.db import models

# Create your models here.

class NLP_MAPS(models.Model):
    id = models.IntegerField(primary_key=True)
    x = models.FloatField() 
    y = models.FloatField()
    Address = models.TextField()
    intensity = models.IntegerField()

    def __str__(self):
        return self.Address 