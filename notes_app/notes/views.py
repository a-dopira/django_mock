from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from .forms import CategoryFilterForm
from .models import Category, Note
from .utils import DataMixin


class CategoriesList(ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(categories__slug=self.kwargs['category_slug']).prefetch_related('categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['category_slug']).title + ' | Нотатки'
        return context


class Categories(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'notes/categories.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context


class FormSearch(ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        query = self.request.GET.get('note_search', '')
        notes = Note.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return notes

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('note_search', '')
        context['title'] = f"Результати пошуку '{query}'"
        context['query'] = query
        return context


class NoteDeletion(DeleteView):
    model = Note
    template_name = 'notes/deletion.html'
    success_url = reverse_lazy('home')


class NoteUpdateView(DataMixin, UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {
            'title': 'Редагування нотатки',
            'header': 'Оновлення нотатки',
            'confirmation': 'Зберегти зміни'
        }
        return context | c_def


class NoteCreateView(DataMixin, CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {
            'title': 'Створення нотатки',
            'header': 'Створення нотатки',
            'confirmation': 'Створити',
        }
        return context | c_def


def note_filter(request):
    form = CategoryFilterForm(request.GET)
    notes = Note.objects.all()

    if form.is_valid() and form.cleaned_data['category']:
        category_id = form.cleaned_data['category']
        notes = notes.filter(categories__id=category_id)

    return render(request, 'notes/notes.html', {'form': form, 'notes': notes})