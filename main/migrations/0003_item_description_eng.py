# Generated by Django 5.1.4 on 2024-12-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_description_author_item_owner_item_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description_eng',
            field=models.TextField(blank=True),
        ),
    ]
