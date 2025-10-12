from django.urls import path
from .views import RegisterView, LoginView, EventListCreateView, EventDetailView, UserListView,UserDetailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("events/", EventListCreateView.as_view(), name='event-list-create'),
    path("events/<int:pk>/", EventDetailView.as_view(), name='event-detail'),
    path("users/", UserListView.as_view(), name='user-list'),
    path("users/<int:pk>/", UserDetailView.as_view(), name='user-detail'),
]