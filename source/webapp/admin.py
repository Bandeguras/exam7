from django.contrib import admin
from webapp.models import Poll, Choice, Answer
# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['variant']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['pk']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
