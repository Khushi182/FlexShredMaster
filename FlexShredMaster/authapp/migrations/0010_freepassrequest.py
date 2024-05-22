# Generated by Django 4.2.3 on 2024-02-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreePassRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('trial_date', models.DateField()),
            ],
        ),
    ]
