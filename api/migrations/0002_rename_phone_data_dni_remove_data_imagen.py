# Generated by Django 4.1 on 2022-11-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='phone',
            new_name='dni',
        ),
        migrations.RemoveField(
            model_name='data',
            name='imagen',
        ),
    ]