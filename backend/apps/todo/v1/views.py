from rest_framework import generics
from ..models import Todo
from .serializers import TodoListSerializer
from rest_framework.permissions import IsAuthenticated


class TodoListView(generics.ListCreateAPIView):
    """ Вывод списка задач """

    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление, удаление, детальная информация задачи """

    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()
