# Generated by Django 3.1.7 on 2021-05-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmgrdept',
            name='Manager_Email',
            field=models.EmailField(max_length=70),
        ),
    ]
