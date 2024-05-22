# Generated by Django 4.2.3 on 2024-01-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_kickboxingregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZumbaRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=255)),
                ('date_of_joining', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('payment_option', models.CharField(max_length=20)),
            ],
        ),
    ]
