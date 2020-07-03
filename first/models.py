from django.db import models

# Create your models here.
class Form(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Country = models.CharField(max_length=50, default=0)
    Comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.Email
