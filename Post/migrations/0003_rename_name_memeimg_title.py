# Generated by Django 3.2.9 on 2021-11-15 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_rename_post_memeimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memeimg',
            old_name='Name',
            new_name='Title',
        ),
    ]