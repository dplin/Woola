#from users.models import User
from rest_framework import serializers
from .models import Item

class GapSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item
    fields = ('id', 'item_name', 'item_price', 'item_id', 'item_url', 'item_image',)
