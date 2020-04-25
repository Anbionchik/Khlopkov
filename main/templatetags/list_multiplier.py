from django import template
from Khlopkov.settings import MIN_ELEMENTS

register = template.Library()


@register.filter()
def list_multiplier(some_list):
    result_list = []
    a = MIN_ELEMENTS - len(some_list)
    for i in range(a):
        result_list.append('')
    return result_list
