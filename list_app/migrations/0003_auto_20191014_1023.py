# Generated by Django 2.2.3 on 2019-10-14 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0002_todo_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='listKey',
            new_name='list_key',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='key',
        ),
    ]