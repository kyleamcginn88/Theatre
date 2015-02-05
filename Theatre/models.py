from django.db import models

class MovieInfo(models.Model):
    name = models.CharField(max_length = 254)
    description = models.CharField(max_length = 254)

class Movie(models.Model):
    title = models.CharField(max_length = 30)
    time = models.CharField(max_length = 30)


class Info(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)
    rating = models.CharField(max_length = 400)
    thumbnail = models.CharField(max_length = 400)
    duration = models.CharField(max_length = 400)

class Store(models.Model):
    item = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    price = models.CharField(max_length = 40)
    thumbnail = models.CharField(max_length = 400)

class location(models.Model):
    item = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    price = models.CharField(max_length = 40)
    thumbnail = models.CharField(max_length = 400)