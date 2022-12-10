from django.urls import reverse

from webapp.models import Poll
from django.views.generic import ListView, DetailView, CreateView
from webapp.form import PollForm
# Create your views here.


class PollIndex(ListView):
    template_name = 'poll/poll_index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = '-created_at'


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll


class PollCreate(CreateView):
    template_name = 'poll/poll_create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_index')
