from django.db import models


class Prediction(models.Model):
    description = models.CharField(max_length=300)
    subsidy_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subsidy_name
