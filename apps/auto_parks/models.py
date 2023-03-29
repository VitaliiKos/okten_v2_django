from core.enums.regex_enum import RegEx
from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

UserModel = get_user_model()


class AutoParksModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')

