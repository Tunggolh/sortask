from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.Board)
admin.site.register(models.Task)
admin.site.register(models.CheckList)
admin.site.register(models.Comment)
