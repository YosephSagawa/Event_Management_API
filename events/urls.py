from django.urls import path
from .views import RegisterView, LoginView, EventListCreateView, EventDetailView, UserListView,UserDetailView, EventRegisterView, CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("events/", EventListCreateView.as_view(), name='event-list-create'),
    path("events/<int:pk>/", EventDetailView.as_view(), name='event-detail'),
    path("users/", UserListView.as_view(), name='user-list'),
    path("users/<int:pk>/", UserDetailView.as_view(), name='user-detail'),
    path("events/<int:pk>/register/", EventRegisterView.as_view(), name='event-register'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]