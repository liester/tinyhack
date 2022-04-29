from django.contrib import admin

from .models import Project, Client, Api, Persistence

admin.site.register(Client)
admin.site.register(Api)
admin.site.register(Persistence)
admin.site.register(Project)
