from django.contrib.admin import register, ModelAdmin
from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass


# @admin.register(Category)
# class CategoryAdmin(BaseAdminMixin, admin.ModelAdmin):
#     pass

