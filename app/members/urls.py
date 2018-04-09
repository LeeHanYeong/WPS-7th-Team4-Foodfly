from django.urls import path

from .apis import (
    AuthTokenView,
    ProfileView,
)

app_name = 'members'
urlpatterns = [
    path('auth-token/', AuthTokenView.as_view(), name='auth-token'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
