from django.urls import path

from .views import UserRegister, BlacklistToken

app_name = 'users'

urlpatterns = [
    path('register/',UserRegister.as_view(),name='create_user'),
    path('logout/blacklist/', BlacklistToken.as_view(), name='blacklist'),
]