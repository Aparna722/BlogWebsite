# Generated by Django 3.2.7 on 2024-01-25 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0003_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
