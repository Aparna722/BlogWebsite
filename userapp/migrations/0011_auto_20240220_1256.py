# Generated by Django 3.2.7 on 2024-02-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_auto_20240220_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
