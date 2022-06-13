# Generated by Django 4.0.5 on 2022-06-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(help_text='Enter the movie description'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.CharField(help_text='Enter the poster url', max_length=500),
        ),
    ]
