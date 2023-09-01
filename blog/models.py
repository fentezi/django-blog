from django.db import models
from django.urls import reverse
from django.conf import settings
from slugify import slugify


# Create your models here.
class BlogCreateModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    image = models.ImageField(upload_to='blog_image', verbose_name='Фото')
    slug = models.SlugField(unique=True)
    body = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Blog'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogCreateModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={
            'slug': self.slug,
        })
