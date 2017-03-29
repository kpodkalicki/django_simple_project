from django.views.generic import DetailView
from django.views.generic import ListView

from notes.models import Note


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note
