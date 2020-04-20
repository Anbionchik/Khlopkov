from django import template

register = template.Library()



@register.filter()
def list_multiplier(some_list):
    result_list = []
    a = 6 - len(some_list)
    for i in range(a):
        result_list.append('')
    return result_list
