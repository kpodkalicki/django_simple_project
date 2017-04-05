from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'body']

    def test_func(self):
        return self.request.user == self.get_object().created_by


class NoteDelete(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def test_func(self):
        return self.request.is_superuser or self.request.user == self.object.created_by


