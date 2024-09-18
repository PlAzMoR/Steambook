from django.shortcuts import render
from .utils import get_page_context

from api.models import Airticket


def index(request):
    template = "posts/index.html"
    ticket_list = Airticket.objects.all()
    context = {
        "ticket_list": ticket_list,
    }
    return render(request, template, context)

def about(request):
    template = "about.html"
    return render(request, template)
