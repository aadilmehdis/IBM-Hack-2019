# Generated by Django 2.2 on 2019-07-20 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energyaudit', '0006_auto_20190719_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisaggregationResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_aggregate', models.FloatField()),
                ('fridge', models.FloatField()),
                ('ac', models.FloatField()),
                ('washing_machine', models.FloatField()),
            ],
        ),
    ]