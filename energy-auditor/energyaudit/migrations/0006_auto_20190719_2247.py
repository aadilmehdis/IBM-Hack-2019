# Generated by Django 2.2 on 2019-07-19 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energyaudit', '0005_auto_20190719_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='pincode',
            field=models.PositiveIntegerField(),
        ),
    ]
