# Generated by Django 3.2.7 on 2024-01-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_auto_20240130_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='like',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
