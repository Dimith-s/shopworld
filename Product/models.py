from django.db import models

# Create your models here.
#model for the products

class Products(models.Model):
    LIVE = 1
    DELETE = 0 
    delete_choice = ((LIVE,'live'),(DELETE,'delete'))
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=delete_choice,default='LIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.title
    
