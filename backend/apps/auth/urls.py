from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (ActivateUserView, AuthMeView, AuthRegisterView,
                    RecoverPasswordConfirmView, RecoverPasswordView,
                    TokenPairView)

urlpatterns = [
    path('', TokenPairView.as_view(), name='auth_login'),
    path('/me', AuthMeView.as_view(), name='auth_me'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_users_activate'),
    path('/recovery_password', RecoverPasswordView.as_view(), name='recover_password'),
    path('/recovery_password/<str:token>', RecoverPasswordConfirmView.as_view(), name='password_reset_confirm'),
]
