# Generated by Django 3.0 on 2020-03-31 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_todo_useremail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='useremail',
        ),
    ]
