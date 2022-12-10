from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.TextField(max_length=30, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")


class Choice(models.Model):
    variant = models.TextField(max_length=30, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='polls')
