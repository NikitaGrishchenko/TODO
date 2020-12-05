from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    PRIORITY = (
        ("T", "3ур"),
        ("S", "2ур"),
        ("F", "1ур"),
        ("Z", "Обычный"),
    )

    title = models.CharField(blank=True, max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    editing = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=100, choices=PRIORITY, default="Z", null=True
    )
    date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
