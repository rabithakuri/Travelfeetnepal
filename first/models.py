from django.db import models

# Create your models here.
class Form(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Country = models.CharField(max_length=50, default=0)
    Comment = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.Email

class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    feedback = models.TextField(blank=True,null=True)
    Archived = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
