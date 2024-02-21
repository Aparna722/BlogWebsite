# Generated by Django 3.2.7 on 2024-02-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_auto_20240130_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]