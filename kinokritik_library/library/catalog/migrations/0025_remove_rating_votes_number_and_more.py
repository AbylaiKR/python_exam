# Generated by Django 4.0.5 on 2022-06-13 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_alter_comment_options_alter_comment_comment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='votes_number',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 15, 41, 57, 309333)),
        ),
    ]
