# Generated by Django 3.1.7 on 2021-03-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('img', models.ImageField(default='None', null=True, upload_to='pics')),
                ('salary', models.IntegerField(default=0, null=True)),
                ('leaves', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
