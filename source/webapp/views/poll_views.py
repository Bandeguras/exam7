from webapp.models import Poll
from django.views.generic import ListView
# Create your views here.


class PollIndex(ListView):
    template_name = 'poll/poll_index.html'
    context_object_name = 'polls'
    model = Poll
