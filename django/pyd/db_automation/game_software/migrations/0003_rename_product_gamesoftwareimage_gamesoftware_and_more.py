# Generated by Django 5.1.4 on 2024-12-18 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_software', '0002_gamesoftwareimage_gamesoftwareprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesoftwareimage',
            old_name='product',
            new_name='gameSoftware',
        ),
        migrations.RenameField(
            model_name='gamesoftwareprice',
            old_name='product',
            new_name='gameSoftware',
        ),
    ]
