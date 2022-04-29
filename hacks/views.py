from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Hack


def index(request):
    hack = Hack.get_tiny_hack()
    template = loader.get_template('hacks/index.html')
    context = {
        'hack': hack,
    }
    return HttpResponse(template.render(context, request))