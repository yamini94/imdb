# Generated by Django 3.1 on 2020-08-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Imdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('popularity', models.FloatField(default=0.0)),
                ('director', models.CharField(blank=True, max_length=200, null=True)),
                ('imdb_score', models.FloatField(default=0.0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('genre', models.ManyToManyField(to='movie.Genre')),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
    ]
