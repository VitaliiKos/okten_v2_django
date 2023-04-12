from django_filters import rest_framework as filters


class AutoParkFilter(filters.FilterSet):
    park_name_start = filters.CharFilter(field_name='name', lookup_expr='istartswith')
    park_name_end = filters.CharFilter(field_name='name', lookup_expr='endswith')
    park_name_contains = filters.CharFilter(field_name='name', lookup_expr='contains')

    cars_year_lt = filters.NumberFilter(field_name='cars__year', lookup_expr='lt', distinct=True)
