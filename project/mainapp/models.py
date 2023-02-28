from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Service(models.Model):
    title = models.CharField('Заголовок', max_length=100, unique=True)
    text = models.TextField('Текст')


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Текст статьи')
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
