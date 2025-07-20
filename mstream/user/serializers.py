from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'confirm_password'
        ]