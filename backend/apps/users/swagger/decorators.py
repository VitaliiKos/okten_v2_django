from apps.users.swagger.serializers import SwaggerProfileSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


def user_list_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'get'
    )


def block_user_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'patch'
    )


def unblock_user_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'patch'
    )


def block_admin_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'patch'
    )


def unblock_admin_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'patch'
    )


def admin_to_user_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'patch'
    )


def user_to_admin_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerProfileSerializer()
        }),
        'patch'
    )
