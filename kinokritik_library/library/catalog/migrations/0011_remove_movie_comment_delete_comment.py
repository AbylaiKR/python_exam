# Generated by Django 4.0.5 on 2022-06-11 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_movie_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
