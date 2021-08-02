from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username', 'name', 'password')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        password = self.validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance