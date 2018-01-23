from django.contrib import admin

from .models import Showstories


@admin.register(Showstories)
class ShowstoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'by', 'descendants', 'kids', 'score', 'text', 'time', 'title', 'type', 'url']
