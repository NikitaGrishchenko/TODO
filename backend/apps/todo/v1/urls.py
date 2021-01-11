from django.urls import path

from .views import TodoListView, TodoDetailView, PriorityListView

app_name = "todo"

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo-detail"),
    path("priority/", PriorityListView.as_view(), name="todo-priority"),
]
