# Generated by Django 2.0 on 2019-08-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20190805_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='code',
            field=models.PositiveIntegerField(default=55978),
        ),
    ]
