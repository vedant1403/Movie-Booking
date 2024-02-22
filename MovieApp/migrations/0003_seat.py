# Generated by Django 5.0.2 on 2024-02-10 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0002_alter_movie1_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_Booked', models.CharField(max_length=5)),
                ('date', models.PositiveIntegerField()),
                ('time', models.IntegerField()),
                ('is_booked', models.BooleanField(default=False)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.movie1')),
            ],
        ),
    ]