from rest_framework import serializers
from authentication.models import User, general_user


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birth']

class general_user_serializer(serializers.ModelSerializer):
    user = user_serializer(read_only=True)
    class Meta:
        model = general_user
        fields = ['user']

