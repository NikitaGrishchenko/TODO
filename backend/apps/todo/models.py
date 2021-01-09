# from django.contrib.auth.models import User

from apps.user_auth.models import User
from django.db import models


class Priority(models.Model):
    """
    Приоритет задач
    """

    name = models.CharField(max_length=250)
    color = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Приоритет"
        verbose_name_plural = "Приоритеты"
        unique_together = ["name", "color"]

    def __str__(self):
        return self.name


class Todo(models.Model):
    """
    Задача
    """

    title = models.CharField(blank=True, max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    editing = models.BooleanField(default=False)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name="priority"
    )
    priority_color = models.CharField(blank=True, null=True, max_length=250)
    date = models.DateField(blank=True, null=True)

    def get_priority_color(self):
        color = self.priority.color
        return color

    def save(self, *args, **kwargs):
        self.priority_color = self.get_priority_color()
        super(Todo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
