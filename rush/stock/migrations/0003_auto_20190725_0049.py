# Generated by Django 2.2.3 on 2019-07-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190725_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='lastprice',
            field=models.FloatField(null='true'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='name',
            field=models.CharField(max_length=10, null='true'),
        ),
    ]
