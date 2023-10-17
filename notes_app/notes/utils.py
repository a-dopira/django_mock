from django.urls import reverse_lazy

from notes.forms import NoteForm
from notes.models import Note


class DataMixin:
    model = Note
    template_name = 'notes/note_edition.html'
    form_class = NoteForm
    success_url = reverse_lazy('home')