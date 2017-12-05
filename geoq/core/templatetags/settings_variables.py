from django import template
from django.conf import settings

register = template.Library()


# gamification host
@register.assignment_tag
def settings_value(name):
    return getattr(settings, name, "")