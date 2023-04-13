from core.permissions.block_unblock_permission import \
    BlockUnblockUserPermission
from core.permissions.is_superuser import IsAdminUser, IsSuperUser
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

from ..auth.swagger.serializers import SwaggerUserSerializer
from .serializers import ProfileSerializer, UserSerializer

UserModel: User = get_user_model()


class UserListView(ListAPIView):
    """
    List of users
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = UserModel.objects.exclude(pk=self.request.user.pk)
        return queryset


class UserProfileUpdateView(UpdateAPIView):
    """
    Update user profile by id
    """
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()

    def get_object(self):
        return self.request.user.profile


class UserToAdminView(GenericAPIView):
    """
    Update user status to Admin by id
    """
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    """
        Update Admin status to user by id
    """

    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlockUserView(GenericAPIView):
    """
       Block user by id
    """
    permission_classes = (BlockUnblockUserPermission,)

    def get_serializer_class(self):
        pass

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    @swagger_auto_schema(responses={status.HTTP_200_OK: SwaggerUserSerializer()})
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            return Response('Error occurred while blocking the user.', status=status.HTTP_400_BAD_REQUEST)

        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnblockUserView(GenericAPIView):
    """
       UnBlock user by id
    """
    permission_classes = (BlockUnblockUserPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            return Response('Error occurred while unblocking the user.', status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlockAdminView(GenericAPIView):
    """
       Block Admin by id
    """
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            return Response('Error occurred. User is not an admin!', status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response('Error occurred while blocking the user.', status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnblockAdminView(GenericAPIView):
    """
       UnBlock Admin by id
    """
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            return Response('Error occurred. User is not an admin!', status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            return Response('Error occurred while unblocking the user.', status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
