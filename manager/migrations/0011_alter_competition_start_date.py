# Generated by Django 4.2.3 on 2023-07-20 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_alter_competition_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
