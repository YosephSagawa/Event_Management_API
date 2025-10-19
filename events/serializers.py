from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import timezone
from .models import Event, Registration, Category

User = get_user_model() # Gets the customer User Model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at'] # Auto-generatedd fields

    def create(self, validated_data):
        # Create user with hashed password
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        user.role = validated_data.get('role', 'user')
        user.save()
        return user
    
class EventSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'date', 'category', 'author', 'capacity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author','created_at', 'updated_at']

    # Function to prevent past dates
    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role # Add custom claims to the token
        return token
    
class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') # Show username
    event = serializers.ReadOnlyField(source='event.title') # Show event title

    class Meta:
        model = Registration
        field = ['id', 'user', 'event', 'status', 'created_at']
        read_only_fields = ['id', 'user', 'event', 'status','created_at']

class CaategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','created_at']
        read_only_fields = ['id','created_at']
        