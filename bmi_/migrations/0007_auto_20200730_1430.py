# Generated by Django 3.0.8 on 2020-07-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi', '0006_auto_20200730_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='bmi_output',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]