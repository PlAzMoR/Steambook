from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = "posts/index.html"
    return render(request, template)

def about(request):
    return HttpResponse("<h2>О нас<h2>")
