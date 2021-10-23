from django.contrib import admin

from people.models import Person, Position

admin.site.register(Person)
admin.site.register(Position)