from django.shortcuts import render
from main.models import ListModel


def main_view(request):
    """ Главная View """
    user = request.user

    try:
        lists = ListModel.objects.filter(
            user=user,
        ).order_by(
            'created'
        )
    except TypeError:
        lists = []

    context = {
        'lists': lists,
        'user': request.user.username
    }
    return render(request, 'index.html', context)


def edit_view(request, pk):
    pass
