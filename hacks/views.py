from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

from .models import Hack
from .serializers import HackSerializer


def index(request):
    hack = Hack.get_tiny_hack()
    template = loader.get_template('hacks/index.html')
    context = {
        'hack': hack,
    }
    return HttpResponse(template.render(context, request))


class HackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    project = Hack.get_tiny_hack()
    project.save()
    queryset = Hack.objects.filter(pk=project.id)
    serializer_class = HackSerializer
