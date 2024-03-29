from django.db import models


class Room(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Message(models.Model):
  value = models.CharField(max_length=10000)
  date_send = models.DateTimeField(auto_now_add=True)
  user = models.CharField(max_length=10000)
  room = models.CharField(max_length=10000)