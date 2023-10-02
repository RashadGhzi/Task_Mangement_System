from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photos', 'due_date', 'creation_date', 'priority', 'is_complete']
    list_filter = ['creation_date', 'due_date', 'priority', 'is_complete']
    search_fields = ['title']
