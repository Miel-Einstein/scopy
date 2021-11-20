from django.contrib.auth import models
from django_filters import CharFilter
import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    content=CharFilter(field_name='content',lookup_expr='icontains')
    class Meta:
        model=Post
        fields=('content',)