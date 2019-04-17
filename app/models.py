from django.db import models


class CrackLog(models.Model):
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)
	location = models.CharField(max_length=100)


class ObstacleLog(models.Model):
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)
	location = models.CharField(max_length=100)
