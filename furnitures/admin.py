from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.FurnituresModel)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    list_filter = ('price',)
    ordering = ('-price',)
    search_fields = ('title',)
