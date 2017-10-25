from django.db import models

# Create your models here.
class Prediction(models.Model):
    description = models.CharField(max_length=300)
    subsidy_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subsidy_name
