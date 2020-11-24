from rest_framework import serializers
from ness_elastic.users.models import User

class CreateAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',])
    
    def create(self, validated_data):
        return User(**validated_data)
