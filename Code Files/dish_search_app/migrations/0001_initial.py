# Generated by Django 4.2.2 on 2023-06-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.CharField(max_length=100)),
                ('restaurant_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('items', models.JSONField()),
            ],
        ),
    ]