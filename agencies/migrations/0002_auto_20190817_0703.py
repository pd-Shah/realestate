# Generated by Django 2.0 on 2019-08-17 07:03

import agencies.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agencies',
            name='commission_rate',
        ),
        migrations.AddField(
            model_name='agencies',
            name='code_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='شناسه صنفی '),
        ),
        migrations.AddField(
            model_name='agencies',
            name='image_owner',
            field=models.ImageField(blank=True, null=True, upload_to=agencies.models.get_image_path, verbose_name='تصویر مدیران و همکاران'),
        ),
        migrations.AddField(
            model_name='agencies',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='ادرس اینستاگرام'),
        ),
        migrations.AddField(
            model_name='agencies',
            name='web_site',
            field=models.URLField(blank=True, null=True, verbose_name='وب سایت'),
        ),
        migrations.AlterField(
            model_name='agencies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=agencies.models.get_image_path, verbose_name='تصویر آژانس'),
        ),
        migrations.AlterField(
            model_name='agencies',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='agencies',
            name='skill',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='حوزه فعالیت'),
        ),
    ]