from django import template

register = template.Library()

@register.filter(name='split')
def split_string(value, key):
    """
    Splits the string on the key and returns a list of strings.
    """
    return value.split(key)