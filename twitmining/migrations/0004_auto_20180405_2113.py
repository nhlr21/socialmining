# Generated by Django 2.0.3 on 2018-04-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0003_auto_20180403_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_html', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]