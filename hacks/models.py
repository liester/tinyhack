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
    # client = models.ForeignKey(Client, on_delete=models.SET_DEFAULT, default='VanillaJS')
    # api = models.ForeignKey(Api, on_delete=models.SET_DEFAULT, default='None')
    # persistence = models.ForeignKey(Persistence, on_delete=models.SET_DEFAULT, default='None')
