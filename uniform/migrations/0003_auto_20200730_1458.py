# Generated by Django 3.0.8 on 2020-07-30 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniform', '0002_auto_20200730_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='uniform_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('uni_input', models.ImageField(max_length=255, upload_to='uniform/input/%Y/%m/%d')),
                ('uni_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='uniform',
        ),
    ]
