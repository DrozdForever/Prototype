from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),

    path('news/', views.NewsView.as_view(), name='news'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<str:username>', views.UserNewsView.as_view(), name='user-news'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
]
