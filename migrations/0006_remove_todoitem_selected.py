# Generated by Django 2.1 on 2019-04-20 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todoitem_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='selected',
        ),
    ]