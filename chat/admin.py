from django.contrib import admin
from chat.models import Message
from chat.models import Room

# Register your models here.
admin.site.register(Message)
admin.site.register(Room)