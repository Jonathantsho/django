from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title" , "created")
    prepopulated_fields = {"slug" : ("title", )}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.Entry, EntryAdmin)