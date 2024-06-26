from rest_framework import serializers
from .models import *
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')