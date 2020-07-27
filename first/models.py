from django.db import models

# Create your models here.
class Form(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Country = models.CharField(max_length=255, default=0)
    Comment = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.Email

class Feedback(models.Model):
    Name = models.CharField(max_length=255)
    feedback = models.TextField(blank=True,null=True)
    Archived = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

class GalleryImage(models.Model):
    HoverTitle = models.CharField(max_length=255)
    PicTitle = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='gallery_pics/')

    def __str__(self):
        return self.PicTitle

class Information_slide(models.Model):
    Title = models.CharField(max_length=255)
    latest_news = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Title