from rest_framework import serializers

# from drf_writable_nested.serializers import NestedUpdateMixin
from ..models import Todo


# class CategoryListSerializer(serializers.ModelSerializer):
#     """ Список категорий """

#     class Meta:
#         model = Category
#         fields = ["name"]


class TodoListSerializer(serializers.ModelSerializer):
    """ Список задач """

    # category = CategoryListSerializer()
    # category = serializers.CharField(source="category.name")

    class Meta:
        model = Todo
        fields = "__all__"

    # def create(self, validated_data):
    #     categories_data = validated_data.pop("category")
    #     todo = Todo.objects.create(**validated_data)
    #     Category.objects.create(**categories_data)
    #     return todo
