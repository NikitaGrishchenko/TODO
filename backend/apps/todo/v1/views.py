from rest_framework import generics
from ..models import Todo
from .serializers import TodoListSerializer
from rest_framework.permissions import AllowAny


class TodoListView(generics.ListCreateAPIView):
    """ Вывод списка задач """

    permission_classes = [AllowAny]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление, удаление, детальная информация задачи """

    permission_classes = [AllowAny]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()
