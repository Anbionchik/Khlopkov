from django.shortcuts import render


data = {
    'lists': [
        {'name': 'Купить шариков', 'is_done': True, 'date': ''},
        {'name': 'Заказать торт', 'is_done': False, 'date': '01.02.03'},
        {'name': 'Разослать приглашения', 'is_done': True, 'date': ''}
    ],
    'user_name' : 'Admin',
}


def list_item_view(request):
    context = data
    return render(request, 'list.html', context)


def edit_view(request, pk):
    pass
