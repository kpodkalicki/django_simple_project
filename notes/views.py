from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from notes.models import Note


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body']


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'body']


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
