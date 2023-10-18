from django import forms

from .models import Category, Note


class NoteForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'custom-select-class'})
    )

    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']


class CategoryFilterForm(forms.Form):
    category_choices = Category.objects.all().values_list('id', 'title')
    category = forms.ChoiceField(
        choices=category_choices,
        required=False,
        label='Оберіть категорію',
        widget=forms.Select(attrs={'class': 'custom-select-class'})
    )
