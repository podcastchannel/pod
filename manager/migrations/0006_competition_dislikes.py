# Generated by Django 4.2.3 on 2023-07-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_remove_competition_dislikes_remove_competition_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='dislikes',
            field=models.ManyToManyField(to='manager.manager'),
        ),
    ]
