import random

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Api(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Persistence(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Size(models.TextChoices):
        LARGE = "large", "Large"
        MEDIUM = "medium", "Medium"
        SMALL = "small", "Small"

    size = models.CharField("Size", max_length=20, choices=Size.choices, default=Size.MEDIUM)

    def __str__(self):
        return self.name


class Hack(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    api = models.ForeignKey(Api, on_delete=models.DO_NOTHING)
    persistence = models.ForeignKey(Persistence, on_delete=models.DO_NOTHING)

    @staticmethod
    def get_tiny_hack():
        # if project_size:
        #     project = Project.objects.filter(size=project_size)[0]
        # else:
        #     project = Project.objects.all()[0]
        project = random.choice(Project.objects.all())
        client = random.choice(Client.objects.all())
        api = random.choice(Api.objects.all())
        persistence = random.choice(Persistence.objects.all())
        return Hack(project=project, client=client, api=api, persistence=persistence)
