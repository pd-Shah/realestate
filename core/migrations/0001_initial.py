# Generated by Django 2.2.3 on 2019-07-14 05:38

import core.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('year_of_construction', models.DateField()),
                ('room_number', models.PositiveSmallIntegerField()),
                ('house_square', models.PositiveSmallIntegerField()),
                ('category', models.CharField(choices=[('0', 'House'), ('1', 'Apartment'), ('2', 'Duplex'), ('3', 'Villa')], max_length=1)),
                ('urban_area_number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22')], max_length=2)),
                ('published', models.BooleanField()),
                ('publish_review', models.CharField(blank=True, max_length=600, null=True)),
                ('consultants_number_allowed', models.SmallIntegerField(default=10)),
                ('allowed_capture_days', models.DurationField(default=10)),
                ('allowed_ad_days', models.DurationField(default=5)),
                ('special', models.BooleanField(default=False)),
                ('city', models.CharField(choices=[('1', 'Tehran')], max_length=1)),
                ('popularity', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('special', models.BooleanField(default=False)),
                ('urban_area_number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22')], max_length=2)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(choices=[('1', 'Tehran')], max_length=1)),
                ('popularity', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('commission_rate', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='ConsultantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.get_image_path)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Consultant')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.get_image_path)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Advertisement')),
            ],
        ),
    ]
