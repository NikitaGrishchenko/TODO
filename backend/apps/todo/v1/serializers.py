from rest_framework import serializers

from ..models import Priority, Todo

# from drf_writable_nested import WritableNestedModelSerializer


# def priority_color_def():
#     return Priority.object.filter(pk=1)


class PriorityListSerializer(serializers.ModelSerializer):
    """ Список задач """

    class Meta:
        model = Priority
        fields = ["pk", "name", "color"]


class TodoListSerializer(serializers.ModelSerializer):
    """ Список задач """

    date = serializers.DateField(
        format="%d-%m-%Y",
    )

    class Meta:
        model = Todo
        fields = "__all__"
