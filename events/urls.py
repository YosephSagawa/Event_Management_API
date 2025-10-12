from django.urls import path
from .views import RegisterView, LoginView, EventListCreateView, EventDetailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("events/", EventListCreateView.as_View(), name='event-list-create'),
    path("events/<int:pk>/", EventDetailView.as_view(), name='event-detail'),
]