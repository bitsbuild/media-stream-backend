from rest_framework.authtoken.views import obtain_auth_token
from user.views import create_user,delete_user
from django.urls import path
urlpatterns = [
    path('signup/',create_user,name='signup'),
    path('login/',obtain_auth_token,name='login'),
    path('delete/',delete_user,name='delete')
]
