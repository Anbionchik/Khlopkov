from django.shortcuts import render
from main.models import ListModel
from list_item.models import ListItemModel
from django.http import Http404


def list_item_view(request, pk):

    user = request.user

    # Список со значениями для списка задач в шаблоне

    lists = ListItemModel.objects.filter(
        listmodel_id=pk
    ).order_by(
        'created'
    )

    # список из main.view

    main_list = ListModel.objects.filter(id=pk)

    header = main_list.values_list(
        'name',
        flat=True
    ).first()

    user_verification = main_list.values_list('user__username', flat=True).first()

    if user_verification != str(user):
        raise Http404

    context = {
        'lists': lists,
        'header': header,
    }
    return render(request, 'list.html', context)


def edit_view(request, pk):
    pass
