# Generated by Django 2.1.4 on 2019-08-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='percent',
            field=models.FloatField(null='true'),
            preserve_default='true',
        ),
    ]
