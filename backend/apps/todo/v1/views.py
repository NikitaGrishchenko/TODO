from rest_framework import generics
from ..models import Todo
from .serializers import TodoListSerializer
from rest_framework.permissions import IsAuthenticated
from coreapi.auth import BasicAuthentication, SessionAuthentication
from django.contrib.auth.decorators import login_required


class TodoListView(generics.ListCreateAPIView):
    """ Вывод списка задач """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()

    @login_required
    def my_view(request):
        pass


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление, удаление, детальная информация задачи """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()
