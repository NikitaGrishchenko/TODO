from rest_framework import serializers
from ..models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    """ Список задач """

    class Meta:
        model = Todo
        fields = "__all__"
