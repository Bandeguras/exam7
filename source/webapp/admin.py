from django.contrib import admin
from webapp.models import Poll, Choice
# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['variant']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
