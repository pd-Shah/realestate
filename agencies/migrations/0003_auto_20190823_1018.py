# Generated by Django 2.0 on 2019-08-23 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0002_auto_20190817_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencies',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]