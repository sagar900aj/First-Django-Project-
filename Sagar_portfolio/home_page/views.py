from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def blog_users(request):
    return HttpResponse("Hello world!")

def home(request):
  template = loader.get_template('Home/home.html')
  return HttpResponse(template.render())

def about_me(request):
  template = loader.get_template('About/about_me.html')
  return HttpResponse(template.render())

def contact_me(request):
  template = loader.get_template('Contact/contact_me.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('Gallery/gallery.html')
  return HttpResponse(template.render())