from django.shortcuts import render


data = {
    'lists': [
        {'name': 'Работа', 'is_done': True},
        {'name': 'Дом', 'is_done': False},
        {'name': 'Учёба', 'is_done': True},
        {'name': 'Дела_1', 'is_done': True},
        {'name': 'Дела_2', 'is_done': True},
        {'name': 'Дела_3', 'is_done': False},
        {'name': 'Дела_4', 'is_done': True},
        {'name': 'Дела_5', 'is_done': True},
    ],
    'user_name' : 'Admin',
}
# for list in data['lists']:
#     name = list[0]
#     is_done = list[1]

def main_view(request):
    context = data
    return render(request, 'index.html', context)
