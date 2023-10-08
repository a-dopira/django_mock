from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import NoteForm
from .models import Category


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
        categories = Category.objects.all()
        return categories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
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
