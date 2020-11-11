from django.urls import path

from .views import TodoListView, TodoDetailView

app_name = "todo"

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("<int:pk>/", TodoDetailView.as_view()),
]