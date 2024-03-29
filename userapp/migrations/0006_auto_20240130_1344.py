# Generated by Django 3.2.7 on 2024-01-30 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20240125_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likedusers',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.blog')),
            ],
        ),
    ]
