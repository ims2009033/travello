# Generated by Django 3.0.5 on 2020-05-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_allotment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='floor',
            field=models.IntegerField(),
        ),
    ]
