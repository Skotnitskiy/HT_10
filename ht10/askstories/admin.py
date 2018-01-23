from django.contrib import admin

from .models import Askstories


@admin.register(Askstories)
class AskstoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'by', 'descendants', 'kids', 'score', 'text', 'time', 'title', 'type', 'url']
