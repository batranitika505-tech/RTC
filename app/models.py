from django.db import models


class Crack(models.Model):
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)
	location = models.CharField(max_length=100)


class Obstacle(models.Model):
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)
	location = models.CharField(max_length=100)
