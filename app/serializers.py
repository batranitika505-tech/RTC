from rest_framework import serializers
from .models import Crack, Obstacle


class CrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Crack
		fields = ('__all__')


class ObstacleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Obstacle
		fields = ('__all__')
