# Generated by Django 4.2.3 on 2023-07-21 08:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_alter_blog_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumb',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='thumb',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='audio',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Audio'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='thumb',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='program',
            name='thumb',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
    ]
