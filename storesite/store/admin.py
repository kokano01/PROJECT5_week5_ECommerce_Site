from django.contrib import admin

# Register your models here.
# import Post
from .models import Cart, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Cart)
