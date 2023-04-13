import os

from apps.users.models import UserModel as User
from configs.celery import app
from core.services.jwt_service import (ActivateToken, JWTService,
                                       RecoveryPasswordToken)
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

UserModel: User = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject=''):
        # Завантажуємо вміст шаблону та форматуємо його за допомогою контексту
        template = get_template(template_name)
        html_content = template.render(context)
        # Створюємо об'єкт повідомлення та заповнюємо його поля
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        # Надсилаємо повідомлення
        msg.send()

    @classmethod
    def register_email(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email.delay(user.email, 'register.html', {'name': user.profile.name, 'url': url}, 'Register')

    @classmethod
    def recovery_password(cls, user):
        token = JWTService.create_token(user, RecoveryPasswordToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email(user.email, 'recover_password.html', {'url': url}, 'Recovery Password')

    @staticmethod
    # @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, 'spam.html', {}, 'Spam')
