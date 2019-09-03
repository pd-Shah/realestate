import os
from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

CATEGORY = [
    (u'0', u'خرید اپارتمان'),
    (u'1', u'فروش اپارتمان'),
    (u'2', u'رهن و اجاره اپارتمان'),
    (u'3', u'خرید اداری'),
    (u'4', u'فروش اداری'),
    (u'5', u'رهن و اجاره اداری'),
    (u'6', u'خرید کلنگی'),
    (u'7', u'فروش کلنگی'),
    (u'8', u'رهن و اجاره کلنگی'),
    (u'9', u'خرید سوییت'),
    (u'10', u'فروش سوییت'),
    (u'11', u'رهن و اجاره سوییت'),
    (u'12', u'خرید ویلا'),
    (u'13', u'فروش ویلا'),
    (u'14', u'رهن و اجاره ویلا'),
    (u'15', u'خرید تجاری'),
    (u'16', u'فروش تجاری'),
    (u'17', u'رهن و اجاره تجاری'),
    (u'18', u'خرید زمین'),
    (u'19', u'فروش زمین'),
    (u'20', u'رهن و اجاره زمین'),
    (u'21', u'خرید باغ'),
    (u'22', u'فروش باغ'),
    (u'23', u'رهن و اجاره باغ'),
    (u'24', u'خرید انبار'),
    (u'25', u'فروش انبار'),
    (u'26', u'رهن و اجاره انبار'),
    (u'27', u'خرید سوله'),
    (u'28', u'فروش سوله'),
    (u'29', u'رهن و اجاره سوله'),
    (u"30", "خرید خانه ویلایی"),
    (u"31", "فروش خانه ویلایی"),
    (u"32", "رهن و اجاره خانه ویلایی"),
    (u"33", "خرید پنت هوس"),
    (u"34", "فروش پنت هوس"),
    (u"35", "رهن و اجاره پنت هوس"),
    (u"36", "خرید مغازه"),
    (u"37", "فروش مغازه"),
    (u"38", "رهن و اجاره مغازه"),
    (u"39", "خرید برج"),
    (u"40", "فروش برج"),
    (u"41", "رهن و اجاره برج"),
    (u"42", "خرید مستغلات"),
    (u"43", "فروش مستغلات"),
    (u"44", "رهن و اجاره مستغلات"),

]

CITY = [
    (u"1", "تهران"),
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

FANCE = [
    (u"0", u"‫سیم‬خاردار"),
    (u"1", u"دیوار"),
    (u"2", u"‫‪‫‪فنس"),
]

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '09226255415'. Up to 15 digits allowed."
)


def get_image_path(instance, filename):
    id = uuid4()
    return os.path.join('Images', str(id), filename)


class ConfigAdvertisement(models.Model):
    name = models.CharField(max_length=100)
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

    def __str__(self):
        return self.name


class Advertisement(models.Model, ):
    uid = models.UUIDField(default=uuid4, editable=False)
    landlord_name = models.CharField(
        max_length=200,
        verbose_name="نام مالک",
        null=True,
        blank=True,
    )
    config = models.OneToOneField(
        ConfigAdvertisement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان اگهی'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name='موبایل',
    )
    urban_area_number = models.CharField(
        max_length=2,
        choices=URBANAREANUMBER,
        verbose_name='منطقه',
        null=True,
        blank=True,
        )
    city = models.CharField(
        max_length=1,
        choices=CITY,
        verbose_name='شهر',
        null=True,
        blank=True,
        )
    quarter = models.CharField(
        max_length=100,
        verbose_name="محله",
        null=True,
        blank=True,
    )
    street = models.CharField(
        max_length=100,
        verbose_name="خیابان فرعی",
        null=True,
        blank=True,
    )
    plak = models.IntegerField(
        verbose_name="شماره پلاک",
        null=True,
        blank=True,
        )
    address = models.CharField(
        max_length=300,
        verbose_name='ادرس',
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
    year_of_construction = models.CharField(
        max_length=2,
        choices=YEARS,
        verbose_name='سال ساخت',
        null=True,
        blank=True,
        )
    room_number = models.PositiveSmallIntegerField(
        verbose_name='تعداد اتاق',
        null=True,
        blank=True,
        )
    bedroom_number = models.SmallIntegerField(
        verbose_name="تعداد اتاق خواب",
        null=True,
        blank=True,
        )
    house_square = models.PositiveSmallIntegerField(
        verbose_name='متراژ',
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
    eslahi = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="اصلاحی",
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
        verbose_name='دسته',
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
    special = models.BooleanField(
        default=False,
        verbose_name='اگهی ویژه'
        )
    popularity = models.CharField(
        max_length=1,
        choices=POPULARITY,
        verbose_name='محبوبیت',
        null=True,
        blank=True,
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
    fance = models.CharField(
        max_length=1,
        choices=FANCE,
        verbose_name='حصار',
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
    image1 = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                        verbose_name="تصویر شماره 1",
                    )
    image2 = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                        verbose_name="تصویر شماره 2",
                    )
    image3 = models.ImageField(
                        upload_to=get_image_path,
                        blank=True,
                        null=True,
                        verbose_name="تصویر شماره 3",
                    )

    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="توضیحات",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advertisement:advertisement_detail', args=[str(self.pk)])
