from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'categoryType': ['exact'],
           'postCategory': ['exact'],
           'author__authorUser': ['exact'],
       }