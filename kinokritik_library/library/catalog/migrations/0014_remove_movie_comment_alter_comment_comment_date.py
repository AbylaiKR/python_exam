# Generated by Django 4.0.5 on 2022-06-13 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_comment_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 9, 14, 36, 19913)),
        ),
    ]
