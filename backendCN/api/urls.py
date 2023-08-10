
from django.urls import path
from api import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("api/users/", views.UsersAPI.as_view(), name = "users"),
    path("api/users/<str:query>/", views.UsersAPI.as_view(), name = "usersSearch"),
    path("api/users/<int:pk>", views.UsersAPI.as_view(), name = "usersDetails")
]
