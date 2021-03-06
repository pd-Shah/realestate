# Generated by Django 2.0 on 2019-08-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='bedroom_number',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='تعداد اتاق خواب'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='eslahi',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='اصلاحی'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='fance',
            field=models.CharField(blank=True, choices=[('0', '\u202bسیم\u202cخاردار'), ('1', 'دیوار'), ('2', '\u202b\u202a\u202b\u202aفنس')], max_length=1, null=True, verbose_name='حصار'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='landlord_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام مالک'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='plak',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره پلاک'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='quarter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='محله'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='خیابان فرعی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='ادرس'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='room_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='تعداد اتاق'),
        ),
    ]
