from django import template

register = template.library()

@register.filter
def split(value, separator=","):
    """"Splits the string by the given separator"""
    if value:
        return value.split(separator)
    return []