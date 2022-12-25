from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    profile = UserProfile()

    def te_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        user_profile_date = data.pop('profile')
        for key, value in user_profile_date.items():
            data.update({key: value})
        return data
    #
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_active", "is_staff", "password", "profile"]

        def create(self, validated_date):
            validated_date['password'] = make_password(validated_date['password'])
            validated_date['is_active'] = True
            validated_date['is_staff'] = True
            user = User.objects.create(**validated_date)
            return user


