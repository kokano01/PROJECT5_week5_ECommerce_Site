from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.apps import apps
from rest_framework.serializers import Serializer


#import models
# from blog, get Post model
Item = apps.get_model('store', 'Item')  

# import serializers
from .serializers import ItemSerializer

@api_view(["GET"])
def index(request):
    return Response({'hello': 'there'}) 

@api_view(['GET'])
def items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)  # querying a list of posts, so we do many=True. if only one to query, many = false
    return Response(serializer.data)


@api_view(["GET"])
def individualItem(request, item_id): # always takes in request, but this needs a path parameter as well
    item = Item.objects.get(id=item_id)
    serializer=ItemSerializer(item, many=False)
    return Response(serializer.data)