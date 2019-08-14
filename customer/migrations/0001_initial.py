# Generated by Django 2.0 on 2019-08-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisement', '0003_advertisement_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=17, verbose_name='شماره تلفن')),
                ('favorites', models.ManyToManyField(related_name='favorited_by', to='advertisement.Advertisement')),
            ],
        ),
    ]
