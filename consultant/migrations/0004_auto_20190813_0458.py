# Generated by Django 2.0 on 2019-08-13 04:58

import consultant.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0003_auto_20190810_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام و نام خانوادکی'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='skill',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='تخصص'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='address',
            field=models.CharField(max_length=300, verbose_name='ادرس'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='city',
            field=models.CharField(choices=[('1', 'Tehran')], max_length=1, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='commission_rate',
            field=models.IntegerField(blank=True, null=True, verbose_name='نرخ کمیسیون'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت اکانت'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=consultant.models.get_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='popularity',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, verbose_name='محبوبیت'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='special',
            field=models.BooleanField(default=False, verbose_name='کاربر ویژه'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='urban_area_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22')], max_length=2, verbose_name='شماره منطقه'),
        ),
    ]
