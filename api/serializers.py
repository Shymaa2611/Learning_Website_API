from rest_framework import serializers
from .models import Track,playList,Resources,RoadMaps

class trackSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Track
        fields='__all__'

class roadMapsSerilizers(serializers.ModelSerializer):
    class Meta:
        model=RoadMaps
        fields='__all__'

class PlayListSerilizers(serializers.ModelSerializer):
    class Meta:
        model=playList
        fields='__all__'


class resourcesSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Resources
        fields='__all__'