from django.db import models
from django.urls import reverse


# Create your models here.
class FurnituresModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='furniture_image')

    def get_absolute_url(self):
        return reverse('furnitures:furn_main')
