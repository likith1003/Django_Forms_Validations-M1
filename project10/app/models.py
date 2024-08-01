from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    princy = models.CharField(max_length=50)

    def __str__(self):
        return self.sname   