# Generated by Django 3.0.5 on 2022-04-04 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0009_auto_20220404_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='user',
        ),
    ]
