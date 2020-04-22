from django.shortcuts import render


data = {
    'lists': [
        {'id': 1, 'name': 'Работа', 'is_done': True},
        {'id': 2,'name': 'Дом', 'is_done': False},
        {'id': 3,'name': 'Учёба', 'is_done': True},
        {'id': 4,'name': 'Дела_1', 'is_done': True},
        {'id': 5,'name': 'Дела_2', 'is_done': True},
        {'id': 6,'name': 'Дела_3', 'is_done': False},
        {'id': 7,'name': 'Дела_4', 'is_done': True},
        {'id': 8,'name': 'Дела_5', 'is_done': True},
    ],
    'user_name' : 'Admin',
}
# for list in data['lists']:
#     name = list[0]
#     is_done = list[1]

def main_view(request):
    context = data
    return render(request, 'index.html', context)

def edit_view(request, pk):
    pass
