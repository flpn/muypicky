# Generated by Django 2.0 on 2018-01-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
