from django.contrib import admin

from .models import Newstories


@admin.register(Newstories)
class NewstoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'by', 'descendants', 'kids', 'score', 'text', 'time', 'title', 'type', 'url']
