from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    AdvertisementListViewMap,
    AboutUsView,
    SelectAddView,
    NewBuyApartment,
    NewSellApartment,
    NewRentApartment,
    NewBuyEdari,
    NewSellEdari,
    NewRentEdari,
    NewBuyColangi,
    NewSellColangi,
    NewRentColangi,
    NewBuySuit,
    NewSellSuit,
    NewRentSuit,
    NewBuyVila,
    NewSellVila,
    NewRentVila,
    NewBuyTejari,
    NewSellTejari,
    NewRentTejari,
    NewBuyZamin,
    NewSellZamin,
    NewRentZamin,
    NewBuyBagh,
    NewSellBagh,
    NewRentBagh,
    NewBuyAnbar,
    NewSellAnbar,
    NewRentAnbar,
    NewBuySole,
    NewSellSole,
    NewRentSole,
    ContactUsView,
    MyPageView,
    BuyApartmentListView,
    SellApartmentListView,
    RentApartmentListView,
    BuyEdariListView,
    SellEdariListView,
    RentEdariListView,
    BuyColangiListView,
    SellColangiListView,
    RentColangiListView,
    BuySuitListView,
    SellSuitListView,
    RentSuitListView,
    BuyVilaListView,
    SellVilaListView,
    RentVilaListView,
    BuyTejariListView,
    SellTejariListView,
    RentTejariListView,
    BuyZaminListView,
    SellZaminListView,
    RentZaminListView,
    BuyBaghListView,
    SellBaghListView,
    RentBaghListView,
    BuyAnbarListView,
    SellAnbarListView,
    RentAnbarListView,
    BuySoleListView,
    RentSoleListView,
    SellSoleListView,
)

