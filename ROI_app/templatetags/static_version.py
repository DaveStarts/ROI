import os
from django import template
from django.templatetags.static import static
from django.conf import settings

register = template.Library()

@register.simple_tag
def static_version(path):
    full_path = os.path.join(settings.BASE_DIR, 'static', path)
    if os.path.exists(full_path):
        version = int(os.path.getmtime(full_path))
        return f"{static(path)}?v={version}"
    return static(path)