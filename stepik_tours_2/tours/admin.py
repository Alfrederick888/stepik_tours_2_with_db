from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

class CardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'departure', 'picture', 'date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'departure')
    list_editable = ('is_published',)
    list_filter = ('is_published',)

admin.site.register(Cards, CardsAdmin)
