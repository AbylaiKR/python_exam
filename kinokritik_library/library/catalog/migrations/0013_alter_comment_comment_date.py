# Generated by Django 4.0.5 on 2022-06-11 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_comment_movie_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 17, 0, 14, 987918)),
        ),
    ]
