from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.BlogCreateModel)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
