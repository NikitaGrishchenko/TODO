from django.contrib.admin import register, ModelAdmin
from django.contrib import admin
from .models import Todo, Priority


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass
