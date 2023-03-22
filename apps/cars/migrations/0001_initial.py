# Generated by Django 4.1.7 on 2023-03-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=20)),
                ('car_year', models.IntegerField()),
                ('number_of_seats', models.IntegerField()),
                ('car_body_type', models.CharField(max_length=20)),
                ('car_engine', models.FloatField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
