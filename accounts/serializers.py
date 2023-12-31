from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import profile,Contact
from api.serializers import PlayListSerilizers,roadMapsSerilizers,trackSerilizers,resourcesSerilizers
from api.models import playList,Resources,RoadMaps,Track


class UserSerializer(serializers.ModelSerializer):
    track = serializers.StringRelatedField()
    class Meta:
        model=get_user_model() 
        fields=('username','email','track')
    def get_email(self, obj):
        return self.context['track']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Use get_user_model() to get the custom user model
        fields = ('id', 'username', 'email', 'password', 'track')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if self.Meta.model.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError('This email address is already in use.')
        else:
            user = self.Meta.model.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                track=validated_data['track']
            )
            return user
        


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField() 
    roadmaps = serializers.SerializerMethodField()
    playList = serializers.SerializerMethodField()
    resource = serializers.SerializerMethodField()

    class Meta:
        model = profile
        fields = ['username', 'roadmaps', 'playList', 'resource']
    def get_username(self, obj):
        return obj.user.username
    def get_roadmaps(self, obj):
     roadmaps = RoadMaps.objects.filter(profile=obj)
     serializer = roadMapsSerilizers(roadmaps, many=True, context=self.context)
     return serializer.data

    def get_playList(self, obj):
      playlist = playList.objects.filter(profile=obj)
      serializer = PlayListSerilizers(playlist, many=True, context=self.context)
      return serializer.data

    def get_resource(self, obj):
       resources = Resources.objects.filter(profile=obj)
       serializer = resourcesSerilizers(resources, many=True, context=self.context)
       return serializer.data


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'



