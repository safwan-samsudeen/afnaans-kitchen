# Generated by Django 3.1.1 on 2020-09-28 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]