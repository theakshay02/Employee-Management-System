# Generated by Django 3.1.7 on 2021-04-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_employee_isadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
