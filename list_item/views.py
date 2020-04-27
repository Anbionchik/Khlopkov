from django.shortcuts import render
from main.models import ListModel
from list_item.models import ListItemModel


def list_item_view(request, pk=1):

    lists = ListItemModel.objects.filter(
        listmodel_id=pk
    ).order_by(
        'created'
    )
    header = ListModel.objects.filter(
        id=pk,
    ).values_list(
        'name',
        flat=True
    ).distinct()

    context = {
        'lists': lists,
        'header': header[0],

    }
    return render(request, 'list.html', context)


def edit_view(request, pk):
    pass
