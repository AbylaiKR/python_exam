# Generated by Django 4.0.5 on 2022-06-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='short_description',
            field=models.CharField(help_text='Enter the movie short description', max_length=100),
        ),
    ]
