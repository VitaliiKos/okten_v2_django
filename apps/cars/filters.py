from django_filters import rest_framework as filters

from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    year_gte = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lte = filters.NumberFilter(field_name='year', lookup_expr='lt')
    year_exact = filters.NumberFilter(field_name='year', lookup_expr='exact')

    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='brand', lookup_expr='endswith')
    brand_contains = filters.CharFilter(field_name='brand', lookup_expr='contains')

    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_exact = filters.NumberFilter(field_name='price', lookup_expr='exact')

    class Meta:
        model = CarModel
        fields = (
            'year_gte', 'year_lte', 'year_exact', 'brand_start', 'brand_end', 'brand_contains', 'price_gte', 'price_lte',
            'price_exact')
