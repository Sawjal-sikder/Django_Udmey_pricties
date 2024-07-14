from django.db import models

# Create your models here.
class personModel(models.Model):
    first_name = models.CharField(max_length=55 )
    last_name = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.first_name}'