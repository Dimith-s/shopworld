from django.db import models

# Create your models here.

#model for the banners

class sitesetting(models.Model):
    banner = models.ImageField(upload_to='media')
    caption = models.TextField()
