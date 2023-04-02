from django import template

from tours.models import *

register = template.Library()

@register.simple_tag()
def get_cards():
    return Cards.objects.all()