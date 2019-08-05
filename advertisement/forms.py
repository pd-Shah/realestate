
from django.forms import ModelForm
from .models import Advertisement


class RentApartment(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "telephone_lines",
            "floor_number",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "building_view",
            "cabinet_type",
            "building_status",
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

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "deposit",
            "rent",
            "telephone_lines",
        }


class SellBuyApartment(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
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
            "building_status",
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
            "image1",
            "image2",
            "image3",
            )
        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "price",
            "price_square",
        }


class RentEdari(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "floors",
            "blocks_per_floor",
            "telephone_lines",
            "exposure_direction",
            "deposit",
            "rent",
            "toilet_type",
            "telephone_lines",
            "building_view",
            "cabinet_type",
            "building_status",
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
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "deposit",
            "rent",
            "telephone_lines",
        }


class SellBuyEdari(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
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
            "building_status",
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
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "telephone_lines",
            "price",
            "price_square",
        }


class RentColangi(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "telephone_lines",
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
            "image1",
            "image2",
            "image3",
            )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "deposit",
            "rent",
            "telephone_lines",
        }


class SellBuyColangi(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "year_of_construction",
            "room_number",
            "house_square",
            "urban_area_number",
            "city",
            "floor_number",
            "telephone_lines",
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
            "image1",
            "image2",
            "image3",
            )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "telephone_lines",
            "price",
            "price_square",
        }


class RentSuit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "urban_area_number",
            "city",
            "year_of_construction",
            "telephone_lines",
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
            "building_status",
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

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "deposit",
            "rent",
            "telephone_lines",
        }


class SellBuySuit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "urban_area_number",
            "city",
            "year_of_construction",
            "telephone_lines",
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
            "building_status",
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

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "telephone_lines",
            "price",
            "price_square",
        }


class RentVila(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "city",
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
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "deposit",
            "rent",
        }


class SellBuyVila(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "urban_area_number",
            "city",
            "year_of_construction",
            "telephone_lines",
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
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "price",
            "price_square",
        }


class RentTejari(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "city",
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
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "deposit",
            "rent",
            "telephone_lines",
        }


class SellBuyTejari(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "city",
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
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "floor_number",
            "telephone_lines",
            "price",
            "price_square",
        }


class RentZamin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "building_status",
            "house_square",
            "yard",
            "deposit",
            "rent",
            "length",
            "water_quota",
            "swimming_pool",
            "video_door_phone",
            "janitor",
            "water",
            "electricity",
            "gas",
            "water_well",
            "car_door",
            "asphalt",
            "caretaker_house",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "deposit",
            "rent",
        }


class SellBuyZamin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "building_status",
            "house_square",
            "yard",
            "price",
            "price_square",
            "bill_status",
            "length",
            "density",
            "water_quota",
            "swimming_pool",
            "video_door_phone",
            "janitor",
            "water",
            "electricity",
            "gas",
            "water_well",
            "car_door",
            "asphalt",
            "caretaker_house",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "house_square",
            "price",
            "price_square",
        }


class RentBagh(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "eslahi",
            "fance",
            "urban_area_number",
            "city",
            "address",
            "house_square",
            "yard",
            "deposit",
            "rent",
            "bill_status",
            "length",
            "agricultural_Type",
            "tree_ages",
            "water_quota",
            "building_status",
            "swimming_pool",
            "video_door_phone",
            "janitor",
            "water",
            "electricity",
            "gas",
            "water_well",
            "car_door",
            "asphalt",
            "caretaker_house",
            "image1",
            "image2",
            "image3",
        )
        required = {
            "landlord_name",
            "title",
            "phone_number",
            "deposit",
            "rent",
        }


class SellBuyBagh(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "eslahi",
            "fance",
            "urban_area_number",
            "city",
            "address",
            "house_square",
            "yard",
            "price",
            "price_square",
            "bill_status",
            "length",
            "agricultural_Type",
            "tree_ages",
            "water_quota",
            "building_status",
            "swimming_pool",
            "video_door_phone",
            "janitor",
            "water",
            "electricity",
            "gas",
            "water_well",
            "car_door",
            "asphalt",
            "caretaker_house",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "price",
            "price_square",
        }


class RentAnbar(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "year_of_construction",
            "room_number",
            "house_square",
            "deposit",
            "rent",
            "building_status",
            "parking",
            "elevator",
            "janitor",
            "water",
            "electricity",
            "gas",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "deposit",
            "rent",
        }


class SellBuyAnbar(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "year_of_construction",
            "room_number",
            "house_square",
            "price",
            "price_square",
            "building_status",
            "parking",
            "elevator",
            "janitor",
            "water",
            "electricity",
            "gas",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "price",
            "price_square",
        }


class RentSole(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "year_of_construction",
            "house_square",
            "deposit",
            "rent",
            "bill_status",
            "building_status",
            "water",
            "electricity",
            "gas",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "deposit",
            "rent",
        }


class SellBuySole(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Advertisement
        fields = (
            "landlord_name",
            "title",
            "phone_number",
            "quarter",
            "street",
            "plak",
            "address",
            "urban_area_number",
            "year_of_construction",
            "house_square",
            "price",
            "price_square",
            "bill_status",
            "building_status",
            "water",
            "electricity",
            "gas",
            "image1",
            "image2",
            "image3",
        )

        required = {
            "landlord_name",
            "title",
            "phone_number",
            "price",
            "price_square",
        }
