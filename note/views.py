from .models import Category, Note
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NoteForm, CategoryForm


class NoteDetail(DetailView):
    model = Note
    template_name = 'note/detail.html'


class NoteUpdate(UpdateView):
    model = Note
    template_name = 'note/update.html'
    form_class = NoteForm

    def get_success_url(self):
        note = self.kwargs['pk']
        return reverse_lazy('note:detail', args=(note,))


class NoteDelete(DeleteView):
    model = Note
    template_name = 'note/delete.html'
    success_url = reverse_lazy('collection:calendar')


class CreateNote(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note/create.html'
    success_url = reverse_lazy('collection:calendar')
    form_class = NoteForm
    login_url = '../../login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FavoriteNote(LoginRequiredMixin, ListView):
    model = Note
    paginate_by = 10
    template_name = 'note/favorite.html'
    login_url = '../../login/'

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'note/create.html'
    success_url = reverse_lazy('collection:calendar')
    form_class = CategoryForm
    login_url = '../../login/'
