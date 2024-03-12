from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'categoryType': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }

        def clean(self):
            cleaned_data = super().clean()
            text = cleaned_data.get("text")
            if text is not None and len(text) < 50:
                raise ValidationError({
                    "description": "Описание не может быть менее 20 символов."
                })

            title = cleaned_data.get("title")
            if title == text:
                raise ValidationError(
                    "Описание не должно быть идентично названию."
                )

            return cleaned_data