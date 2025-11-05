from django.urls import path
from . import views

urlpatterns = [
    path('blog-users/', views.blog_users, name='blog-users'),
    path('', views.home, name='home'),  
    path('home/', views.home, name='Home-page'),
    path('about_me/', views.about_me, name='about_me'),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('gallery/', views.gallery, name='gallery'),
]
