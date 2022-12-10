from django.shortcuts import get_object_or_404
from django.urls import reverse
from webapp.form import ChoiceForm
from webapp.models import Choice, Poll
from django.views.generic import CreateView, UpdateView
# Create your views here.


class ChoiceCreate(CreateView):
    template_name = 'choice/choice_create.html'
    model = Choice
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)


class ChoiceUpdate(UpdateView):
    template_name = 'choice/choice_update.html'
    context_object_name = 'choices'
    model = Choice
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})