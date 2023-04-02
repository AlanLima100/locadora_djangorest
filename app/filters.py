from django_filters import rest_framework as filters
from django.utils import timezone


class DateFilter(filters.CharFilter):
    """
    Filtra um campo de data e hora para exibir no formato brasileiro.
    """
    def filter(self, queryset, value):
        if not value:
            return queryset
        try:
            date = timezone.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            return queryset
        date_start = timezone.make_aware(date, timezone.get_current_timezone()).date()
        date_end = date_start + timezone.timedelta(days=1)
        return queryset.filter(**{'%s__range' % self.field_name: (date_start, date_end)})

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'range')
        super().__init__(*args, **kwargs)
