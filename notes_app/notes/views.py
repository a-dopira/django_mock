from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import NoteForm
from .models import Category, Note


class CategoriesList(ListView):
    template_name = 'notes/notes.html'
    model = Category
    context_object_name = 'category'

    def get_queryset(self):
        return get_object_or_404(Category, slug=self.kwargs.get('category_slug'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_queryset().title + ' | Нотатки'
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
    template_name = 'notes/search_result.html'
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


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('simple_view')
    else:
        form = NoteForm()

    context = {
        'form': form,
    }

    return render(request, 'notes/note_create.html', context)
