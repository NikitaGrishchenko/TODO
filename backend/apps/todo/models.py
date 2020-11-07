from datetime import timedelta
from django.db import models
from django.utils import timezone


def get_due_date():
    """ На выполнение задачи по-умолчанию даётся один день """
    return timezone.now() + timedelta(days=1)


class Todo(models.Model):
    title = models.CharField(blank=True, max_length=250)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    editing = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
