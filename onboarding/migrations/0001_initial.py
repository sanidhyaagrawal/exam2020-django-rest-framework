# Generated by Django 3.0.5 on 2020-06-21 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
            ],
        ),
    ]
