# Generated by Django 3.0.5 on 2020-04-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aboutme1', models.CharField(max_length=600)),
                ('aboutme2', models.CharField(max_length=600)),
                ('aboutsite1', models.CharField(max_length=600)),
                ('aboutsite2', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bhanai', models.CharField(max_length=700)),
                ('bhanne', models.CharField(max_length=100)),
            ],
        ),
    ]