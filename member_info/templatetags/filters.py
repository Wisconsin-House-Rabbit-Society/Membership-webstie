from django import template
from django.forms import BoundField

register = template.Library()

@register.filter(name='addplaceholder')
def addplaceholder(value: BoundField, arg: str):
        return value.as_widget(attrs={"placeholder": arg})