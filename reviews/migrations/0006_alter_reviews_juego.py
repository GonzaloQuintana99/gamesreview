# Generated by Django 4.2.3 on 2023-08-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_reviews_juego'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='juego',
            field=models.CharField(choices=[('NADA', 'Selecciona un Juego'), ('Minecraft', 'Minecraft'), ('League of Legends', 'League of Legends'), ('Counter Strike Global Ofensive', 'Counter Strike Global Ofensive'), ('Terraria', 'Terraria'), ('Valorant', 'Valorant'), ('Grand Theft Auto V', 'Grand Theft Auto V'), ('Phasmophobia', 'Phasmophobia'), ('Rust', 'Rust')], default='NADA', max_length=50),
        ),
    ]
