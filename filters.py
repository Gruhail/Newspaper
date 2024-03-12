import django.forms
from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post


# class PostFilter(FilterSet):
#     #published = DateTimeFilter()
#     class Meta:
#         model = Post
#         fields = {
#             'dateCreation': ['date'],
#             'title': ['icontains'],
#             'text': ['icontains'],
#             'rating': ['lte', 'gte']
#         }

class PostFilter(FilterSet):
    dateCreation = DateFilter(lookup_expr='gt', widget=django.forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    title = CharFilter(
        lookup_expr='icontains',
        widget=django.forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control',
                   'placeholder': 'Enter title',
                   'name': 'title'
                   }
        )
    )
    text = CharFilter(
        lookup_expr='icontains',
        widget=django.forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control'
                   }
        )
    )

    class Meta:
        model = Post
        fields = []