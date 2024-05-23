from django.shortcuts import render
from .utils import get_page_context

from .models import *


def index(request):
    template = "posts/index.html"
    post_list = Post.objects.all()
    context = {
        "post_list": get_page_context(request, post_list),
    }
    return render(request, template, context)

def about(request):
    pass
