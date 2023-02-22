# Generated by Django 4.0 on 2023-02-22 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('opening_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('overview', models.TextField()),
            ],
        ),
    ]
