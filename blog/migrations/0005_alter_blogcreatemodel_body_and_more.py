# Generated by Django 4.2.4 on 2023-08-31 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogcreatemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcreatemodel',
            name='body',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blogcreatemodel',
            name='image',
            field=models.ImageField(upload_to='blog_image', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='blogcreatemodel',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название статьи'),
        ),
    ]
