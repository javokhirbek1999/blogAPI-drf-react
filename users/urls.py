from django.urls import path

from .views import UserRegister

app_name = 'users'

urlpatterns = [
    path('register/',UserRegister.as_view(),name='create_user'),
]