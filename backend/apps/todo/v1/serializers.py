from rest_framework import serializers
from ..models import Todo, Priority

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

    # priority = PriorityListSerializer()
    # priority_color = serializers.CharField(default=priority_color_def)

    class Meta:
        model = Todo
        fields = "__all__"
