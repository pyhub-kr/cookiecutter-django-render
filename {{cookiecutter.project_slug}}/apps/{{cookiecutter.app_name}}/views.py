from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'base.html', {
        'title': 'Welcome to {{cookiecutter.project_name}}',
        'content': 'Django project ready for Render.com deployment'
    })


def about(request):
    return render(request, '{{cookiecutter.app_name}}/about.html', {
        'title': 'About - {{cookiecutter.author_name}}',
        'author_name': '{{cookiecutter.author_name}}',
        'author_email': '{{cookiecutter.author_email}}',
    })