# Generated by Django 3.0.8 on 2020-08-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
    ]
