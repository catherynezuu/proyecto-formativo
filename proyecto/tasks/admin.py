from django.contrib import admin
from .models import tasks
# Register your models here.

class tasksAdmin(admin.ModelAdmin):
    readonly_fields=("created",)
admin.site.register(tasks, tasksAdmin)