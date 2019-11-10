# Generated by Django 2.2.7 on 2019-11-10 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('release_date', models.DateField()),
                ('type', models.CharField(choices=[('p', 'Painting'), ('m', 'Music'), ('f', 'Film')], max_length=1)),
                ('description', models.TextField()),
                ('artist', models.ManyToManyField(to='backend.Artist')),
            ],
        ),
    ]
