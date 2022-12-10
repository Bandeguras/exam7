from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import View
from webapp.models import Answer, Poll


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        answer = Answer.objects.all()
        question = answer.question = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context = {
            'answer': answer,
            'question': question
        }
        return render(request, 'answer/answer_add.html', context)

    def post(self, request, *args, **kwargs):
        question = self.kwargs.get('pk')
        variant2 = request.POST.get('choice')
        Answer.objects.create(question_id=question, variant_id=variant2)
        return HttpResponseRedirect(reverse_lazy('poll_index'))



