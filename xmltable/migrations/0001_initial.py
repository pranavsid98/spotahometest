# Generated by Django 2.0.1 on 2019-01-30 05:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.IntegerField()),
                ('title', models.TextField(default='')),
                ('link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('city', models.CharField(max_length=100)),
                ('main_image', models.TextField(validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]