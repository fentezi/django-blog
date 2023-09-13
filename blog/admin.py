from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(models.BlogCreateModel)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('title', 'show_image', 'created_at', 'author',)
    list_filter = ('author',)
    search_fields = ('title', 'author',)
    date_hierarchy = 'created_at'

    def show_image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' height='60' />".format(obj.image.url))
        return None

    show_image.__name__ = 'Фото'
