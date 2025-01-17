# Generated by Django 4.1.7 on 2023-03-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stuAddress',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='stuEmail',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='stuPhone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
