import os
from uuid import uuid4
from django.db import models
from django.core.validators import RegexValidator

CATEGORY = [
    (u'0', u'اپارتمان'),
    (u'1', u'مسکونی'),
    (u'2', u'اداری'),
    (u'3', u'کلنگی'),
    (u'4', u'سوییت'),
    (u'5', u'ویلا'),
    (u'6', u'تجاری'),
    (u'7', u'زمین'),
    (u'8', u'باغ'),
]

CITY = [
    (u"1", "Tehran"),
]

URBANAREANUMBER = [
    (u'1', u'1'),
    (u'2', u'2'),
    (u'3', u'3'),
    (u'4', u'4'),
    (u'5', u'5'),
    (u'6', u'6'),
    (u'7', u'7'),
    (u'8', u'8'),
    (u'9', u'9'),
    (u'10', u'10'),
    (u'11', u'11'),
    (u'12', u'12'),
    (u'13', u'13'),
    (u'14', u'14'),
    (u'15', u'15'),
    (u'16', u'16'),
    (u'17', u'17'),
    (u'18', u'18'),
    (u'19', u'19'),
    (u'20', u'20'),
    (u'21', u'21'),
    (u'22', u'22'),
]

GENERAL = u"0"
DESIRED = u"1"
POWER = [
    (GENERAL, u"general"),
    (DESIRED, u"desired"),
]

POPULARITY = [
    (u"0", u"0"),
    (u"1", u"1"),
    (u"2", u"2"),
    (u"3", u"3"),
    (u"4", u"4"),
]

EXPOSUREDIRECTION = [
    (u"0", u"شمالی"),
    (u"1", u"جنوبی"),
    (u"2", u"شرقی"),
    (u"3", u"غربی"),
    (u"4", u"تمام جهات"),
]

BILLSTATE = [
    (u"0", u"شخصی"),
    (u"1", u"مسکونی"),
    (u"2", u"اداری"),
    (u"3", u"تجاری"),
    (u"4", u"صنعتی"),
    (u"5", u"تجاری صنعتی"),
    (u"6", u"قولنامه ای"),
    (u"7", u"تعاونی"),
    (u"8", u"اوقافی"),
    (u"9", u"سرقفلی"),
    (u"10", u"بنیادی"),
    (u"11", u"وکالتی"),
    (u"12", u"مبابعه نامه"),
    (u"13", u"صلح نامه ای"),
    (u"14", u"بنچاق"),
    (u"15", u"زمین شهری"),
    (u"16", u"منگوله دار"),
    (u"17", u"دست اول"),
    (u"18", u"قراردادی"),
    (u"19", u"در دست اقدام"),
    (u"20", u"اماده محضر"),
    (u"21", u"باغچه"),
    (u"22", u"کشاورزی"),
    (u"23", u"مشاع"),
    (u"24", u"شهرداری"),
    (u"25", u"بیت رهبری"),
    (u"26", u"اعیان"),
    (u"27", u"صنایع دفاع"),
    (u"28", u"کارگاهی"),
    (u"29", u"اموزشی"),
    (u"30", u"سازمانی"),
    (u"31", u"ستاد اجرایی"),
    (u"32", u"برگه حاکم"),
]

TOILETTYPE = [
    (u"0", u"ایرانی"),
    (u"1", u"فرنگی"),
    (u"2", u"هردو"),
]

BUILDINGVIEW = [
    (u"0", u"سنگ"),
    (u"1", u"ترکیبی"),
    (u"2", u"اجر نما"),
    (u"3", u"کامپوزیت"),
    (u"4", u"سیمان"),
    (u"5", u"سیمان سفید"),
    (u"6", u"سیمان رنگی"),
    (u"7", u"گرانیت"),
    (u"8", u"اجر سه سانت"),
    (u"9", u"اجر سفال"),
    (u"10", u"اجر گزی"),
    (u"11", u"سنگ و شیشه"),
    (u"12", u"شیشه رفرکس"),
    (u"13", u"شیشه سکوریت"),
    (u"14", u"الومینیوم"),
    (u"15", u"تراورنن"),
    (u"16", u"سرامیک"),
    (u"17", u"چوب"),
    (u"18", u"کنتکس"),
    (u"19", u"رومالین"),
    (u"20", u"الویایل"),
    (u"21", u"گرالولیت"),
]

BUILDINGSTATUS = [
    (u"0", u"تخلیه"),
    (u"1", u"اجاره"),
    (u"2", u"سکونت مالک"),
    (u"3", u"واگذار شده"),
    (u"4", u"در حال ساخت"),
]

