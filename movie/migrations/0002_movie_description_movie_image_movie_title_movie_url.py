# Generated by Django 4.2.4 on 2023-08-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=' ', upload_to='movie/images/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.URLField(blank=True, default=' '),
        ),
    ]
