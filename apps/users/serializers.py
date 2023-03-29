from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.serializers import ModelSerializer

from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    auto_parks = AutoParkSerializer(many=True, read_only=True)

    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'auto_parks')


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile'
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
