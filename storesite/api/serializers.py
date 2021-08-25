from rest_framework import serializers

from django.apps import apps

Item = apps.get_model('store', 'Item')  

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' # grabs all the fields; title, author, content, date posted. json-able 

