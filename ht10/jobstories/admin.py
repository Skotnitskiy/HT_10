from django.contrib import admin

from .models import Jobstories


@admin.register(Jobstories)
class JobstoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'by', 'descendants', 'kids', 'score', 'text', 'time', 'title', 'type', 'url']
