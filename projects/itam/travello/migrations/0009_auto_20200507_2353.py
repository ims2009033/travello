# Generated by Django 3.0.5 on 2020-05-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_infrastructure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='brand',
            field=models.CharField(max_length=20),
        ),
    ]
