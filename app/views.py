from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Crack, Obstacle
from .serializers import CrackSerializer, ObstacleSerializer


class CrackView(APIView):

	def get(self, request, format=None):
		cracks = Crack.objects.all()
		serializer = CrackSerializer(cracks, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CrackSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObstacleView(APIView):

	def get(self, request, format=None):
		obstacles = Obstacle.objects.all()
		serializer = ObstacleSerializer(obstacles, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ObstacleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
