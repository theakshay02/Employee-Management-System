# Generated by Django 3.1.7 on 2021-05-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0005_auto_20210503_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approveleave',
            name='Mgr_id',
            field=models.CharField(max_length=30),
        ),
    ]
