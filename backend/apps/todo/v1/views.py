from rest_framework import generics
from ..models import Todo
from .serializers import TodoListSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

# from coreapi.auth import BasicAuthentication, SessionAuthentication


# @login_required(login_url="/login/")
class TodoListView(generics.ListCreateAPIView):
    """ Вывод списка задач """

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(user_id=user.pk)
        return queryset

    # @login_required
    # def my_view(request):
    #     pass


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление, удаление, детальная информация задачи """

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()