CABINETTYPE = [
    (u"0", u"ندارد"),
    (u"1", u"ناشمخص"),
    (u"2", u"به انتخاب"),
    (u"3", u"ام دی اف"),
    (u"4", u"مایگلاس"),
    (u"5", u"فلزی"),
    (u"6", u"تمام چوب"),
    (u"7", u"اچ دی اف"),
    (u"8", u"ملامینه"),
    (u"9", u"بلی وود"),
    (u"10", u"پی وی سی"),
    (u"11", u"نیوپان"),
    (u"12", u"چوبی فلزی"),
    (u"13", u"سنگ"),
    (u"14", u"فرومیکا"),
    (u"15", u"فایبرگلاس"),
]

FLOORTYPE = [
    (u"0", u"سرامیک"),
    (u"1", u"موازیک"),
    (u"2", u"پارکت"),
]

YEARS = [
    (u'1', u'1398'),
    (u'2', u'1397'),
    (u'3', u'1396'),
    (u'4', u'1395'),
    (u'5', u'1394'),
    (u'6', u'1393'),
    (u'7', u'1392'),
    (u'8', u'1391'),
    (u'9', u'1390'),
    (u'10', u'1389'),
    (u'11', u'1387'),
    (u'12', u'1386'),
    (u'13', u'1385'),
    (u'14', u'1384'),
    (u'15', u'1383'),
    (u'16', u'1382'),
    (u'17', u'1381'),
    (u'18', u'1380'),
    (u'19', u'1379'),
    (u'20', u'1378'),
    (u'21', u'1377'),
    (u'22', u'1376'),
    (u'23', u'1375'),
    (u'24', u'1374'),
    (u'25', u'1373'),
    (u'26', u'1372'),
    (u'27', u'1371'),
    (u'28', u'1370'),
]

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


def get_image_path(instance, filename):
    id = uuid4()
    return os.path.join('Images', str(id), filename)


class AdvertisementImage(models.Model):
    advertisement = models.ForeignKey(
                        "Advertisement",
                        on_delete=models.CASCADE,
                    )
    image = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                    )

    def __str__(self):
        return str(self.id)


