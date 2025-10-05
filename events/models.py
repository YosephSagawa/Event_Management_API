from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, Permission
# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('superuser', 'Superuser'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Override groups field to avoid reverse accessor clash
    groups = models.ManyToManyField(
        Group,
        related_name='events_user_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='events_user',
    )

    # Override user_permissions field to avoid reverse accessor clash
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='events_user_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='events_user',
    )

    def __str__(self):
        return self.username

# Category model for event categorization
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Event model with added capacity field as per requirements
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()  # Date and Time
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Optional category (stretch)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')  # Organizer
    capacity = models.PositiveIntegerField(default=0)  # Added for capacity management
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Custom method to check if event is upcoming
    def is_upcoming(self):
        return self.date > timezone.now()

# Favorite model as per schema
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
        indexes = [
            models.Index(fields=['user', 'event']),
        ]

    def __str__(self):
        return f"{self.user.username} favorites {self.event.title}"

# Additional model for event registrations
# This is added to fulfill the capacity management and registration requirements
class Registration(models.Model):
    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('waiting', 'Waiting'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"