# Generated by Django 3.1.7 on 2021-03-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0002_auto_20210327_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatpoll',
            name='on1',
            field=models.IntegerField(default=0),
        ),
    ]