class Advertisement(models.Model, ):
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان اگهی'
        )
    address = models.CharField(
        max_length=300,
        verbose_name='ادزس',
        null=True,
        blank=True,
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ساخت'
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ اخرین اپدیت'
        )
    year_of_construction = models.CharField(
        max_length=2,
        choices=YEARS,
        verbose_name='سال ساخت',
        null=True,
        blank=True,
        )
    room_number = models.PositiveSmallIntegerField(
        verbose_name='تعداد اتاف',
        null=True,
        blank=True,
        )
    house_square = models.PositiveSmallIntegerField(
        verbose_name='متراژ',
        null=True,
        blank=True,
        )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY,
        verbose_name='دسته',
        null=True,
        blank=True,
        )
    urban_area_number = models.CharField(
        max_length=2,
        choices=URBANAREANUMBER,
        verbose_name='منطقه',
        null=True,
        blank=True,
        )
    published = models.BooleanField(
        verbose_name='منتشرشده',
        default=False,
        )
    publish_review = models.CharField(
        max_length=600,
        null=True,
        blank=True,
        verbose_name='نظر منتشرکننده'
        )
    consultants_number_allowed = models.SmallIntegerField(
        default=10,
        verbose_name='تعداد مشاورین مجاز برای دریافت اگهی',
        )
    allowed_capture_days = models.PositiveSmallIntegerField(
        default=10,
        verbose_name = 'روزهای مجاز داشتن اگهی',
        )
    allowed_ad_days = models.PositiveSmallIntegerField(
        default=5,
        verbose_name = 'روزهای مجاز نمایش اگهی',
        )
    special = models.BooleanField(
        default=False,
        verbose_name='اگهی ویژه'
        )
    city = models.CharField(
        max_length=1,
        choices=CITY,
        verbose_name='شهر',
        null=True,
        blank=True,
        )
    popularity = models.CharField(
        max_length=1,
        choices=POPULARITY,
        verbose_name='محبوبیت',
        null=True,
        blank=True,
        )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        verbose_name='موبایل',
    )
    price = models.IntegerField(
        verbose_name='قیمت',
        null=True,
        blank=True,
        )
    price_square = models.IntegerField(
        verbose_name='قیمت متر مربع',
        null=True,
        blank=True,
        )
    floor_number = models.PositiveSmallIntegerField(
        verbose_name='شماره طبقه',
        null=True,
        blank=True,
        )
    floors = models.PositiveSmallIntegerField(
        verbose_name='تعداد طبقات',
        null=True,
        blank=True,
        )
    blocks_per_floor = models.PositiveSmallIntegerField(
        verbose_name='تعداد واحد هر طبقه',
        null=True,
        blank=True,
        )
    yard = models.PositiveSmallIntegerField(
        verbose_name='متراژ حیاط',
        null=True,
        blank=True,
        )
    exposure_direction = models.CharField(
        max_length=1,
        choices=EXPOSUREDIRECTION,
        verbose_name="جهت نوردهی",
        null=True,
        blank=True,
        )
    deposit = models.IntegerField(
        verbose_name='رهن',
        null=True,
        blank=True,
        )
    rent = models.IntegerField(
        verbose_name='اجاره',
        null=True,
        blank=True,
        )
    bill_status = models.CharField(
        max_length=2,
        verbose_name='وضعیت سند',
        choices=BILLSTATE,
        null=True,
        blank=True,
        )
    density = models.IntegerField(
        verbose_name='تراکم',
        null=True,
        blank=True,
        )
    length = models.IntegerField(
        verbose_name='طول بر',
        null=True,
        blank=True,
        )
    agricultural_Type = models.CharField(
        max_length=200,
        verbose_name='نوع کاشت',
        null=True,
        blank=True,
        )
    tree_ages = models.IntegerField(
        verbose_name='عمر درختان',
        null=True,
        blank=True,
        )
    water_quota = models.IntegerField(
        verbose_name='سهمیه اب',
        null=True,
        blank=True,
        )
    toilet_type = models.CharField(
        max_length=1,
        choices=TOILETTYPE,
        verbose_name="نوع توالت",
        null=True,
        blank=True,
        )
    telephone_lines = models.PositiveSmallIntegerField(
        verbose_name='تعداد خط تلفن',
        null=True,
        blank=True,
        )
    building_view = models.CharField(
        max_length=2,
        choices=BUILDINGVIEW,
        verbose_name="نما ساختمان",
        null=True,
        blank=True,
        )
    building_status = models.CharField(
        max_length=1,
        choices=BUILDINGSTATUS,
        verbose_name="وضعیت ملک",
        null=True,
        blank=True,
    )
    cabinet_type = models.CharField(
        max_length=2,
        choices=CABINETTYPE,
        verbose_name="نوع کابینت",
        null=True,
        blank=True,
    )
    flooring_type = models.CharField(
        max_length=1,
        choices=FLOORTYPE,
        verbose_name="کفپوش",
        null=True,
        blank=True,
    )
    parking = models.BooleanField(
        default=False,
        verbose_name="پارکینگ",
        )
    elevator = models.BooleanField(
        default=False,
        verbose_name="اسانسور",
        )
    depot = models.BooleanField(
        default=False,
        verbose_name="انباری",
        )
    sauna = models.BooleanField(
        default=False,
        verbose_name="سونا",
        )
    jacuzzi = models.BooleanField(
        default=False,
        verbose_name="جکوزی",
        )
    swimming_pool = models.BooleanField(
        default=False,
        verbose_name="استخر",
        )
    balcony = models.BooleanField(
        default=False,
        verbose_name="بالکون",
        )
    kitchen = models.BooleanField(
        default=False,
        verbose_name="اشپزخانه",
        )
    lobby = models.BooleanField(
        default=False,
        verbose_name="لابی",
        )
    video_door_phone = models.BooleanField(
        default=False,
        verbose_name="ایفون تصویری",
        )
    remote = models.BooleanField(
        default=False,
        verbose_name="ریموت",
        )
    janitor = models.BooleanField(
        default=False,
        verbose_name="سرایدار",
        )
    table_gas = models.BooleanField(
        default=False,
        verbose_name="گاز رو میزی",
        )
    water_cooler = models.BooleanField(
        default=False,
        verbose_name="کولر ابی",
        )
    air_conditioners = models.BooleanField(
        default=False,
        verbose_name="کولر گازی",
        )
    chiller = models.BooleanField(
        default=False,
        verbose_name="چیلر",
        )
    duct_split = models.BooleanField(
        default=False,
        verbose_name="داکت اسپیلیت",
        )
    package = models.BooleanField(
        default=False,
        verbose_name="پکیج",
        )
    radiant = models.BooleanField(
        default=False,
        verbose_name="شوفاژ",
        )
    heater = models.BooleanField(
        default=False,
        verbose_name="بخاری",
        )
    floor_heating = models.BooleanField(
        default=False,
        verbose_name="گرمایش از کف",
        )
    water = models.BooleanField(
        default=False,
        verbose_name="اب",
        )
    electricity = models.BooleanField(
        default=False,
        verbose_name="برق",
        )
    gas = models.BooleanField(
        default=False,
        verbose_name="گاز",
        )
    water_well = models.BooleanField(
        default=False,
        verbose_name="چاه اب",
        )
    car_door = models.BooleanField(
        default=False,
        verbose_name="درب ماشین رو",
        )
    asphalt = models.BooleanField(
        default=False,
        verbose_name="جاده اسفالت",
        )
    caretaker_house = models.BooleanField(
        default=False,
        verbose_name="خانه سرایدار",
        )

    def __str__(self):
        return self.title
