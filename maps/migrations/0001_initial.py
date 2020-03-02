# Generated by Django 3.0.3 on 2020-03-02 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('icon', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('photo_height', models.IntegerField()),
                ('photo_width', models.IntegerField()),
                ('photo_reference', models.CharField(max_length=100)),
                ('photo_attributions', models.CharField(max_length=200)),
                ('place_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
                ('type_of', models.CharField(max_length=50)),
                ('formatted_address', models.CharField(max_length=200)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('place_id', models.CharField(max_length=100)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('place_id', models.CharField(max_length=100)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Day')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Trip'),
        ),
    ]