# Generated by Django 2.0.3 on 2018-05-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0010_auto_20180527_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
