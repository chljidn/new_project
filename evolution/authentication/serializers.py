from rest_framework import serializers
from authentication.models import User

class user_serializer(serializers.ModelSerializer):
    # address =
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birth']

