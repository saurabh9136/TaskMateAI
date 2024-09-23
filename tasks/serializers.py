from rest_framework import serializers
from .models import AIResponse, Tasks
from rest_framework.serializers import Serializer, CharField
from django.contrib.auth.models import User

class UserSerializer(Serializer):
    username = CharField(max_length=150)
    password = CharField(write_only=True)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIResponse
        fields = ['ai_text']
        
class TaskSerializer(serializers.ModelSerializer):
    ai_response = AIResponseSerializer(read_only=True)
    class Meta:
        model = Tasks
        fields = ['id', 'user', 'task_title', 'task_description', 'status', 'ai_response']

