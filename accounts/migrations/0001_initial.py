# Generated by Django 3.2.4 on 2021-10-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_num', models.IntegerField(max_length=12, unique=True)),
                ('ph_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
