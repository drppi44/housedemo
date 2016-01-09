import django_filters
from main.models import Flat, House
from main.models import WC_CHOICES


class FlatFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    area_total = django_filters.RangeFilter()
    area_living = django_filters.RangeFilter()
    kitchen_area = django_filters.RangeFilter()
    wc_type = django_filters.ChoiceFilter(choices=WC_CHOICES)
    owners_count = django_filters.RangeFilter()

    class Meta:
        model = Flat
        fields = [
            'price',
            'level',
            'region',
            'level',
            'max_level',
            'rooms',
            'area_total',
            'area_living',
            'kitchen_area',
            'wc_type',
            'owners_count',
            'town',
            'area'
        ]


class HouseFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    area_total = django_filters.RangeFilter()

    class Meta:
        model = House
        fields = [
            'price',
            'region',
            'town',
            'area',
            'area_total',
        ]
