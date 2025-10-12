from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, EventSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from .models import Event
from django.utils import timezone
from django.db.models import Q

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # Allow anyone to register

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully."
        }, status=status.HTTP_201_CREATED)
    
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# User Management Views
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can list all users

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def has_object_permission(self, request, view, obj):
        # Allow users to view/update their own profile, admins can do all
        if request.user.is_staff or request.user == obj:
            return True
        return False

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated] # Must be logged in to list and create events

    def get_queryset(self):
        # Filter events that are in the future
        queryset = Event.objects.filter(date__gt = timezone.now())
        # Filter events based on query parameters
        title = self.request.query_params.get('title')
        location = self.request.query_params.get('location')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset
    
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly] #Authenticated and logged in + ownership for update/delete