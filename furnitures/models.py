from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


# Create your models here.
class FurnituresModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='furniture_image')

    class Meta:
        verbose_name = 'Furniture'

    def get_absolute_url(self):
        return reverse('furnitures:furn_main')


