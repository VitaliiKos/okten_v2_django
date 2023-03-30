# Generated by Django 4.1.7 on 2023-04-01 20:58

import django.db.models.deletion
from django.db import migrations, models

import core.services.upload_car_service


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='photo',
        ),
        migrations.CreateModel(
            name='CarPhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=core.services.upload_car_service.upload_to)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='cars.carmodel')),
            ],
            options={
                'db_table': 'cars_photo',
            },
        ),
    ]
