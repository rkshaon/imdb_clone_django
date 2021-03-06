# Generated by Django 3.1.2 on 2020-11-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0002_movie_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('movies', models.ManyToManyField(to='movie.Movie')),
            ],
        ),
    ]
