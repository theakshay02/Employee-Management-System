# Generated by Django 3.1.7 on 2021-05-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_auto_20210502_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applyforleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20)),
                ('leave_type', models.CharField(max_length=30)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('avial_days', models.IntegerField(default=0, null=True)),
                ('req_days', models.IntegerField(default=0, null=True)),
                ('reason', models.TextField()),
            ],
        ),
    ]
