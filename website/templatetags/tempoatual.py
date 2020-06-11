import datetime
from django import template

register = template.Library()

@register.simple_tag
def tempoatual():
    return datetime.datetime.now().strftime('%H:%M:%S')
