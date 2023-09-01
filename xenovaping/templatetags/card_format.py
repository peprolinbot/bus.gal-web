from django import template

register = template.Library()


@register.filter()
def add_card_number_spaces(value):
    s = str(value)
    return ' '.join([s[i:i+4] for i in range(0, 16, 4)])
