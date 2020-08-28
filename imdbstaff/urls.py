from django.urls import path
from . import views
urlpatterns = [
    path('imdbstaff/user/', views.CreateEditUserApiView.as_view(), name="user-create"),
    path('imdbstaff/user/<int:pk>/', views.CreateEditUserApiView.as_view(), name="user-edit"),
    ]