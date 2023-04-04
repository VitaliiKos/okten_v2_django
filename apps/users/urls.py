from django.urls import path

from .views import (
    AdminToUserView,
    BlockAdminView,
    BlockUserView,
    TestSendEmailView,
    UnblockAdminView,
    UnblockUserView,
    UserListView,
    UserProfileUpdateView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('/test', TestSendEmailView.as_view(), name='send_email'),
    path('/profile', UserProfileUpdateView.as_view(), name='users_profile_update'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='users_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block-user', BlockUserView.as_view(), name='block-user'),
    path('/<int:pk>/unblock-user', UnblockUserView.as_view(), name='unblock-user'),
    path('/<int:pk>/block-admin', BlockAdminView.as_view(), name='block-admin'),
    path('/<int:pk>/unblock-admin', UnblockAdminView.as_view(), name='unblock-admin'),

]