app_name = 'advertisement'
urlpatterns = [
    path(
        'contact-us',
        ContactUsView.as_view(),
        name='contact_us'
    ),
    path(
        'my-page',
        MyPageView.as_view(),
        name='my_page'
    ),
    path(
        '',
        AdvertisementListView.as_view(),
        name="advertisement_list"
    ),
    path(
        '<int:pk>',
        AdvertisementDetailView.as_view(),
        name='advertisement_detail'
    ),
    path(
        'map/',
        AdvertisementListViewMap.as_view(),
        name="advertisement_list_map"
    ),
    path(
        'about-us/',
        AboutUsView.as_view(),
        name='about_us'
    ),
    path(
        'select/',
        SelectAddView.as_view(),
        name='select_ad'
    ),
    path(
        'new-buy-apartment/',
        NewBuyApartment.as_view(),
        name='new_buy_apartment',
    ),
    path(
        'select/new-sell-apartment/',
        NewSellApartment.as_view(),
        name='new_sell_apartment',
    ),
    path(
        'select/new-rent-apartment/',
        NewRentApartment.as_view(),
        name='new_rent_apartment',
    ),
    path(
        'select/new-buy-edari/',
        NewBuyEdari.as_view(),
        name='new_buy_edari',
    ),
    path(
        'select/new-sell-edari/',
        NewSellEdari.as_view(),
        name='new_sell_edari',
    ),
    path(
        'select/new-rent-edari/',
        NewRentEdari.as_view(),
        name='new_rent_edari',
    ),
    path(
        'select/new-buy-colangi/',
        NewBuyColangi.as_view(),
        name='new_buy_colangi',
    ),
    path(
        'select/new-sell-colangi/',
        NewSellColangi.as_view(),
        name='new_sell_colangi',
    ),
    path(
        'select/new-rent-colangi/',
        NewRentColangi.as_view(),
        name='new_rent_colangi',
    ),
    path(
        'select/new-buy-suit/',
        NewBuySuit.as_view(),
        name='new_buy_suit',
    ),
    path(
        'select/new-sell-suit/',
        NewSellSuit.as_view(),
        name='new_sell_suit',
    ),
    path(
        'select/new-rent-suit/',
        NewRentSuit.as_view(),
        name='new_rent_suit',
    ),
    path(
        'select/new-buy-vila/',
        NewBuyVila.as_view(),
        name='new_buy_vila',
    ),
    path(
        'select/new-sell-vila/',
        NewSellVila.as_view(),
        name='new_sell_vila',
    ),
    path(
        'select/new-rent-vila/',
        NewRentVila.as_view(),
        name='new_rent_vila',
    ),
    path(
        'select/new-buy-tejari/',
        NewBuyTejari.as_view(),
        name='new_buy_tejari',
    ),
    path(
        'select/new-sell-tejari/',
        NewSellTejari.as_view(),
        name='new_sell_tejari',
    ),
    path(
        'select/new-rent-tejari/',
        NewRentTejari.as_view(),
        name='new_rent_tejari',
    ),
    path(
        'select/new-buy-zamin/',
        NewBuyZamin.as_view(),
        name='new_buy_zamin',
    ),
    path(
        'select/new-sell-zamin/',
        NewSellZamin.as_view(),
        name='new_sell_zamin',
    ),
    path(
        'select/new-rent-zamin/',
        NewRentZamin.as_view(),
        name='new_rent_zamin',
    ),
    path(
        'select/new-buy-bagh/',
        NewBuyBagh.as_view(),
        name='new_buy_bagh',
    ),
    path(
        'select/new-sell-bagh/',
        NewSellBagh.as_view(),
        name='new_sell_bagh',
    ),
    path(
        'select/new-rent-bagh/',
        NewRentBagh.as_view(),
        name='new_rent_bagh',
    ),
    path(
        'select/new-buy-anbar/',
        NewBuyAnbar.as_view(),
        name='new_buy_anbar',
    ),
    path(
        'select/new-sell-anbar/',
        NewSellAnbar.as_view(),
        name='new_sell_anabr',
    ),
    path(
        'select/new-rent-anbar/',
        NewRentAnbar.as_view(),
        name='new_rent_anbar',
    ),
    path(
        'select/new-buy-sole/',
        NewBuySole.as_view(),
        name='new_buy_sole',
    ),
    path(
        'select/new-sell-sole/',
        NewSellSole.as_view(),
        name='new_sell_sole',
    ),
    path(
        'select/new-rent-sole/',
        NewRentSole.as_view(),
        name='new_rent_sole',
    ),
    path(
        'buy-apartment/',
        BuyApartmentListView.as_view(),
        name='buy_apartment_list_view'
    ),
    path(
        'sell-apartment/',
        SellApartmentListView.as_view(),
        name='sell_apartment_list_view'
    ),
    path(
        'rent-apartment/',
        RentApartmentListView.as_view(),
        name='rent_apartment_list_view'
    ),
    path(
        'buy-edari/',
        BuyEdariListView.as_view(),
        name='buy_edari_list_view'
    ),
    path(
        'sell-edari/',
        SellEdariListView.as_view(),
        name='sell_edari_list_view'
    ),
    path(
        'rent-edari/',
        RentEdariListView.as_view(),
        name='rent_edari_list_view'
    ),
    path(
        'buy-colangi/',
        BuyColangiListView.as_view(),
        name='buy_colangi_list_view'
    ),
    path(
        'sell-colangi/',
        SellColangiListView.as_view(),
        name='sell_colangi_list_view'
    ),
    path(
        'rent-colangi/',
        RentColangiListView.as_view(),
        name='rent_colangi_list_view'
    ),
    path(
        'buy-suit/',
        BuySuitListView.as_view(),
        name='buy_suit_list_view'
    ),
    path(
        'sell-suit/',
        SellSuitListView.as_view(),
        name='sell_suit_list_view'
    ),
    path(
        'rent-suit/',
        RentSuitListView.as_view(),
        name='rent_suit_list_view'
    ),
    path(
        'buy-vila/',
        BuyVilaListView.as_view(),
        name='buy_vila_list_view'
    ),
    path(
        'sell-vila/',
        SellVilaListView.as_view(),
        name='sell_vila_list_view'
    ),
    path(
        'rent-vila/',
        RentVilaListView.as_view(),
        name='rent_vila_list_view'
    ),
    path(
        'buy-tejari/',
        BuyTejariListView.as_view(),
        name='buy_tejari_list_view'
    ),
    path(
        'sell-tejari/',
        SellTejariListView.as_view(),
        name='sell_tejari_list_view'
    ),
    path(
        'rent-tejari/',
        RentTejariListView.as_view(),
        name='rent_tejari_list_view'
    ),
    path(
        'buy-zamin/',
        BuyZaminListView.as_view(),
        name='buy_zamin_list_view'
    ),
    path(
        'sell-zamin/',
        SellZaminListView.as_view(),
        name='sell_zamin_list_view'
    ),
    path(
        'rent-zamin/',
        RentZaminListView.as_view(),
        name='rent_zamin_list_view'
    ),
    path(
        'buy-bagh/',
        BuyBaghListView.as_view(),
        name='buy_bagh_list_view'
    ),
    path(
        'sell-bagh/',
        SellBaghListView.as_view(),
        name='sell_bagh_list_view'
    ),
    path(
        'rent-bagh/',
        RentBaghListView.as_view(),
        name='rent_bagh_list_view'
    ),
    path(
        'buy-anbar/',
        BuyAnbarListView.as_view(),
        name='buy_anbar_list_view'
    ),
    path(
        'sell-anbar/',
        SellAnbarListView.as_view(),
        name='sell_anbar_list_view'
    ),
    path(
        'rent-anabr/',
        RentAnbarListView.as_view(),
        name='rent_anbar_list_view'
    ),
    path(
        'buy-sole/',
        BuySoleListView.as_view(),
        name='buy_sole_list_view'
    ),
    path(
        'sell-sole/',
        SellSoleListView.as_view(),
        name='sell_sole_list_view'
    ),
    path(
        'rent-sole/',
        RentSoleListView.as_view(),
        name='rent_sole_list_view'
    ),
]
