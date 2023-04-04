from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from core.permissions.is_superuser import IsAdminUser, IsSuperUser
from core.services.email_service import EmailService

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

from .serializers import ProfileSerializer, UserSerializer

UserModel: User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = UserModel.objects.exclude(pk=self.request.user.pk)
        return queryset


class UserProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()

    def get_object(self):
        return self.request.user.profile


class UserToAdminView(GenericAPIView):
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
    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not self.request.user.is_staff or (user.is_staff and not self.request.user.is_superuser):
            return Response('Error occurred. You do not have permission to do this!',
                            status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response('Error occurred while blocking the user.', status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnblockUserView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not self.request.user.is_staff or (user.is_staff and not self.request.user.is_superuser):
            return Response('Error occurred.  You do not have permission to do this!',
                            status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            return Response('Error occurred while unblocking the user.', status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlockAdminView(GenericAPIView):
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


class TestSendEmailView(GenericAPIView):
    def get(self, *args, **kwargs):
        EmailService.send_email({'user': 'Max'})
        return Response(status=status.HTTP_200_OK)
