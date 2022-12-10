"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import PollIndex, PollView, PollCreate, PollUpdate, PollDelete, ChoiceCreate, ChoiceUpdate, ChoiceDelete, AnswerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollIndex.as_view(), name='poll_index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll'),
    path('poll/create/', PollCreate.as_view(), name='poll_create'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),

    path('poll/<int:pk>/create/choice/', ChoiceCreate.as_view(), name='choice_create'),
    path('choice/<int:pk>/update/', ChoiceUpdate.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name='choice_delete'),
    path('answer/<int:pk>/', AnswerView.as_view(), name='answer_add'),

]
