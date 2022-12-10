from webapp.models import Poll
from django.views.generic import ListView, DetailView
# Create your views here.


class PollIndex(ListView):
    template_name = 'poll/poll_index.html'
    context_object_name = 'polls'
    model = Poll


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll
