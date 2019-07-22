
from django.forms import ModelForm
from .models import Advertisement


class RentApartment(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "building_view",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "table_gas",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
            "image1",
            "image2",
            "image3",
        )


class SellBuyApartment(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "price",
            "price_square",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "exposure_direction",
            "bill_status",
            "density",
            "toilet_type",
            "building_view",
            "cabinet_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "table_gas",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
            )


class RentEdari(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "address",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "telephone_lines",
            "building_view",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "video_door_phone",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
        )


class SellBuyEdari(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "address",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "price",
            "price_square",
            "exposure_direction",
            "toilet_type",
            "telephone_lines",
            "building_view",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "video_door_phone",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
        )


class RentColangi(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "yard",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "building_view",
            "building_status",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "video_door_phone",
            "remote",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
            )


class SellBuyColangi(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "yard",
            "exposure_direction",
            "price",
            "price_square",
            "toilet_type",
            "building_view",
            "building_status",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "video_door_phone",
            "remote",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
            )


class RentSuit(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "urban_area_number",
            "city",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "building_view",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "table_gas",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
        )


class SellBuySuit(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "urban_area_number",
            "city",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "exposure_direction",
            "price",
            "price_square",
            "bill_status",
            "toilet_type",
            "building_view",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "table_gas",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
        )


class RentVila(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "urban_area_number",
            "city",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "floors",
            "yard",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "building_view",
            "building_status",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "janitor",
            "table_gas",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
            "car_door",
            "caretaker_house",
        )


class SellBuyVila(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "urban_area_number",
            "city",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "floors",
            "yard",
            "exposure_direction",
            "price",
            "price_square",
            "bill_status",
            "toilet_type",
            "building_view",
            "building_status",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "janitor",
            "table_gas",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
            "car_door",
            "caretaker_house",
        )


class RentTejari(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "urban_area_number",
            "city",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "category",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "yard",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "telephone_lines",
            "building_view",
            "building_status",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "janitor",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
        )


class SellBuyTejari(ModelForm):
    class Meta:
        model = Advertisement
        fields = (
            "title",
            "phone_number",
            "urban_area_number",
            "city",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "category",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "yard",
            "exposure_direction",
            "price",
            "price_square",
            "bill_status",
            "toilet_type",
            "telephone_lines",
            "building_view",
            "building_status",
            "cabinet_type",
            "flooring_type",
            "parking",
            "elevator",
            "depot",
            "sauna",
            "jacuzzi",
            "swimming_pool",
            "balcony",
            "kitchen",
            "lobby",
            "video_door_phone",
            "remote",
            "janitor",
            "water_cooler",
            "air_conditioners",
            "chiller",
            "duct_split",
            "package",
            "radiant",
            "heater",
            "floor_heating",
        )


class RentZamin(ModelForm):
    class Meta:
        model = Advertisement
        fields = (

        )


class SellBuyZamin(ModelForm):
    class Meta:
        model = Advertisement
        fields = (

        )


class RentBagh(ModelForm):
    class Meta:
        model = Advertisement
        fields = (

        )


class SellBuyBagh(ModelForm):
    class Meta:
        model = Advertisement
        fields = (

        )


class RentAnbar(ModelForm):
    class Meta:
        model = Advertisement
        fields = (

        )


class SellBuyAnbar(ModelForm):
    class Meta:
        model = Advertisement
        fields = (

        )
