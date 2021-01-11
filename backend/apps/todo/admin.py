from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from .models import Priority, Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "created",
        "priority",
        "completed",
    )


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass
