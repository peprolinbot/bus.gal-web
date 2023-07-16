from django import template
from django.urls import reverse
from django.utils.html import mark_safe

register = template.Library()


@register.filter()
def form_stop_string(value):
    return f"{value.id}/{value.type}/{value.name}"


@register.filter()
def stop_button(value):
    return mark_safe(f'<button class="btn btn-outline-secondary" data-bs-toggle="popover" data-bs-html="true"'
                     f'data-bs-title="Set as..."'
                     f'data-bs-content="<a href=\'{reverse("buses:index")}?origin={form_stop_string(value)}\' class=\'btn btn-primary\'>Origin</a> '
                     f'<a href=\'{reverse("buses:index")}?destination={form_stop_string(value)}\' class=\'btn btn-primary\'>Destination</a>">'
                     f'{value.name}</button>')
