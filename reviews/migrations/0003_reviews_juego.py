# Generated by Django 4.2.3 on 2023-08-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_reviews_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='juego',
            field=models.CharField(choices=[('Selecciona un Juego', 'Selecciona un Juego'), ('Minecraft', 'Minecraft'), ('League of Legends', 'League of Legends'), ('Counter Strike Global Ofensive', 'Counter Strike Global Ofensive'), ('Terraria', 'Terraria'), ('Valorant', 'Valorant'), ('Grand Theft Auto V', 'Grand Theft Auto V'), ('Phasmophobia', 'Phasmophobia')], default='Selecciona un Juego', max_length=50),
        ),
    ]
