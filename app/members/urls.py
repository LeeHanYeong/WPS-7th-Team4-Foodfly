from django.urls import path

from .apis import (
    SignupView,
    AuthTokenView,
    ProfileView,
)

app_name = 'members'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('auth-token/', AuthTokenView.as_view(), name='auth-token'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
