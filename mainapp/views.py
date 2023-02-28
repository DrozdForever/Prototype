from .models import Service, News
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def services(request):
    data = {
        'text': Service.objects.all(),
    }
    return render(request, 'mainapp/services.html', data)


class NewsView(ListView):
    model = News
    template_name = 'mainapp/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(NewsView, self).get_context_data(**kwards)
        return ctx


class UserNewsView(ListView):
    model = News
    template_name = 'mainapp/user_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserNewsView, self).get_context_data(**kwards)
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'mainapp/news-detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'mainapp/news-add.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавить статью'
        ctx['btn_text'] = 'Добавить статью'
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'mainapp/news-add.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновить статью'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'mainapp/news-delete.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


def main(request):
    return render(request, 'mainapp/main.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
