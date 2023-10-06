from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import NoteForm
from .models import Category


class Categories(ListView):
    template_name = 'notes/notes.html'
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all().prefetch_related('notes')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page is here'
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
