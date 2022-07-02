from .models import Hack
from rest_framework import serializers


class HackSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.CharField(source="project.name")
    description = serializers.CharField(source='project.description')
    client = serializers.CharField(source='client.name')
    api = serializers.CharField(source='api.name')
    persistence = serializers.CharField(source='persistence.name')

    class Meta:
        model = Hack
        fields = ['id', 'project', 'description', 'client', 'api', 'persistence']