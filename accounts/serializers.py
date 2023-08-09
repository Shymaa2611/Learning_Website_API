from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import profile
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
    user = serializers.StringRelatedField()
    roadmaps = serializers.SerializerMethodField()
    playList= serializers.SerializerMethodField()
    resource=serializers.SerializerMethodField()

    class Meta:
        model = profile
        fields = ['user', 'roadmaps','playList','resource']

    def get_roadmaps(self, obj):
        roadmap =RoadMaps.objects.filter(user=obj.user)
        serializer = roadMapsSerilizers(roadmap, many=True, context=self.context)
        return serializer.data
    def get_playList(self, obj):
        playlist=playList.objects.filter(user=obj.user)
        serializer =PlayListSerilizers(playlist, many=True, context=self.context)
        return serializer.data
    def get_resource(self, obj):
        resources=Resources.objects.filter(user=obj.user)
        serializer = resourcesSerilizers(resources, many=True, context=self.context)
        return serializer.data
