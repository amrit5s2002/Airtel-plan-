from django.db import models

# Create your models here.
class Plans(models.Model):
    plans = models.CharField(max_length=36)
    
    def __str__(self):
        return self.plans
    