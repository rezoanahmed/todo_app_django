# Generated by Django 3.1.4 on 2020-12-09 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='add_todo',
        ),
    ]
