from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model dynamically
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Explicitly define password as a CharField and set it to write_only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Use the custom user model
        fields = ['username', 'password', 'bio', 'profile_picture']  # Include necessary fields

    def create(self, validated_data):
        # Use get_user_model().objects.create_user to create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the newly registered user
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    # LoginSerializer to handle user login with username and password
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
