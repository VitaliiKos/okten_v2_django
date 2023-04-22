from core.services.email_service import EmailService
from core.services.jwt_service import (ActivateToken, JWTService,
                                       RecoveryPasswordToken, SocketToken)
from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     RetrieveAPIView, get_object_or_404)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from .serializers import (EmailSerializer, PasswordSerializer,
                          TokenPairSerializer)
from .swagger.decorators import (activate_user_swagger, auth_me_swagger,
                                 auth_register_swagger, token_pair_swagger)

UserModel: User = get_user_model()


@token_pair_swagger()
class TokenPairView(TokenObtainPairView):
    """
        Login
    """
    serializer_class = TokenPairSerializer
    permission_classes = (AllowAny,)


@activate_user_swagger()
class ActivateUserView(GenericAPIView):
    """
    Activate User by token
    """
    permission_classes = (AllowAny,)

    @staticmethod
    def get(*args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@auth_me_swagger()
class AuthMeView(RetrieveAPIView):
    """
    Return authorization user
    """
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_object(self):
        return self.request.user


class RecoverPasswordView(GenericAPIView):
    """
    Request password recovery
    """
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: ''}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = get_object_or_404(UserModel, email=email)
        user.save()
        EmailService.recovery_password(user)
        return Response(status=status.HTTP_200_OK)


class RecoverPasswordConfirmView(GenericAPIView):
    """
    Set recovery password
    """
    serializer_class = PasswordSerializer
    permission_classes = (AllowAny,)

    @atomic
    @swagger_auto_schema(responses={status.HTTP_200_OK: ''}, security=[])
    def post(self, *args, **kwargs):
        token = kwargs['token']
        user: User = JWTService.validate_token(token, RecoveryPasswordToken)
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.set_password(data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK)


@auth_register_swagger()
class AuthRegisterView(CreateAPIView):
    """
    Register User
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class SocketTokenView(GenericAPIView):
    def get(self, *args, **kwargs):
        user = self.request.user
        token = JWTService.create_token(user, SocketToken)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)
