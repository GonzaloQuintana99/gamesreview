# Generated by Django 4.2.3 on 2023-08-19 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='juego',
        ),
    ]
