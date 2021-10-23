from django.contrib import admin

from museum.models import Item, ItemImage, Category


admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Category)
