# Generated by Django 5.1.4 on 2024-12-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description_author',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
