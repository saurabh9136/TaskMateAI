import os
import google.generativeai as genai
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Tasks, AIResponse
from .serializers import TaskSerializer, UserSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})

def clean_ai_response(ai_text):
    # Only replace escape sequences if absolutely necessary
    clean_text = ai_text.replace("\\n", "\n").replace("\\'", "'").replace('\\"', '"')
    return clean_text.strip()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        
        task = serializer.save(user=self.request.user)

        # Generate AI response
        content = f"Provide a concise solution or key points to complete this task: {task.task_title} - {task.task_description} in exactly 5 bullet points, focusing only on the main steps or code-related details without unnecessary explanations."

        
        try:
            # Initialize chat session and generate response
            chat_session = genai.GenerativeModel(model_name="gemini-1.5-flash").start_chat()
            response = chat_session.send_message(content)

            # Access the AI response text correctly
            if response.parts and response.parts[0].text:
                ai_response_text = response.parts[0].text
            else:
                raise ValueError("No valid AI response found")

            # Clean the AI response text
            clean_text = clean_ai_response(ai_response_text)

            # Save AI response
            ai_response = AIResponse.objects.create(ai_text=clean_text)
            task.ai_response = ai_response
            task.save()

        except Exception as e:
            print(f"Error generating AI response: {e}")
            task.ai_response = None
            task.save()


